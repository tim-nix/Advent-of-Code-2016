# The problem input is a 'compressed' file using a
# new compression format. The format compresses a
# sequence of characters. Whitespace is ignored. 
# To indicate that some sequence should be
# repeated, a marker is added to the file, like
# (10x2). To decompress this marker, take the
# subsequent 10 characters and repeat them 2
# times. Then, continue reading the file after the
# repeated data. The marker itself is not included
# in the decompressed output. If markers appear
# within the data referenced by a marker, the
# markers within decompressed data are also
# decompressed.
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


# Use recursion to handle nested markers. Assume
# that nested markers will follow immediatly from
# prior markers. The recursion just handles the
# string segment specified by the marker and the
# marker itself.
def recursiveDecompress(index, end_index, file_input):
   char_count = 0

   # Iterate over the string segment.
   while index < end_index:
      
      # If an opening parenthesis is encountered,
      # then handle the marker.
      if file_input[index] == '(':
         
         # Find the end of the marker.
         end_marker = index
         while file_input[end_marker] != ')':
            end_marker += 1

         # Extract and convert the string length
         # and the number of repeats.
         low, high = file_input[index+1:end_marker].split('x')
         length = int(low)
         repeats = int(high)

         # Need to recurse if another marker
         # follows this one.
         index = end_marker + 1

         # Handle the nested marker recursively,
         # if present.
         if file_input[index] == '(':
            char_count += repeats * recursiveDecompress(index, index + length, file_input)

         # Otherwise, just update the count.
         else:
            char_count += (length * repeats)

         # Update the index to the end of the
         # sequence.
         index += length

      # Otherwise, handle the lone character.
      else:
         index += 1
         char_count += 1

   # Return the character count for the segment.
   return char_count



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input9b.txt")[0]

   # Calculate the decompressed length.
   char_count = recursiveDecompress(0, len(file_input), file_input)

   # Display the resulting decompression length.
   print('Decompressed length = ' + str(char_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
