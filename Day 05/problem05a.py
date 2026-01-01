# The problem input is part of a seed for an MD5
# hash function used for generating a password.
# The eight-character password is generated one
# character at a time by finding the MD5 hash of
# the puzzle input concatenated with an increasing
# integer index (starting with 0). A hash value
# indicates the next character in the password if
# its hexadecimal representation starts with five
# zeroes. If it does, the sixth character in the
# hash is the next character of the password.
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
   # The sixth digit is appended to the password.
   # Repeat until we have all eight characters of
   # the password.
   password = ''
   p_length = 8
   count = 0
   while len(password) < p_length:
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
         # then a character of the password is
         # found.
         if hex_string[:5] == '00000':
            # Append the sixth character of hash.
            password += hex_string[5]
            # Break out of the inner loop.
            found = True

         # Increment the count and loop.
         count += 1
      
   # Display the results.
   print('Password = ' + password)

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
