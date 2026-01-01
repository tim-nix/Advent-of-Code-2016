# The problem input consists of a list of three
# integer values corresponding to the lengths of
# three sides of a triangle. In a valid triangle,
# the sum of any two sides must be larger than
# the remaining side. For example, the "triangle"
# 5 10 25 is impossible, because 5 + 10 is not
# larger than 25. However, triangles are specified
# in groups of three vertically. Each set of three
# numbers in a column specifies a triangle. Rows
# are unrelated.
#
# In your puzzle input, and instead reading by
# columns, how many of the listed triangles are
# possible?

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


# Each line of file input corresponds to a string
# containing three numbers. Remove the commas,
# split the string into the three numbers and
# convert them to integers, storing them in a
# tuple. Then, read the integers by column, three
# at a time, and store them in a tuple. Do that
# for all three columns
def parseInput(values):
   # First break each string into a tuple of three
   # integers and store in a list.
   triangles1 = list()
   for line in values:
      line = line.replace(',', '')
      lengths = [ int(i) for i in line.split() ]
      triangles1.append(tuple(lengths))

   # Then, read numbers within the same column,
   # three at a time, and store in a list.
   triangles2 = list()
   for t in range(0, len(triangles1), 3):
      for i in range(3):
         triangles2.append((triangles1[t][i], triangles1[t+1][i], triangles1[t+2][i]))

   # Return the list of potential triangles.
   return triangles2


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   fileInput = readFile("input3b.txt")
   triangles = parseInput(fileInput)
   
   # Count the number of good triangles.
   good_triangles = 0
   for t in triangles:
      # Sum of any two sides should be longer the
      # third.
      if (t[0] + t[1] > t[2]) and (t[1] + t[2] > t[0]) and (t[0] + t[2] > t[1]):
         good_triangles += 1

   # Display the results
   print("Good triangles = " + str(good_triangles))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
