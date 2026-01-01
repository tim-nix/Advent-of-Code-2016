# The problem input is a 'compressed' file using a
# new compression format. The format compresses a
# sequence of characters. Whitespace is ignored. 
# To indicate that some sequence should be
# repeated, a marker is added to the file, like
# (10x2). To decompress this marker, take the
# subsequent 10 characters and repeat them 2
# times. Then, continue reading the file after the
# repeated data. The marker itself is not included
# in the decompressed output. If parentheses or
# other characters appear within the data
# referenced by a marker, that's okay - treat it
# like normal data, not a marker, and then resume
# looking for markers after the decompressed
# section.
#
# What is the decompressed length of the file?

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

   # Read the input file.   
   file_input = readFile("input9b.txt")[0]

   # Iterate through the characters of the file.
   index = 0
   char_count = 0
   while index < len(file_input):
      # If an opening parenthesis is encountered,
      # then handle the marker.
      if file_input[index] == '(':
         
         # Find the end of the marker.
         end_index = index
         while file_input[end_index] != ')':
            end_index += 1
            
         # Extract the string length (low) and the
         # number of repeats (high).
         low, high = file_input[index+1:end_index].split('x')

         # Update index and character count.
         index = end_index + 1 + int(low)
         char_count += (int(low) * int(high))

      # Otherwise, handle the lone character.
      else:
         index += 1
         char_count += 1
         

   # Display the resulting decompression length.
   print('Decompressed length = ' + str(char_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
