# The problem input is a salt for an MD5 hash
# serving as a passcode. You're trying to access a
# secure vault protected by a 4x4 grid of small
# rooms connected by doors. You start in the top-
# left room (0, 0), and you can access the vault
# (3, 3) once you reach the bottom-right room:
#
#      #########
#      #S| | | #
#      #-#-#-#-#
#      # | | | #
#      #-#-#-#-#
#      # | | | #
#      #-#-#-#-#
#      # | | |  
#      ####### V
#
# Fixed walls are marked with #, and doors are
# marked with - or |. The doors in your current
# room are either open or closed (and locked)
# based on the hexadecimal MD5 hash of a passcode
# (your puzzle input) followed by a sequence of
# uppercase characters representing the path you
# have taken so far (U for up, D for down, L for
# left, and R for right). Only the first four
# characters of the hash are used; they represent,
# respectively, the doors up, down, left, and
# right from your current position. Any b, c, d,
# e, or f means that the corresponding door is
# open; any other character (any number or a)
# means that the corresponding door is closed and
# locked. To access the vault, you need to reach
# the bottom-right room.
#
# Given your vault's passcode, what is the
# shortest path (the actual path, not just the
# length) to reach the vault?

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
   
   return lines


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file for the hash salt.
   passcode = readFile("input17b.txt")[0]

   # Specify the starting and ending coordinates.
   start = (0, 0)
   vault = (3, 3)

   # Keep the original length to extract the path
   # from the final passcode.
   original_length = len(passcode)

   # Specify hash digit values denoting open doors.
   open_values = { 'b', 'c', 'd', 'e', 'f' }

   # Perform a BFS until the vault is reached. No
   # visited cache is used because backtracking
   # may be needed.
   to_visit = [ (start, passcode) ]
   path = ''
   done = False
   while not done:
      # Pop the current location and passcode.
      current, passcode = to_visit.pop(0)
      current_x, current_y = current

      # If the current location is the vault, then
      # extract the path and done checking.
      if current == vault:
         done = True
         path = passcode[original_length:]

      # Otherwise, hash the passcode and check the
      # directions.
      else:
         # Hash the passcode.
         byte_data = passcode.encode('utf-8')
         md5 = hashlib.md5()
         md5.update(byte_data)
         hex_string = md5.hexdigest()

         # The first four characters of the hash
         # determine open doors.
         up, down, left, right = hex_string[:4]

         # For each direction, make sure its not a
         # wall and it's open. If so, update the
         # location and passcode and add to the
         # to_visit list.
         if (up in open_values) and ((current_y - 1) >= 0):
            to_visit.append(((current_x, current_y - 1), passcode + 'U'))
            
         if (down in open_values) and ((current_y + 1) < 4):
            to_visit.append(((current_x, current_y + 1), passcode + 'D'))
            
         if (left in open_values) and ((current_x - 1) >= 0):
            to_visit.append(((current_x - 1, current_y), passcode + 'L'))
            
         if (right in open_values) and ((current_x + 1) < 4):
            to_visit.append(((current_x + 1, current_y), passcode + 'R'))
     
   # Display the shortest path to the vault.
   print('Path to vault = ' + path)

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
