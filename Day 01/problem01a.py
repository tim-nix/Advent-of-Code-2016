# The problem input consists of a list of
# direction and distances. You start at given
# coordinates (0,0) and face North. Following the
# provided sequence: either turn left (L) or right
# (R) 90 degrees, then walk forward the given
# number of blocks, ending at a new intersection.
#
# How many blocks away is the destination?

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

# Take the file input (a string), remove all
# commas, and split on whitespace into a list.
# Then, for each step, make a tuple consisting of
# each direction  ('L' or 'R') and distance (as
# an integer). Return the list.
def parseInput(values):
   values = values.replace(',', '')
   v_list = values.split()

   steps = list()
   for v in v_list:
      steps.append((v[0], int(v[1:])))

   return steps

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   fileInput = readFile("input1b.txt")
   steps = parseInput(fileInput[0])

   # The directions are used to maintain facing
   # with the initial facing as 'north'.
   directions = [ 'north', 'east', 'south', 'west' ]
   facing = 0

   # Initialize and track how far north and east
   # traverse from following the directions.
   north = 0
   east = 0

   # Iterate through the steps taken.
   for s in steps:
      # Update the direction you are facing.
      if s[0] == 'R':
         facing = (facing + 1) % len(directions)
      elif s[0] == 'L':
         facing = (facing - 1) % len(directions)
      else:
         print('Error: unknown direction!')

      # Based on the new direction, update the
      # total distance traveled.
      if directions[facing] == 'north':
         north += s[1]
      elif directions[facing] == 'south':
         north -= s[1]
      elif directions[facing] == 'east':
         east += s[1]
      elif directions[facing] == 'west':
         east -= s[1]
      
   # Display the results   
   print("Blocks away = " + str(abs(north) + abs(east)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
