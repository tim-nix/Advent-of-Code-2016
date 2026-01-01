# The problem input is a list of IPv7 addresses.
# We need to figure out which IPs support SSL. An
# IP supports SSL if it has an ABA anywhere in the
# supernet sequences (outside any square bracketed
# sections), and a corresponding Byte Allocation
# Block, or BAB, anywhere in the hypernet
# sequences. An ABA is any three-character
# sequence which consists of the same character
# twice with a different character between them,
# such as xyx or aba. A corresponding BAB is the
# same characters but in reversed positions: yxy
# and bab, respectively.
#
# How many IPs in your puzzle input support SSL?

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


# Generate a list of possible BAB values from the
# given string, seq.
def findBABs(seq):
   # A string could contain multiple potential
   # BABs, so process entire string and store all.
   babs = list()
   
   # An BAB is three characters long, so leave
   # room for last check.
   for i in range(len(seq) - 2):
      # The sequence should not be three of the
      # same letters.
      if seq[i] != seq[i+1]:
         # First character must match the third.
         if (seq[i] == seq[i+2]):
            babs.append(seq[i:i+3])

   # Return the list of potential BABs.
   return babs

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input7b.txt")
   ips = parseInput(file_input)

   # Iterate through each IP address data.
   count = 0
   for outer, inner in ips:
      # Find all possible BABs from the outer
      # strings.
      p_babs1 = list()
      for o in outer:
         p_babs1 += findBABs(o)

      # Find all possible BABs from the inner
      # strings and convert to a set.
      p_babs2 = list()
      for i in inner:
         p_babs2 += findBABs(i)
      babs_set = set(p_babs2)

      # For each potential BAB from the outer
      # string, generate its corresponding BAB and
      # see if that string is in the possible BABs
      # in the set of potential inner BABs.
      for b in p_babs1:
         test = b[1] + b[0] + b[1]
         
         # If so, then increment count and no need
         # to continue with given IP address.
         if test in babs_set:
            count += 1
            break
      

   # Display the resulting count.
   print('Number of IPs that support TLS = ' + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
