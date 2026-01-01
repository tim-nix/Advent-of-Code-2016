# The problem input consists of a list of steps
# for manipulating the pixels on a screen. The
# screen is 50 pixels wide and 6 pixels tall, all
# of which start off, and is capable of three
# somewhat peculiar operations:
# - rect AxB turns on all of the pixels in a
#   rectangle at the top-left of the screen which
#   is A wide and B tall.
# - rotate row y=A by B shifts all of the pixels
#   in row A (0 is the top row) right by B pixels.
#   Pixels that would fall off the right end
#   appear at the left end of the row.
# - rotate column x=A by B shifts all of the
#   pixels in column A (0 is the left column) down
#   by B pixels. Pixels that would fall off the
#   bottom appear at the top of the column.
#
# After all steps execute, what code is the screen
# trying to display?

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


# Convert the list of strings into a list of
# tuples containing necessary information.
def parseInput(values):
   instructions = list()

   # Iterate through the list of strings.
   for line in values:
      # Split the text into a list of strings.
      parts = line.split()

      # If the first string is 'rect', then
      # convert to tuple as ('rect', x, y) where x
      # and y denote the dimensions of the
      # rectangle to be lit.
      if parts[0] == 'rect':
         coords = parts[1].split('x')
         step = (parts[0], int(coords[0]), int(coords[1]))

      # If the first string is 'rotate', then
      # convert to tuple where the first element
      # is either an 'x' or a 'y' ('x'/'y' denotes
      # a column/row rotation. The second element
      # denotes the column/row, and the third
      # element denotes the size of the shift.
      elif parts[0] == 'rotate':
         shift = parts[2].split('=')
         step = (shift[0], int(shift[1]), int(parts[4]))

      # Add the constructed step to the list.
      instructions.append(step)

   # Return the list.
   return instructions


      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input8b.txt")
   instructions = parseInput(file_input)

   # Set the dimensions of the screen.
   max_x = 50
   max_y = 6

   # Initialize the screen with all pixels off.
   screen = [ [ '.' for i in range(max_x) ] for j in range(max_y) ]

   # Iterate through the steps and modify the
   # screen accordingly.
   for step in instructions:
      # Handle rectangle construction.
      if step[0] == 'rect':
         for y in range(step[2]):
            for x in range(step[1]):
               screen[y][x] = '#'

      # Handle column rotation.
      elif step[0] == 'x':
         for _ in range(step[2]):
            copy = [ screen[y][step[1]] for y in range(max_y) ]
            last = copy.pop(-1)
            copy.insert(0, last)
            for y in range(max_y):
               screen[y][step[1]] = copy[y]

      # Handle row rotation.
      elif step[0] == 'y':
         for _ in range(step[2]):
            copy = [ screen[step[1]][x] for x in range(max_x) ]
            last = copy.pop(-1)
            copy.insert(0, last)
            for x in range(max_x):
               screen[step[1]][x] = copy[x]

   # Display the resulting screen.
   for line in screen:
      print(''.join(line))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
