# The problem input is a simple assembly language
# program. It looks mostly compatible with code
# you worked on just recently. This antenna code,
# being a signal generator, uses one extra
# instruction:
# - out x transmits x (either an integer or the
#   value of a register) as the next value for
#   the clock signal.
# The code takes a value (via register a) that
# describes the signal to generate, but you're not
# sure how it's used. You'll have to find the
# input to produce the right signal through
# experimentation.
#
# What is the lowest positive integer that can be
# used to initialize register a and cause the code
# to output a clock signal of 0, 1, 0, 1...
# repeating forever?

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
   file_input = readFile("input25b.txt")
   instructions = parseInput(file_input)

   # Iterate through initial values for register a
   # until the correct value is found to generate
   # the repeating pattern.
   a_value = 0

   # Not sure if the first value is '0' or '1'.
   done_string1 = '010101010101'
   done_string2 = '101010101010'
   
   done = False
   while not done:
      # Initialize the registers.
      registers = dict()
      registers['a'] = a_value
      registers['b'] = 0
      registers['c'] = 0
      registers['d'] = 0

      # Iterate through the instructions as directed
      # by the updated instruction pointer (ip).
      ip = 0
      output = ''
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

         # Handle the out instruction.
         elif instructions[ip][0] == 'out':
            # Compare with direct operand.
            if isinstance(instructions[ip][1], int):
               output += str(instructions[ip][1])

            # Compare with register value.
            else:
               output += str(registers[instructions[ip][1]])
               
            ip += 1

            # Once enough output is generated,
            # compare with repeating patterns.
            if len(output) == len(done_string1):
               if (output == done_string1) or (output == done_string2):
                  done = True
               else:
                  a_value += 1
               break

   # Display the contents of the 'a' register.
   print("Register 'a' contents = " + str(a_value))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
