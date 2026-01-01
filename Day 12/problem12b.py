# The problem input is a list of instructions in
# a simplified assembly language called assembunny
# code. We need to write a program that can
# execute the code and get the password. The
# assembunny code operates on four registers (a,
# b, c, and d) that start at 0 and can hold any
# integer. However, it seems to make use of only a
# few instructions:
# - cpy x y copies x (either an integer or the
#   value of a register) into register y.
# - inc x increases the value of register x by
#   one.
# - dec x decreases the value of register x by
#   one.
# - jnz x y jumps to an instruction y away
#   (positive means forward; negative means
#   backward), but only if x is not zero.
#
# If you instead initialize register c to be 1,
# what value is now left in register a?


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
      instructions.append(tuple(instruction))

   # Return the list.
   return instructions
         



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and process.   
   file_input = readFile("input12b.txt")
   instructions = parseInput(file_input)

   # Initialize the registers.
   registers = dict()
   registers['a'] = 0
   registers['b'] = 0
   registers['c'] = 1
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
               ip += instructions[ip][2]
            else:
               ip += 1

         # Compare with register value.
         else:
            if registers[instructions[ip][1]] != 0:
               ip += instructions[ip][2]
            else:
               ip += 1

   # Display the contents of the 'a' register.
   print("Register 'a' contents = " + str(registers['a']))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
