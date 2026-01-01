# The problem input describes a set of discs; that
# is, the total number of positions and the
# current position at time=0. Each disc rotates by
# one position every second. A capsule is dropped
# and tries to fall through slots in the set of
# rotating discs to finally go through a little
# hole at the bottom. If any of the slots aren't
# aligned with the capsule as it passes (at
# location 0), the capsule bounces off the disc
# and soars away. The discs are spaced out so that
# after you push the button, one second elapses
# before the first disc is reached, and one second
# elapses as the capsule passes from one disc to
# the one below it. So, if you push the button at
# time=100, then the capsule reaches the top disc
# at time=101, the second disc at time=102, the
# third disc at time=103, and so on. The button
# will only drop a capsule at an integer time - no
# fractional seconds allowed. 
#
# What is the first time you can press the button
# to get a capsule?

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


# Convert each line of file input text into a
# tuple with the first element holding the number
# of positions on the disc and the second being
# the position of the disc at time 0.
def parseInput(values):
   discs = list()
   for line in values:
      line = line.replace('.', '')
      parts = line.split()
      discs.append((int(parts[3]), int(parts[11])))

   return discs


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it to a list
   # of tuples.
   file_input = list(readFile("input15b.txt"))
   discs = parseInput(file_input)

   # Check each time, t, until the capsule passes
   # all the way through.
   drop_time = 99
   done = False
   t = 0
   while not done:
      success = True

      # Check each disc for its position when the
      # capsule reaches it given the drop time and
      # the location of the disc.
      for d in range(len(discs)):
         # Time when the capsule reaches the disc.
         p_time = t + d + 1
         
         # The disc position at that time.
         disc_position = (discs[d][1] + p_time) % discs[d][0]

         # If not at position 0, the capsule does
         # not pass through. So, increment time
         # and try again.
         if disc_position != 0:
            success = False
            t += 1
            break

      # Capsule passed through all discs so stop.
      if success:
         drop_time = t
         done = True
         break
     
   # Display the drop time.
   print('Drop time = ' + str(drop_time))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
