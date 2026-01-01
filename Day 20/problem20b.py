# The problem input consists of a list of blocked
# IP addresses. The list seems to be messy and
# poorly maintained, and it's not clear which IPs
# are allowed. Also, rather than being written in
# dot-decimal notation, they are written as plain
# 32-bit integers, which can have any value from 0
# through 4294967295, inclusive.
#
# Given the list of blocked IPs retrieved from the
# firewall, how many IPs are allowed by the
# blacklist? 

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


# Convert the list of ranges (as string) into a
# list of tuples with the range (inclusive) of IP
# addresses blocked.
def parseInput(values):
   ranges = list()
   for line in values:
      parts = line.split('-')
      ranges.append((int(parts[0]), int(parts[1])))

   return sorted(ranges)

# Detects if range2 and range2 overlap or if they
# are adjacent. In either case, 'True' is 
# returned. Otherwise, 'False' is returned.
def rangesOverlap(range1, range2):
    overlap = max(range1[0], range2[0]) <= min(range1[1], range2[1])
    adjacent = (range1[1] + 1 == range2[0]) or (range2[1] + 1 == range1[0])

    return overlap or adjacent

# Detects if range2 is completely within range1.
def rangeContained(range1, range2):
   return (range1[0] <= range2[0]) and (range1[1] >= range2[1])

if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of tuples, each denoting a range of blocked
   # IP addresses.
   file_input = readFile("input20b.txt")
   ranges = parseInput(file_input)

   # While ranges can be consolidated, continue to
   # consolidate. Overlapped and adjacent ranges
   # are combined (replacing the originals). 
   done = False
   while not done:
      done = True
      next_ranges = list()
      # Iterate through each range...
      for i in range(len(ranges)):
         combined = False
         skip_set = set()
         # ...and combine it with any overlapping
         # or adjacent range.
         for j in range(len(ranges)):
            # Ranges already combined are skipped.
            if ranges[j] not in skip_set:
               # If the second range is contained
               # within the first, then skip it.
               if rangeContained(ranges[i], ranges[j]):
                  skip_set.add(ranges[j])
                  continue

               # If ranges overlap or are adjacent,
               # then combine them.
               if rangesOverlap(ranges[i], ranges[j]):
                  done = False
                  combined = True
                  low = min(ranges[i][0], ranges[j][0])
                  high = max(ranges[i][1], ranges[j][1])
                  next_ranges.append((low, high))

                  # Mark the second range for skip.
                  skip_set.add(ranges[j])

         # If the first range was not combined
         # with anything, add it.
         if not combined:
            next_ranges.append(ranges[i])

      # Set up for another round.
      ranges = sorted(list(set(next_ranges)))

   # Find number of allowed IP addresses.
   max_address = 4294967295
   num_addresses = 0
   address = ranges[0][1] + 1
   for i in range(1, len(ranges)):
      num_addresses += (ranges[i][0] - address)
      address = ranges[i][1] + 1

   # Make sure there are no addresses above the
   # highest blocked address.
   if address < max_address:
      num_addresses += (max_address - address)

   # Display the number of IP address that are not
   # blocked by the black list.
   print('Number of good IP addresses = ' + str(num_addresses))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

   # 100 is too low
        
