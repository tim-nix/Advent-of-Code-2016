# The problem input is a simple assembly language
# program. The code looks like it uses almost the
# same architecture and instruction set that the
# monorail computer used! You should be able to
# use the same assembunny interpreter for this as
# you did there, but with one new instruction:
# - tgl x toggles the instruction x away (pointing
#   at instructions like jnz does: positive means
#   forward; negative means backward):
# - For one-argument instructions, inc becomes
#   dec, and all other one-argument instructions
#   become inc.
# - For two-argument instructions, jnz becomes
#   cpy, and all other two-instructions become
#   jnz.
# - The arguments of a toggled instruction are not
#   affected.
# - If an attempt is made to toggle an instruction
#   outside the program, nothing happens.
# - If toggling produces an invalid instruction
#   (like cpy 1 2) and an attempt is later made to
#   execute that instruction, skip it instead.
# - If tgl toggles itself (for example, if a is 0,
#   tgl a would target itself and become inc a),
#   the resulting instruction is not executed
#   until the next time it is reached.
#
# Place the keypad entry (the number of eggs, 7)
# in register a, run the code, and then send the
# value left in register a to the safe. What value
# should be sent to the safe?

import time          # For timing the execution


# Read in the data file and convert it to a list
# of strings.
def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines


# Parse the file input into a list of tuples in
# which each tuple contains the mnemonic and
# operands. Direct operands are converted to
# integers and indirect operands (registers) are
# left as strings.
def parseInput(values):
   instructions = list()

   # Iterate through each line of file input.
   for line in values:
      # Split it into a list of strings.
      parts = line.split()

      # Iterate through the parts to build the
      # tuple instruction.
      instruction = list()
      for i in range(len(parts)):
         # If the string is a number, convert it
         # to an integer.
         if parts[i].isdigit():
            parts[i] = int(parts[i])
         # If the string is a negative number,
         # convert it to and integer.
         elif (parts[i][0] == '-') and (parts[i][1:].isdigit()):
            parts[i] = - int(parts[i][1:])

         # Add the part to the instruction.
         instruction.append(parts[i])

      # Add the instruction to the list.
      instructions.append(instruction)

   # Return the list.
   return instructions
         


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and process.   
   file_input = readFile("input23b.txt")
   instructions = parseInput(file_input)

   # Initialize the registers.
   registers = dict()
   registers['a'] = 7
   registers['b'] = 0
   registers['c'] = 0
   registers['d'] = 0

   # Iterate through the instructions as directed
   # by the updated instruction pointer (ip).
   ip = 0
   while ip < len(instructions):
      # Handle the copy instruction.
      if instructions[ip][0] == 'cpy':
         # Copy direct operand value.
         if isinstance(instructions[ip][1], int):
            registers[instructions[ip][2]] = instructions[ip][1]

         # Copy register value.
         else:
            registers[instructions[ip][2]] = registers[instructions[ip][1]]
         ip += 1

      # Handle the increment instruction.
      elif instructions[ip][0] == 'inc':
         registers[instructions[ip][1]] += 1
         ip += 1

      # Handle the decrement instruction.
      elif instructions[ip][0] == 'dec':
         registers[instructions[ip][1]] -= 1
         ip += 1

      # Handle the jump if not zero instruction.
      elif instructions[ip][0] == 'jnz':
         # Compare with direct operand.
         if isinstance(instructions[ip][1], int):
            if instructions[ip][1] != 0:
               if isinstance(instructions[ip][2], int):
                  ip += instructions[ip][2]
               else:
                  ip += registers[instructions[ip][2]]
            else:
               ip += 1

         # Compare with register value.
         else:
            if registers[instructions[ip][1]] != 0:
               ip += instructions[ip][2]
            else:
               ip += 1

      # Handle the toggle instruction.
      elif instructions[ip][0] == 'tgl':
         offset = registers[instructions[ip][1]]

         # If an attempt is made to toggle an
         # instruction outside the program,
         # nothing happens.
         if (ip+offset) in range(len(instructions)):
            # For one-argument instructions, inc
            # becomes dec, and all other one-
            # argument instructions become inc.
            if len(instructions[ip+offset]) == 2:
               if instructions[ip+offset][0] == 'inc':
                  instructions[ip+offset][0] = 'dec'
               else:
                  instructions[ip+offset][0] = 'inc'

            # For two-argument instructions, jnz
            # becomes cpy, and all other two-
            # instructions become jnz.
            elif len(instructions[ip+offset]) == 3:
               if instructions[ip+offset][0] == 'jnz':
                  instructions[ip+offset][0] = 'cpy'
               else:
                  instructions[ip+offset][0] = 'jnz'       
         ip += 1

   # Display the contents of the 'a' register.
   print("Register 'a' contents = " + str(registers['a']))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
