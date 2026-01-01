# The problem input is a list of IPv7 addresses.
# We need to figure out which IPs support TLS
# (transport-layer snooping). An IP supports TLS
# if it has an ABBA. An ABBA is any four-character
# sequence which consists of a pair of two
# different characters followed by the reverse of
# that pair, such as xyyx or abba. However, the IP
# also must not have an ABBA within any hypernet
# sequences, which are contained by square
# brackets.
#
# How many IPs in your puzzle input support TLS?

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


# Given the file input, split the contents of each
# line into the strings outside of braces and the
# strings inside the braces.
def parseInput(values):
   ips = list()
   for line in values:
      # Modify the list for a single delimiter.
      line = line.replace(']', '[')
      parts = line.split('[')

      # Assume the first string will be outside
      # and then alternate. Thus, outside strings
      # will be at even indices and inside strings
      # will be at odd indices.
      outside = [ parts[i] for i in range(0, len(parts), 2) ]
      inside  = [ parts[i] for i in range(1, len(parts), 2) ]

      # Store inside and outside as a tuple within
      # the overall list.
      ips.append((tuple(outside), tuple(inside)))

   # Return the list of IPs.
   return ips


# For a given string, see if an ABBA string exists
# and return True/False accordingly.
def containsABBA(seq):
   # An ABBA is four characters long, so leave
   # room for last check.
   for i in range(len(seq) - 3):
      # The sequence should not be four of the
      # same letters.
      if seq[i] != seq[i+1]:
         # First character must match the last and
         # the second must match the third.
         if (seq[i] == seq[i+3]) and (seq[i+1] == seq[i+2]):
            return True

   # Otherwise, no ABBA was found.
   return False

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input7b.txt")
   ips = parseInput(file_input)

   # Iterate through each IP address data.
   count = 0
   for outer, inner in ips:
      # At least one outer string should contain
      # an ABBA.
      found_outer = False
      for o in outer:
         if containsABBA(o):
            found_outer = True

      # No inner string should contain and ABBA.
      found_inner = False
      for i in inner:
         if containsABBA(i):
            found_inner = True

      # If outer ABBA was found and no inner ABBA
      # was found, then increment count.
      if found_outer and not found_inner:
         count += 1

   # Display the resulting count.
   print('Number of IPs that support TLS = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
