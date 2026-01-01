# The problem input is the results from calling
# the df command; that is, the disk usage of all
# nodes. Nodes are named by their position, such
# as the node named node-x10-y10. The goal is to
# gain access to the data which begins in the node
# with y=0 and the highest x (that is, the node in
# the top-right corner). To do this, we need to
# move data around. First, we find the empty node.
# Next, we swap adjacent data with the empty node
# and move the empty node next to the goal data.
# We also need to avoid nodes that contain too
# much data to move (will not fit). Once the empty
# node is adjacent to the goal node, we can begin
# to move to goal data to (0, 0).
#
# What is the fewest number of steps required to
# move your goal data to node-x0-y0?

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


# For each line of file input, extract the
# coordinates, the size of the node, and the
# amount of used space. Convert each value to
# integer and store in a list as a tuple in the
# following format: ((x, y), size, used).
def parseInput(values):
   df = list()
   # Iterate through disk data, ignoring headers.
   for line in values[2:]:
      parts = line.split()
      
      # Extract x and y.
      x_str, y_str = parts[0][15:].split('-')
      coords = (int(x_str[1:]), int(y_str[1:]))

      # Extract size.
      size = int(parts[1][:-1])

      # Extract used.
      used = int(parts[2][:-1])

      # Add to df information.
      df.append((coords, size, used))

   # Return df information.
   return df
      


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of tuples, each denoting a range of blocked
   # IP addresses.
   file_input = readFile("input22b.txt")
   df = parseInput(file_input)

   # Build the layout as a map.
   
   # Find max_x and max_y.
   max_x = max( [d[0][0] for d in df ] ) + 1
   max_y = max( [d[0][1] for d in df ] ) + 1

   # Empty grid
   grid = [ [ '.' for x in range(max_x) ] for y in range(max_y) ]

   # Find and mark the location of the empty node.
   empty_size = 0
   start = (0, 0)
   for node in df:
      if node[2] == 0:
         grid[node[0][1]][node[0][0]] = '_'
         empty_size = node[1]
         start = node[0]

   # Find and mark the locations of walls.
   for node in df:
      if node[2] > empty_size:
         grid[node[0][1]][node[0][0]] = '#'

   # Mark the goal data and where it is moved to.
   grid[0][max_x - 1] = 'G'
   grid[0][0] = 'O'

   # Use BFS to find the shortest distance from
   # '_' to the location to the left of 'G',
   # avoiding any wall.

   # Used to calculate neighbors in the four
   # cardinal directions.
   directions = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]

   to_visit = [ (start, 0) ]
   stop = (max_x - 2, 0)
   visited = set()
   total_steps = 0
   found = False
   while not found:
      current, distance = to_visit.pop(0)
      current_x, current_y = current

      # Are the current coordinates equal to the
      # final coordinates; if so, assign to
      # total_steps and done.
      if current == stop:
         found = True
         total_steps = distance

      # Otherwise, examine the cardinal neighbors
      # of the current coordinates.
      else:
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
                     if grid[next_y][next_x] != '#':
                        to_visit.append(((next_x, next_y), distance+1))
                        visited.add((next_x, next_y))

   # Next, move '_' right one (moves 'G' left
   # one), then move '_' down one, left two, and
   # up one (total of five). Repeat this to get
   # '_' to (0, 0) with 'G' to its right.
   total_steps +=  5 * (max_x - 2)

   # Then, one more move of '_' to the right,
   # moving 'G' to its destination (0,0).
   total_steps += 1

   # Display the total number of steps needed to
   # move the data.
   print("Fewest steps required = " + str(total_steps))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
