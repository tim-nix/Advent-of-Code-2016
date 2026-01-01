# The problem input consists of a list of possible
# rooms. The list is encrypted and full of decoy
# data, but the instructions to decode the list
# are barely hidden nearby. Better remove the
# decoy data first. Each room consists of an
# encrypted name (lowercase letters separated by
# dashes) followed by a dash, a sector ID, and a
# checksum in square brackets. A room is real (not
# a decoy) if the checksum is the five most common
# letters in the encrypted name, in order, with
# ties broken by alphabetization. Remove the decoy
# names from the list and decrypt the real names.
# To decrypt a room name, rotate each letter
# forward through the alphabet a number of times
# equal to the room's sector ID. A becomes B, B
# becomes C, Z becomes A, and so on. Dashes become
# spaces.
#
# What is the sector ID of the room where North
# Pole objects are stored?

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


# Break up the line of text into the room name
# (with the dashes removed), the checksum, and the
# sector_IDs (convert to integer).
def parseInput(values):
   rooms = list()
   for line in values:
      # Split on the opening brace to find the
      # start of checksum.
      line = line.split('[')
      checksum = line[1][:-1]

      # In the first part, split on the dashes and
      # the last list item is the sector ID; so
      # convert to integer.
      line = line[0].split('-')
      sector_ID = int(line[-1])

      # Rejoin the first elements (sans dashes)
      # into the room name.
      name = ''.join(line[:-1])

      # Add the elements as a tuple to the list.
      rooms.append((name, checksum, sector_ID))

   # Return the list of room data.
   return rooms


# Given a room name, generate the checksum. Find
# the occurrence count for each letter and rejoin
# the characters with the highest counts in order
# (sorted for ties).
def getChecksum(name):
   # Build a list of character counts for each.
   l_count = list()
   l_found = set()
   for c in name:
      if c not in l_found:
         l_count.append((c, name.count(c)))
         l_found.add(c)

   # Sort in reverse by count (high to low) and
   # then normally for ties (low character to high
   # character).
   sorted_count = sorted(l_count,key=lambda x:(-x[1],x[0]))

   # Rejoin the first five characters in the list.
   checksum = ''.join([ a[0] for a in sorted_count[:5] ])

   # Return the checksum.
   return checksum


# Decrypt the name of the room using the sector ID
# as a Ceasar cipher key.
def decryptRoom(name, sector_ID):
   decrypted = ''
   # Iterate through each character of the name.
   for c in name:
      # Find the integer offset of the character.
      i_c = ord(c) - ord('a')
      # Add the sector ID modulo 26.
      i_c = (i_c + sector_ID) % 26
      # Convert back to a character and add to the
      # decrypted string.
      decrypted += chr(i_c + ord('a'))

   # Return the decrypted string.
   return decrypted


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   fileInput = readFile("input4b.txt")
   rooms = parseInput(fileInput)

   # Iterate through each room.
   good_rooms = list()
   for r in rooms:
      # Get the checksum of the room name.
      checksum = getChecksum(r[0])
      # If it matches, then add the room to the
      # list of good rooms.
      if checksum == r[1]:
         good_rooms.append(r)

   # Now, decrypt each room name and search for
   # ''northpole' (since we removed the dashes, we
   # removed the spaces).
   for r in good_rooms:
      decrypted = decryptRoom(r[0], r[2])
      if 'northpole' in decrypted:
         found_ID = r[2]
   
   # Display the sector ID of the storage room.
   print("Sector ID for the North Pole Storage = " + str(found_ID))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
