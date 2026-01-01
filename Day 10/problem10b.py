# The problem input consists of a list of
# instructions for bots on a factory floor. Each
# bot only proceeds when it has two microchips,
# and once it does, it gives each one to a
# different bot or puts it in a marked "output"
# bin. Sometimes, bots take microchips from
# "input" bins, too. Microchips each contain a
# single number; the bots must use the problem
# input to decide what to do with each chip. Some
# of the instructions specify that a specific-
# valued microchip should be given to a specific
# bot; the rest of the instructions indicate what
# a given bot should do with its lower-value or
# higher-value chip.
#
# After the instructions execute, what do you get
# if you multiply together the values of one chip
# in each of outputs 0, 1, and 2?

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


# Convert the instructions (as strings) to a list
# of tuples with each tuple containing the
# relevant information about the instruction.
def parseInput(values):
   instructions = list()

   # Iterate through each instruction.
   for line in values:
      # Split it into parts.
      parts = line.split()

      # Handle a bot receiving a value.
      if parts[0] == 'value':
         # Just need the bot number and the value.
         instructions.append((int(parts[5]), int(parts[1])))

      # Handle a bot giving two values (low/high).
      else:
         # Need the bot number, the destination 
         # number for the low value (bot or
         # output) and the high value (bot or
         # output).
         instructions.append((int(parts[1]), parts[5], int(parts[6]), parts[10], int(parts[11])))

   # Return list of instructions.
   return instructions


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file.   
   file_input = readFile("input10b.txt")
   instructions = parseInput(file_input)

   # Store chip values with either bots or outputs.
   bots = dict()
   outputs = dict()

   # Keep processing as long as instructions
   # remain.
   while len(instructions) > 0:
      # Initialize a list for storing instructions
      # that can't execute yet (bot doesn't have
      # both chips).
      next_round = list()

      # Iterate through the instructions.
      for i in instructions:
         # If length = 2, then bot retrieves chip.
         if len(i) == 2:
            if i[0] not in bots:
               bots[i[0]] = list()
            bots[i[0]].append(i[1])

         # If length = 5, then bot gives low chip
         # and high chip to bots or outputs.
         elif len(i) == 5:
            # The bot has no chips.
            if i[0] not in bots:
               next_round.append(i)

            # The bot has only one chip.
            elif len(bots[i[0]]) < 2:
               next_round.append(i)

            # The bot has both chips.
            else:
               # Get low and high values.
               low, high = sorted(bots[i[0]])

               # Handle giving low chip to bot.
               if i[1] == 'bot':
                  if i[2] not in bots:
                     bots[i[2]] = list()
                  bots[i[2]].append(low)

               # Handle giving high chip to bot.
               if i[3] == 'bot':
                  if i[4] not in bots:
                     bots[i[4]] = list()
                  bots[i[4]].append(high)

               # Handle giving low chip to output.
               if i[1] == 'output':
                  outputs[i[2]] = low

               # Handle giving high chip to output.
               if i[3] == 'output':
                  outputs[i[4]] = high

      # Set up for next round.
      instructions = next_round

   # Display the product of outputs 0, 1, and 2.
   product = 1
   for key in outputs:
      if (key == 0) or (key == 1) or (key == 2):
         product *= outputs[key]

   print('The product of outputs 0, 1, and 2 = ' + str(product))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
