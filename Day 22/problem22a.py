# The problem input is the results from calling
# the df command; that is, the disk usage of all
# nodes. Nodes are named by their position, such
# as the node named node-x10-y10. We need to count
# the number of viable pairs of nodes. A viable
# pair is any two nodes (A,B), regardless of
# whether they are directly connected, such that:
# - Node A is not empty (its Used is not zero).
# - Nodes A and B are not the same node.
# - The data on node A (its Used) would fit on
#   node B (its Avail).
#
# How many viable pairs of nodes are there?

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
# coordinates, the amount of used space, and the
# amount of available space. Convert each value to
# integer and store in a list as a tuple in the
# following format: ((x, y), used, avail).
def parseInput(values):
   df = list()
   # Iterate through disk data, ignoring headers.
   for line in values[2:]:
      parts = line.split()
      
      # Extract x and y.
      x_str, y_str = parts[0][15:].split('-')
      coords = (int(x_str[1:]), int(y_str[1:]))

      # Extract used.
      used = int(parts[2][:-1])

      # Extract available.
      avail = int(parts[3][:-1])

      # Add to df information.
      df.append((coords, used, avail))

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

   # Iterate through every pair of nodes; include
   # both (A, B) and (B, A).
   count = 0
   for i in range(len(df)):
      for j in range(len(df)):
         # Node A is not empty and Nodes A and B
         # are not the same node.
         if (df[i][0] != df[j][0]) and (df[i][1] != 0):
            # Data on node A would fit on node B.
            if df[i][1] <= df[j][2]:
               # Then they are viable, so
               # increment the count.
               count += 1

   # Display the number of viable pairs.
   print('Viable pairs = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
