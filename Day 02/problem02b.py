# The problem input is a set of instructions for
# entering a code on a keypad. Eeach button to be
# pressed can be found by starting on the previous
# button and moving to adjacent buttons on the
# keypad: U moves up, D moves down, L moves left,
# and R moves right. Each line of instructions
# corresponds to one button, starting at the
# previous button (or, for the first line, the "5"
# button); press whatever button you're on at the
# end of each line. If a move doesn't lead to a
# button, ignore it. The keypad looks like this:
#
#      1
#    2 3 4
#  5 6 7 8 9
#    A B C
#      D
#
# What is the bathroom code?

import time     # For timing the execution

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

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   instructions = readFile("input2b.txt")

   # Define the keypad. Given the irregular shape,
   # pad around with 'X' values to simplify cases
   # when step results in moving off pad.
   keypad = [['X','X','X','X','X','X','X'],
             ['X','X','X','1','X','X','X'],
             ['X','X','2','3','4','X','X'],
             ['X','5','6','7','8','9','X'],
             ['X','X','A','B','C','X','X'],
             ['X','X','X','D','X','X','X'],
             ['X','X','X','X','X','X','X']]

   # Find the '5' button to start.
   current = list()
   for y in range(len(keypad)):
      for x in range(len(keypad[y])):
         if keypad[y][x] == '5':
            current.append(y)
            current.append(x)

   # Each button of the keycode is added here.
   keycode = list()

   # Iterate through each of the steps of the
   # instructions and track the current finger
   # position on the keypad. If position is off of
   # the keypad (equals 'X'), then undo the move.
   for y in range(len(instructions)):
      for x in range(len(instructions[y])):
         if instructions[y][x] == 'U':
            current[0] -= 1
            if keypad[current[0]][current[1]] == 'X':
               current[0] += 1
         elif instructions[y][x] == 'D':
            current[0] += 1
            if keypad[current[0]][current[1]] == 'X':
               current[0] -= 1
         elif instructions[y][x] == 'L':
            current[1] -= 1
            if keypad[current[0]][current[1]] == 'X':
               current[1] += 1
         elif instructions[y][x] == 'R':
            current[1] += 1
            if keypad[current[0]][current[1]] == 'X':
               current[1] -= 1

      # Add to the keycode, the button number of
      # the current position.
      keycode.append(keypad[current[0]][current[1]])
         
   # Display the results   
   print("Key code = " + ''.join(keycode))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
