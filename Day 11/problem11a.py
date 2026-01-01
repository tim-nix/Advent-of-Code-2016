# The problem input consists of a description of
# the contents on each floor of the "Radioisotope
# Testing Facility". Here, special generators
# (RTGs) are designed to be paired with specially-
# constructed microchips (chips). If a chip is
# ever left in the same area as another RTG, and
# it's not connected to its own RTG, the chip will
# be fried. Therefore, chips need to be connected
# to their corresponding RTG when they're in the
# same room, and away from other RTGs otherwise.
# All chips and RTGs need to be moved to the 
# fourth floor of the facility. An elevator is
# available that can move between the four floors.
# Its capacity rating means it can carry at most
# yourself and two RTGs or microchips in any
# combination. As a security measure, the elevator
# will only function if it contains at least one
# RTG or microchip. The elevator always stops on
# each floor to recharge, and this takes long
# enough that the items within it and the items on
# that floor can irradiate each other. (You can
# prevent this if a chip and its RTG end up on the
# same floor in this way, as they can be connected
# while the elevator is recharging.) When you
# enter the containment area, you and the elevator
# will start on the first floor (floor 0).
#
# What is the minimum number of steps required to
# bring all of the objects to the fourth floor?

import time          # For timing the execution
import math          # For math.inf


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


# From the file input, extract the important
# information and store it in a tuple of tuples of
# tuples. The inner tuples identify each equipment
# piece as either a microchip or generator and the
# corresponding type. The middle tuples correspond
# to each floor of the facility. The outer tuple
# stored the floor data.
def parseInput(values):
   diagram = list()

   # Each line of file input data corresponds to
   # the contents of a single floor.
   for i in range(len(values)):
      floor = list()

      # Remove commas and periods.
      values[i] = values[i].replace(',', '')
      values[i] = values[i].replace('.', '')
      parts = values[i].split()

      # Extract the word 'microchip' or 'generator'
      # and the word prior to it. 
      for j in range(len(parts)):
         if parts[j] == 'microchip':
            # Slightly simplify the type of chip
            # by ignoring '-compatible'.
            type_chip = parts[j-1].split('-')
            floor.append((type_chip[0], 'microchip'))
         elif parts[j] == 'generator':
            floor.append((parts[j-1], 'generator'))

      # Sort the floor to more easily detect
      # duplicate arrangements.
      diagram.append(sorted(floor))
   
   return diagram


# Determine if a floor arrangement is good; that
# is, if the equipment on the floor results in
# a microchip being destroyed with the presence of
# a different type generator without the precence
# of the correct type generator.
def goodFloor(floor):
   # Iterate through the floor equipment.
   for f1 in floor:
      # If a microchip is on the floor...
      if (f1[1] == 'microchip'):
         # Make sure that either the correct
         # generator is present or no generator is
         # present.
         good_generator = False
         bad_generator = False
         for f2 in floor:
            if (f2[0] == f1[0]) and (f2[1] == 'generator'):
               good_generator = True
            elif (f2[0] != f1[0]) and (f2[1] == 'generator'):
               bad_generator = True

         # Otherwise, the chip is destroyed.
         if bad_generator and not good_generator:
            return False

   # The chip is good.
   return True


# As long as each floor is good (no chip
# destroyed), we don't care about the specific
# type of generators or microchips, only the
# general layout type. Thus, we don't need to
# search similar patterns. So, the patterns are
# stored without the type of each RTG or chip.
def getPattern(diagram):
   # Copy the diagram excluding each RTG and chip
   # type.
   pattern = list()
   for floor in diagram:
      p_floor = list()
      for item in floor:
         p_floor.append(item[1])

      pattern.append(tuple(sorted(p_floor)))

   # Return as nested tuple for storage in a set.
   return tuple(pattern)


# Make a deep copy of the diagram with changes
# based on the move, the current floor, and the
# new floor (either one floor up or down).
def updateDiagram(diagram, move, old_floor, new_floor):
   # Copy the diagram.
   diagram_copy = list()
   for i in range(len(diagram)):
      f_list = list()
      for j in range(len(diagram[i])):
         # But, exclude moved equipment from the
         # old floor.
         if i == old_floor:
            if diagram[i][j] not in move:
               f_list.append(diagram[i][j])

         else:
            f_list.append(diagram[i][j])

      # Add moved equipment to the new floor.
      if i == new_floor:
         f_list += move

      # Add updated floor to the copy.
      diagram_copy.append(tuple(sorted(f_list)))

   # Return the copy.
   return tuple(diagram_copy)



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and process.   
   file_input = readFile("input11b.txt")
   diagram = parseInput(file_input)

   # Set for preventing state space explosion.
   seen = set()
   pattern = getPattern(diagram)
   seen.add((0, pattern))

   # For breadth-first search.
   to_visit = [ [0, diagram, 0] ]

   # Continue BFS until all equipment is moved to
   # the top floor.
   found = False
   new_length = 0
   while not found:
      # Extract from front of to_visit.
      floor, diagram, path_length = to_visit.pop(0)

      # Periodically output the depth of search.
      if path_length > new_length:
         print('path_length = ' + str(path_length))
         new_length = path_length

      # Check to see if move is done (nothing is
      # located on the lower floors).
      done = all([ len(f) == 0 for f in diagram[:-1] ])
      # If so, then done with BFS.
      if (floor == 3) and done:
         min_path = path_length
         found = True

      # Otherwise, from the current diagram,
      # generate and perform each good move.
      else:
         # Generate all moves of one and two items
         # of equipment.
         moves = list()
         for e1 in range(len(diagram[floor])):
            moves.append([ diagram[floor][e1] ])
            for e2 in range(e1+1, len(diagram[floor])):
               moves.append([ diagram[floor][e1], diagram[floor][e2] ])

         # Iterate through each move.
         for m in moves:
            # Only move up if not on the top floor.
            if floor < len(diagram) - 1:
               # Make an updated copy of the
               # diagram based on the move.
               diagram_copy = updateDiagram(diagram, m, floor, floor+1)

               # Check to make sure move is safe.
               if goodFloor(diagram_copy[floor]) and goodFloor(diagram_copy[floor+1]):
                  # Check to make sure move hasn't
                  # already been seen.
                  pattern = getPattern(diagram_copy)
                  if ((floor+1, pattern) not in seen):
                     # Add new diagram.
                     seen.add((floor+1, pattern))
                     to_visit.append([floor+1, diagram_copy, path_length+1])

            # Only move down if not on the bottom
            # floor and lower floors are not empty.
            at_bottom = all([ len(diagram[i]) == 0 for i in range(floor) ])
            if (floor > 0) and not at_bottom:
               # Make an updated copy of the
               # diagram based on the move.
               diagram_copy = updateDiagram(diagram, m, floor, floor-1)

               # Check to make sure move is safe.
               if goodFloor(diagram_copy[floor]) and goodFloor(diagram_copy[floor-1]):
                  # Check to make sure move hasn't
                  # already been seen.
                  pattern = getPattern(diagram_copy)
                  if ((floor-1, pattern) not in seen):
                     # Add new diagram.
                     seen.add((floor-1, pattern))
                     to_visit.append([floor-1, diagram_copy, path_length+1])
                  

   # Display the length of the minimum path.
   print('Length of the minimum path is ' + str(min_path))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
    
        
