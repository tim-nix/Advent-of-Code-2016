# The problem input specifies the number of elves
# participating in the White Elephant party. Each
# Elf brings a present. They all sit in a circle,
# numbered starting with position 1. Then,
# starting with the first Elf, they take turns
# stealing all the presents from the Elf directly
# across the circle. If two Elves are across the
# circle, the one on the left (from the
# perspective of the stealer) is stolen from. The
# other rules remain unchanged: Elves with no
# presents are removed from the circle entirely,
# and the other elves move in slightly to keep the
# circle evenly spaced.
#
# With the number of Elves given in your puzzle
# input, which Elf gets all the presents?

import time     # For timing the execution
from collections import deque

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

   # Start with all elves.
   elves_list = [ i for i in range(1, num_elves + 1) ]

   # Removing from the front of a list is very
   # inefficient. Using dequeue is efficient for
   # front and back operations but not for middle.
   # Thus, we split the circle of elves into two
   # with the first group being slightly larger
   # (by one more).

   elves1 = deque(elves_list[:len(elves_list) // 2])
   elves2 = deque(elves_list[len(elves_list) // 2:])

   while len(elves1) <= len(elves2):
      spare = elves2.popleft()
      elves1.append(spare)

   # While more than one elf remains...
   while len(elves1) > 1:
      # Remove the middle elf (back of elves1).
      elves1.pop()

      # Move the first elf to the back of elves2.
      spare = elves1.popleft()
      elves2.append(spare)

      # Again, make elves1 slightly larger.
      while len(elves1) <= len(elves2):
         spare = elves2.popleft()
         elves1.append(spare)
   
   # Display the elf that ends up with all presents.
   print('The lone elf = ' + str(elves1[0]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
