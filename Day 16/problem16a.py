# The problem input is an initial state string
# which is used to generate filler data from which
# a checksum is calculated. Starting with the
# initial state, so long as you don't have enough
# data yet to fill the disk, the following steps
# are repeated:
# - Call the data you have at this point "a".
# - Make a copy of "a"; call this copy "b".
# - Reverse the order of the characters in "b".
# - In "b", replace all instances of 0 with 1 and
#   all 1s with 0.
# - The resulting data is "a", then a single 0,
#   then "b".
# Repeat these steps until you have enough data to
# fill the desired disk. Once the data has been
# generated, you also need to create a checksum of
# that data. Calculate the checksum only for the
# data that fits on the disk, even if a larger
# amount of data was generated. The checksum for
# some given data is created by considering each
# non-overlapping pair of characters in the input
# data. If the two characters match (00 or 11),
# the next checksum character is a 1. If the
# characters do not match (01 or 10), the next
# checksum character is a 0. This should produce
# a new string which is exactly half as long as
# the original. If the length of the checksum is
# even, repeat the process until you end up with
# a checksum with an odd length.
#
# The first disk you have to fill has length 272.
# Using the initial state in your puzzle input,
# what is the correct checksum?

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


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file for the starting string.
   data_string = readFile("input16b.txt")[0]

   # The amount of disk space to fill.
   fill_space = 272

   # Repeat steps until space is filled.
   while len(data_string) < fill_space:
      data_copy = ''
      # For each character is the original string,
      # invert the bit in the copy.
      for c in data_string:
         if c == '1':
            data_copy += '0'
         else:
            data_copy += '1'

      # Then, reverse the bit order in the copy.
      data_copy = data_copy[::-1]

      # Append a '0' and the data copy to the
      # original date.
      data_string = data_string + '0' + data_copy

   # After space is filled, trucate any excess.
   data_string = data_string[:fill_space]

   # Calculate the checksum of the data.
   checksum = ''

   # For each (non-overlapping) pair of bits, if
   # they are the same, the checksum bit is '1';
   # '0' otherwise.
   for i in range(0, len(data_string) - 1, 2):
      if (data_string[i] == data_string[i+1]):
         checksum += '1'
      else:
         checksum += '0'

   # Using the checksum, repeatedly generate a new
   # checksum until the checksum is of odd length.
   while (len(checksum) % 2) == 0:
      next_checksum = ''
      for i in range(0, len(checksum) - 1, 2):
         if (checksum[i] == checksum[i+1]):
            next_checksum += '1'
         else:
            next_checksum += '0'

      checksum = next_checksum
     
   # Display the resulting checksum.
   print('Checksum = ' + checksum)

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
