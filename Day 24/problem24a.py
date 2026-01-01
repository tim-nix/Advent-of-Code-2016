# The problem input is a maze (map) that a robot
# needs to traverse. The starting location is
# marked as '0'. The other numbers are (in no
# particular order) the locations the robot needs
# to visit at least once each. Walls are marked as
# '#', and open passages are marked as '.'.
# Numbers behave like open passages.
#
# Given your actual map, and starting from
# location 0, what is the fewest number of steps
# required to visit every non-0 number marked on
# the map at least once?

import time          # For timing the execution
import itertools     # For permutations
import math          # For math.inf

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

   # Read the input file and process.   
   maze = readFile("input24b.txt")

   # Define the max dimensions of the maze.
   max_x = len(maze[0])
   max_y = len(maze)
   
   numbers = dict()
   for y in range(max_y):
      for x in range(max_x):
         if maze[y][x].isdigit():
            numbers[(x, y)] = maze[y][x]

   # Used to calculate neighbors in the four
   # cardinal directions.
   directions = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]

   # From each numbered location, use BFS to find
   # the shortest path to all other numbered
   # locations.
   shortest_paths = dict()
   for key in numbers:
      # Reset the BFS each time.
      start = key
      to_visit = [ (start, 0) ]
      visited = set()
      found = set()
      found.add(numbers[key])
      while len(found) < len(numbers):
         current, distance = to_visit.pop(0)
         current_x, current_y = current

         # If a numbered location is found (for
         # the first time), add it to 'found' and
         # to the dictionary of shortest paths.
         if (current in numbers) and (numbers[current] not in found):
            found.add(numbers[current])
            shortest_paths[(numbers[start], numbers[current])] = distance

         # For each neighbor...
         for dx, dy in directions:
            next_x = current_x + dx
            next_y = current_y + dy

            # Make sure not visited.
            if (next_x, next_y) not in visited:
               # Make sure no negative coordinates.
               if (next_x >= 0) and (next_x < max_x):
                  if (next_y >= 0) and (next_y < max_y):
                     # If not a wall, then add it to the
                     # list of locations to visit.
                     if maze[next_y][next_x] != '#':
                        to_visit.append(((next_x, next_y), distance+1))
                        visited.add((next_x, next_y))

   # Create permutations of all numbered locations
   # except for '0'.
   nums = sorted([ numbers[key] for key in numbers ])
   combos = itertools.permutations(nums[1:])

   # For each permutation, follow the path,
   # starting at '0' and calculate the sum
   # of the shortest path between legs.
   min_path = math.inf
   for c in combos:
      current = '0'
      path = 0
      for next_num in c:
         path += shortest_paths[(current, next_num)]
         current = next_num

      # If this path is the shortest seen, then
      # set it to min_path.
      if path < min_path:
         min_path = path


   # Display the length of the shortest path.
   print("Shortest path = " + str(min_path))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
