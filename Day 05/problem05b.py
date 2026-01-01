# The problem input is part of a seed for an MD5
# hash function used for generating a password.
# The eight-character password is generated one
# character at a time by finding the MD5 hash of
# the puzzle input concatenated with an increasing
# integer index (starting with 0). Instead of
# simply filling in the password from left to
# right, the hash now also indicates the position
# within the password to fill. You still look for
# hashes that begin with five zeroes; however,
# now, the sixth character represents the position
# (0-7), and the seventh character is the
# character to put in that position. A hash result
# of 000001f means that f is the second character
# in the password. Use only the first result for
# each position, and ignore invalid positions.
#
# Given the file input, what is the password?

import time     # For timing the execution
import hashlib  # For calculating the hash value

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
   
   return lines[0]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   seed = readFile("input5b.txt")

   # Maintain a decimal count. Append this value,
   # as a string, to the seed value (also as a
   # string). Calculate the MD5 hash and check it.
   # Repeat until we have all eight characters of
   # the password.
   p_length = 8
   password = [ '' for i in range(p_length) ]
   p_found = 0
   count = 0
   while p_found < p_length:
      # Iterate until a hash value in the correct
      # form is found.
      found = False
      while not found:
         # Form the string to hash.
         hex_count = str(count)
         byte_data = (seed + hex_count).encode('utf-8')

         # Hash the string.
         md5 = hashlib.md5()
         md5.update(byte_data)
         hex_string = md5.hexdigest()

         # If the hash starts with five zeros,
         # then a character of the password 
         # may be found.
         if hex_string[:5] == '00000':
            # Convert the 6th character to integer.
            loc = int(hex_string[5], 16)

            # If it is a valid index and that spot
            # is empty, then add the 7th character
            # to that spot.
            if (loc < len(password)) and (password[loc] == ''):
               password[loc] = hex_string[6]
               # Increment the number of spots
               # found.
               p_found += 1
               
               # Break out of the inner loop.
               found = True

         # Increment the count and loop.
         count += 1
      
   # Display the results.
   print('Password = ' + ''.join(password))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
