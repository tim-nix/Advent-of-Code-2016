# The problem input consists of a list of 
# instructions for scrambling the password. The
# scrambling function is a series of operations.
# Starting with the password to be scrambled,
# apply each operation in succession to the
# string. The individual operations behave as
# follows:
# - swap position X with position Y means that the
#   letters at indexes X and Y (counting from 0)
#   should be swapped.
# - swap letter X with letter Y means that the
#   letters X and Y should be swapped (regardless
#   of where they appear in the string).
# - rotate left/right X steps means that the whole
#   string should be rotated; for example, one
#   right rotation would turn abcd into dabc.
# - rotate based on position of letter X means
#   that the whole string should be rotated to the
#   right based on the index of letter X (counting
#   from 0) as determined before this instruction
#   does any rotations. Once the index is
#   determined, rotate the string to the right one
#   time, plus a number of times equal to that
#   index, plus one additional time if the index
#   was at least 4.
# - reverse positions X through Y means that the
#   span of letters at indexes X through Y
#   (including the letters at X and Y) should be
#   reversed in order.
# - move position X to position Y means that the
#   letter which is at index X should be removed
#   from the string, then inserted such that it
#   ends up at index Y.
#
# For this problem, we need to unscramble the
# scrambled password by reversing the scrambling
# process. What is the un-scrambled version of the
# scrambled password 'fbgdceah'?

import time       # For timing the execution
import itertools  # For permutations function.

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


# Convert the list of string operations into a
# list of tuples with the first element being the
# instruction type and the rest being the
# appropriate operands (integer or letter).
def parseInput(values):
   instructions = list()

   # Iterate through the instructions.
   for line in values:
      command = list()

      # Divide the instruction into parts.
      parts = line.split()
      command.append(parts[0])

      # Iterate through the parts and append the
      # appropriate operands.
      for i in range(len(parts[1:])):
         if parts[i] == 'position':
            if parts[i+1] != 'of':
               command.append(int(parts[i+1]))

         if parts[i] == 'positions':
            command.append(int(parts[i+1]))
            command.append(int(parts[i+3]))

         if parts[i] == 'letter':
            command.append(parts[i+1])

         if (parts[i] == 'left') or (parts[i] == 'right'):
            command.append(parts[i])
            command.append(int(parts[i+1]))
            
      # Add the instruction to the list.
      instructions.append(command)

   # Return the list of instructions.
   return instructions
      


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of tuples, each denoting a range of blocked
   # IP addresses.
   file_input = readFile("input21b.txt")
   instructions = parseInput(file_input)

   # Initialize the starting string (as a list).
   final_string = list('fbgdceah')

   # Create a list of the permutations of the
   # characters in the final string.
   test_strings = list(itertools.permutations(final_string))

   # Iterate through each permutation to determine
   # if it scrambled to the final string. 
   for t_string in test_strings:
      # Need to convert the string permutation to
      # a list so it can be modified (string) and
      # another (initial_string) to preserve the
      # initial string so it remains unmodified
      initial_string = [ s for s in t_string ]
      string = [ s for s in t_string ]
      
      # Iterate through each instruction.
      for line in instructions:
         # Handle the swap instruction.
         if line[0] == 'swap':
            # With integer operands.
            if isinstance(line[1], int):
               temp = string[line[1]]
               string[line[1]] = string[line[2]]
               string[line[2]] = temp
            # With letter operands.
            else:
               index1 = string.index(line[1])
               index2 = string.index(line[2])
               temp = string[index1]
               string[index1] = string[index2]
               string[index2] = temp

         # Reverse a portion of the string.
         elif line[0] == 'reverse':
            part1 = string[:line[1]]
            part2 = string[line[1]:line[2]+1]
            part3 = string[line[2]+1:]
            part2 = part2[::-1]
            string = part1 + part2 + part3

         # Rotate the string.
         elif line[0] == 'rotate':
            # Rotate left.
            if line[1] == 'left':
               for _ in range(line[2]):
                  item = string.pop(0)
                  string.append(item)

            # Rotate right.
            elif line[1] == 'right':
               for _ in range(line[2]):
                  item = string.pop(-1)
                  string.insert(0, item)

            # Rotate based on position.
            else:
               # First, find the index.
               index = string.index(line[1])
               
               # Rotate right once
               item = string.pop(-1)
               string.insert(0, item)

               # Plus as many times as the index. 
               for _ in range(index):
                  item = string.pop(-1)
                  string.insert(0, item)

               # Plus one more time if index >= 4.
               if index >= 4:
                  item = string.pop(-1)
                  string.insert(0, item)
                  
         # Move from first index to second index.
         elif line[0] == 'move':
            item = string.pop(line[1])
            string.insert(line[2], item)

      # Compare the resulting scrambled string
      # with the known scrambled string. If they
      # match then we have the initial string.
      if string == final_string:
         break

   # Display the resulting scrambled string.
   print('Resulting string = ' + ''.join(initial_string))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
