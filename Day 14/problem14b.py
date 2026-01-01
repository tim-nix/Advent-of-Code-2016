# The problem input is a salt for hashing. Hashing
# is used to generate keys. To generate keys, you
# first get a stream of random data by taking the
# MD5 of a pre-arranged salt (your puzzle input)
# and an increasing integer index (starting with
# 0, and represented in decimal); the resulting
# MD5 hash should be represented as a string of
# lowercase hexadecimal digits. However, not all
# of these MD5 hashes are keys, and you need 64
# new keys for your one-time pad. A hash is a key
# only if:
# - It contains three of the same character in a
#   row, like 777. Only consider the first such
#   triplet in a hash.
# - One of the next 1000 hashes in the stream
#   contains that same character five times in a
#   row, like 77777.
# This problem also uses key stretching. To
# implement key stretching, whenever you generate
# a hash, before you use it, you first find the
# MD5 hash of that hash, then the MD5 hash of that
# hash, and so on, a total of 2016 additional
# hashings. Always use lowercase hexadecimal
# representations of hashes.
#
# Given the actual salt in your puzzle input and
# using 2016 extra MD5 calls of key stretching,
# what index now produces your 64th one-time pad
# key?

import time      # For timing the execution.
import hashlib   # For calculating the hash value.

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

   # Read the input file and the salt is the lone
   # element within the list.   
   file_input = readFile("input14b.txt")
   salt = file_input[0]

   # Initialize the parameter that sets the number
   # of times each hash is performed.
   key_stretch = 2016

   hash_list = list()
   # Generate the first 1001 hashes. Thus, we have
   # hash data for the current count and the next
   # 1000 hashes.
   for index in range(1001):
      # Form the string to hash.
      hex_count = str(index)
      byte_data = (salt + hex_count).encode('utf-8')

      # Hash the string.
      md5 = hashlib.md5()
      md5.update(byte_data)
      hex_string = md5.hexdigest()
      byte_data = hex_string.encode('utf-8')

      # Repeatedly hash the hash.
      for i in range(key_stretch):
         md5 = hashlib.md5()
         md5.update(byte_data)
         hex_string = md5.hexdigest()
         byte_data = hex_string.encode('utf-8')   

      # Create list at location.
      hash_list.append(list())

      # Find first 3-character sequence and, if
      # found, add it to list.
      seq_found = False
      for i in range(len(hex_string) - 2):
         if hex_string[i] == hex_string[i+1] == hex_string[i+2]:
            seq_found = True
            seq_str = 3 * hex_string[i]
            hash_list[index].append(seq_str)
            break

      # Find all 5-character sequences.
      if seq_found:
         seq_found = False
         for i in range(len(hex_string) - 4):
            seq_found = False
            if hex_string[i] == hex_string[i+1] == hex_string[i+2] == hex_string[i+3] == hex_string[i+4]:
               seq_found = True
               seq_str = 5 * hex_string[i]
               hash_list[index].append(seq_str)
   
   # With this precomputed list of data from the
   # hash values, start identifying keys. The
   # hash_list will serve as a circular buffer.
   needed_keys = 64
   key_indices = list()
   count = 0
   
   # Keep looking for keys until the list of key
   # indices contains the number of needed keys.
   while len(key_indices) < needed_keys:
      # Calculate the current index.
      index = count % len(hash_list)
      
      # Check for 3-character sequence.
      seq_found = False
      if len(hash_list[index]) > 0:
         seq = hash_list[index][0]
         seq_found = True

      # If found, check list for 5-character
      # sequence.
      if seq_found:
         seq_str = 5 * hash_list[index][0][0]
         for i in range(len(hash_list)):
            if (i != index) and (seq_str in hash_list[i]):
               key_indices.append(count)
               break

      # Use the current counter value plus the
      # length of the list to replace data at the
      # current index with new hash data on the
      # hash for the 1000th hash past the next
      # count (count+1).
      
      # Form the string to hash.
      hex_count = str(count + len(hash_list))
      byte_data = (salt + hex_count).encode('utf-8')

      # Hash the string.
      md5 = hashlib.md5()
      md5.update(byte_data)
      hex_string = md5.hexdigest()
      byte_data = hex_string.encode('utf-8')

      # Repeatedly hash the hash.
      for i in range(key_stretch):
         md5 = hashlib.md5()
         md5.update(byte_data)
         hex_string = md5.hexdigest()
         byte_data = hex_string.encode('utf-8')

      # Create list at location.
      hash_list[index] = list()

      # Find first 3-character sequence and, if
      # found, add it to list.
      seq_found = False
      for i in range(len(hex_string) - 2):
         if hex_string[i] == hex_string[i+1] == hex_string[i+2]:
            seq_found = True
            seq_str = 3 * hex_string[i]
            hash_list[index].append(seq_str)
            break

      # Find all 5-character sequences within the
      # hash and add each to the list.
      if seq_found:
         seq_found = False
         for i in range(len(hex_string) - 4):
            seq_found = False
            if hex_string[i] == hex_string[i+1] == hex_string[i+2] == hex_string[i+3] == hex_string[i+4]:
               seq_found = True
               seq_str = 5 * hex_string[i]
               hash_list[index].append(seq_str)
               
      # Increment the count and loop.
      count += 1

   # Display the index of the last key found.
   print("Index of last key = " + str(key_indices[-1]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
