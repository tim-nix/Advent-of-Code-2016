# The problem input specifies the number of elves
# participating in the White Elephant party. Each
# Elf brings a present. They all sit in a circle,
# numbered starting with position 1. Then,
# starting with the first Elf, they take turns
# stealing all the presents from the Elf to their
# left. An Elf with no presents is removed from
# the circle and does not take turns.
#
# With the number of Elves given in your puzzle
# input, which Elf gets all the presents?

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
   file_input = readFile("input19b.txt")[0]
   num_elves = int(file_input)

   # In the first round, start with elf 1 and only
   # include every other elf (odd numbered elves).
   elves = [ i for i in range(1, num_elves + 1, 2) ]

   # For the next round, set the index to start at
   # the first element if the last elf in the
   # previous round survives the cut.
   if num_elves in elves:
      index = 1
   else:
      index = 0

   # While more than one elf remains...
   while len(elves) > 1:
      # Choose every other elf for the next round.
      next_elves = [ elves[i] for i in range(index, len(elves), 2) ]

      # For the next round, set the index to start at
      # the first element if the last elf in the
      # previous round survives the cut.
      if elves[-1] in next_elves:
         index = 1
      else:
         index = 0

      # Update the list of elves.
      elves = next_elves
   
   # Display the elf that ends up with all presents.
   print('The lone elf = ' + str(elves[0]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
