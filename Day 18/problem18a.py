# The problem input is a string representing a row
# of floor tiles and whether or not each tile is
# safe or trapped. The traps and safe tiles in
# this room seem to follow a pattern. The tiles
# are arranged into rows that are all the same
# width; you take note of the safe tiles (.) and
# traps (^) in the first row (your puzzle input).
# The type of tile (trapped or safe) in each row
# is based on the types of the tiles in the same
# position, and to either side of that position,
# in the previous row. If either side is off 
# either end of the row, it counts as "safe"
# because there isn't a trap embedded in the wall.
# wall. A new tile is a trap only in one of the
# following situations:
# - Its left and center tiles are traps, but its
#   right tile is not.
# - Its center and right tiles are traps, but its
#   left tile is not.
# - Only its left tile is a trap.
# - Only its right tile is a trap.
#
# In a total of 40 rows (including the starting
# row), how many safe tiles are there?

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


# Count the number of 'safe tiles' withiin the
# row; that is, the number of tiles with the value
# of '.'.
def countSafe(row):
   count = 0
   # Iterate through each tile
   for tile in row:
      # If it is safe, increment count.
      if tile == '.':
         count += 1

   # Return the count.
   return count


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   start_row = list(readFile("input18b.txt")[0])

   # Initialize the count of safe tiles to the
   # number of safe tiles in the starting row.
   safe_count = countSafe(start_row)

   # The number of rows to look at is 40.
   max_rows = 40

   # Already looked at row 0, so start on row 1.
   # Loop until all rows generated and examined.
   row_count = 1
   while row_count < max_rows:
      # Create a new but empty row.
      next_row = [ '.' for x in range(len(start_row)) ]

      # Iterate through each tile location.
      for i in range(len(start_row)):
         # Determine if traps on the row above.
         left = center = right = False
         
         if (i - 1 >= 0) and (start_row[i-1] == '^'):
            left = True

         if (start_row[i] == '^'):
            center = True

         if (i + 1 < len(start_row)) and (start_row[i+1] == '^'):
            right = True

         # Assign trap based on traps above.
         if left and center and not right:
            next_row[i] = '^'

         elif not left and center and right:
            next_row[i] = '^'

         elif left and not center and not right:
            next_row[i] = '^'

         elif not left and not center and right:
            next_row[i] = '^'

      start_row = next_row

      # Count the safe tiles and add to count.
      safe_count += countSafe(start_row)
      # Increment row count
      row_count += 1
   
   # Display the resulting count for safe tiles.
   print('Number of safe tiles = ' + str(safe_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
