# The problem input consists of a list of
# direction and distances. You start at given
# coordinates (0,0) and face North. Following the
# provided sequence: either turn left (L) or right
# (R) 90 degrees, then walk forward the given
# number of blocks, ending at a new intersection.
#
# How many blocks away is the first location you
# visit twice?

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

   # Initialize and track each location visited.
   path = [ (0, 0) ]

   # Iterate through the steps taken.
   for s in steps:
      # Update the direction you are facing.
      if s[0] == 'R':
         facing = (facing + 1) % len(directions)
      elif s[0] == 'L':
         facing = (facing - 1) % len(directions)
      else:
         print('Error: unknown direction!')

      # Based on the new direction, add all
      # locations visited along the traverse to
      # the next turn. First, find the last
      # location of this traverse.
      next_north = 0
      next_east = 0
      if directions[facing] == 'north':
         next_north = north + s[1]
      elif directions[facing] == 'south':
         next_north = north - s[1]
      elif directions[facing] == 'east':
         next_east = east + s[1]
      elif directions[facing] == 'west':
         next_east = east - s[1]

      # Now, append the new locations to the path.
      if directions[facing] == 'north':
         for n in range(north + 1, next_north + 1):
            path.append((east, n))
         north = next_north
      elif directions[facing] == 'south':
         for n in range(north - 1, next_north - 1, -1):
            path.append((east, n)) 
         north = next_north
      elif directions[facing] == 'east':
         for e in range(east + 1, next_east + 1):
            path.append((e, north))
         east = next_east
      elif directions[facing] == 'west':
         for e in range(east - 1, next_east - 1, -1):
            path.append((e, north)) 
         east = next_east
   
   # Determine the first location visited twice.
   for loc in path:
      if path.count(loc) > 1:
         location = loc
         break
   # Only displayed if no 'break' occurs.
   else:
      print('Error: location not found.')
      
   # Display the results   
   print("Blocks away = " + str(abs(location[0]) + abs(location[1])))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
