# The problem input is an integer value serving as
# a seed for the deterministic random number
# generator. Every (x,y)-coordinate is either a
# wall or an open space. You can't move
# diagonally. The cube maze starts at 0,0 and
# seems to extend infinitely toward positive x and
# y; negative values are invalid, as they
# represent a location outside the building. You
# are in a small waiting area at 1,1. You can
# determine whether a given x,y coordinate will be
# a wall or an open space using a simple system:
# - Find x*x + 3*x + 2*x*y + y + y*y.
# - Add the office designer's favorite number
#   (your puzzle input).
# - Find the binary representation of that sum;
#   count the number of bits that are 1.
# - If the number of bits that are 1 is even, it's
#   an open space.
# - If the number of bits that are 1 is odd, it's a
#   wall.
#
# What is the fewest number of steps required for
# you to reach 31,39?

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



# Determine if the given x,y-coordinate is open or
# is a wall.
def isOpen(x, y, number):
   # Compute formula.
   result = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + number

   # Convert to binary.
   r_bin = bin(result)

   # Count the number of '1's in the binary
   # representation.
   count = len([ True for i in r_bin[2:] if i == '1' ])

   # If even number of '1's, then open.
   return (count % 2) == 0


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and process.   
   file_input = readFile("input13b.txt")
   input_number = int(file_input[0])

   # Initialize the destination coordinates.
   final_x = 31
   final_y = 39

   # Initialize the starting position.         
   start = (1, 1)

   # Used to calculate neighbors in the four
   # cardinal directions.
   directions = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]

   # Will store the shortest path distance from
   # start to final.
   final_distance = 0

   # Conduct a BFS of the maze.
   to_visit = [ (start, 0) ]
   visited = set()
   found = False
   while not found:
      current, distance = to_visit.pop(0)
      current_x, current_y = current

      # Are the current coordinates equal to the
      # final coordinates; if so, finish.
      if (current_x == final_x) and (current_y == final_y):
         found = True
         final_distance = distance

      # Otherwise, examine the cardinal neighbors
      # of the current coordinates.
      elif current not in visited:
         visited.add(current)

         # For each neighbor...
         for dx, dy in directions:
            next_x = current_x + dx
            next_y = current_y + dy

            # Make sure no negative coordinates.
            if (next_x >= 0) and (next_y >= 0):
               # If not a wall, then add it to the
               # list of locations to visit.
               is_open = isOpen(next_x, next_y, input_number)
               if is_open:
                  to_visit.append(((next_x, next_y), distance+1))

   
   # Display the fewest steps required to reach
   # the final x,y.
   print("Fewest steps required = " + str(distance))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
