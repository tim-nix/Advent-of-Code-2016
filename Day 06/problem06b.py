# The problem input is a list of strings. Each
# string is the same message sent repeatedly, but
# the data seems quite corrupted - almost too
# badly to recover. Almost. All you need to do is
# figure out which character is LEAST frequent
# for each position; that is, the character least
# frequent within each column.
#
# What is the error-corrected version of the
# message being sent?

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


# Convert each line of text into a list of
# characters corresponding to each column.
def parseInput(values):
   columns = list()
   # Iterate through each character in the message.
   for c in range(len(values[0])):
      # Build a list of all characters in that
      # position from each line of input.
      col = list()
      for line in values:
         col.append(line[c])

      # Append the list of column characters.
      columns.append(col)

   # Return the list for all columns.
   return columns

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input6b.txt")
   columns = parseInput(file_input)

   # Iterate through each column of letters.
   message = ''
   for c in columns:
      # Find the least occurring character from
      # the list and append it to the message.
      message += min(set(c), key=c.count)
      
   # Display the results.
   print('Message = ' + message)

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
