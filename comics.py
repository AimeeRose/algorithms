import csv

G = {}
characters_in_book = {}
csvfile = 'marvel.tsv'

with open(csvfile, 'rb') as input_file:
  # Store as list because file is read out
  lines = list(csv.reader(input_file, delimiter = '\t'))
  for line in lines:
    character, comic_book = line
    # Add the character to the graph
    if character not in G: G[character] = {}
    if comic_book not in characters_in_book: characters_in_book[comic_book] = []
    if character not in characters_in_book[comic_book]: characters_in_book[comic_book].append(character)
  for line in lines:
    character, comic_book = line
    # find all the other characters in that book
    other_characters = characters_in_book[comic_book]
    # For each of those other characters
    for other in other_characters:
      if other != character:
        # The distance from the other to the character is a ratio of the number of books they have in common
        if other not in G[character]:
          G[character][other] = 1.0
        else:
          G[character][other] = 1/((1/G[character][other]) + 1)

def distance_by_total_hops(G, character):
  # Keep track of how many hops it took to get to each character.
  reachable_characters = {}
  # Start a todo list with the character of interest.
  todo = [character]
  # The distance from the character to itself is 0.
  reachable_characters[character] = 0
  # While there are still nodes to look at.
  while len(todo) > 0:
    # Take the first item off the list
    current_node = todo[0]
    del todo[0]
    # Get all of its neighbors
    neighbors = G[current_node]
    for n in neighbors:
      if n not in reachable_characters:
        # If we haven't already visited n, add it to the todo list.
        todo.insert(0, n)
        # Set the hops to that instance to the hops to the current node plus 1
        reachable_characters[n] = reachable_characters[current_node] + 1
      # If we have already visited n, and if the count of hops is greater than current hops plus one, reassign.
      elif reachable_characters[n] > reachable_characters[current_node] + 1:
        todo.insert(0, n)
        reachable_characters[n] = reachable_characters[current_node] + 1
  return reachable_characters

# Above we have something like {'BUZZ': 2, 'BLACK WIDOW': 2, 'STALKER': 4} which is the total number of hops for the shortest route
# Now we need to hold on to the number of hops based on the shortest distance. 
# reachable_characters will maintain hops and dist, 
#  It will track the number of hops and be overriden when the total distance is less than distance so far.
def distance_by_weighted_hops(G, character):
  # Keep track of how many hops it took to get to each character.
  reachable_characters = {}
  # Start a todo list with the character of interest.
  todo = [character]
  # The distance from the character to itself is 0.
  reachable_characters[character] = {'hops': 0, 'distance': 0}
  # While there are still nodes to look at.
  while len(todo) > 0:
    # Take the first item off the list
    current_node = todo[0]
    del todo[0]
    # Get all of its neighbors
    neighbors = G[current_node]
    for n in neighbors:
      if n not in reachable_characters:
        # If we haven't already visited n, add it to the todo list.
        todo.insert(0, n)
        reachable_characters[n] = {}
        # Set the hops to that instance to the hops to the current node plus 1
        reachable_characters[n]['hops'] = reachable_characters[current_node]['hops'] + 1
        # The distance from character to node n is the distance so far to the current node plus the distance between the current node and this neighbor
        reachable_characters[n]['distance'] = reachable_characters[current_node]['distance'] + G[current_node][n]
      # If we have already visited n, and if the distance counted so far is greater than the distance to the current node plus its edge
      elif reachable_characters[n]['distance'] > reachable_characters[current_node]['distance'] + G[current_node][n]:
        todo.insert(0, n)
        reachable_characters[n]['hops'] = reachable_characters[current_node]['hops'] + 1
        reachable_characters[n]['distance'] = reachable_characters[current_node]['distance'] + G[current_node][n]
  return reachable_characters

def count_shorter_paths(character):
  total_hops = distance_by_total_hops(G, character)
  weighted_hops = distance_by_weighted_hops(G, character)
  shorter_paths_by_weight = 0
  for other in total_hops:
    if weighted_hops[other]['hops'] > total_hops[other]:
      shorter_paths_by_weight += 1
  return shorter_paths_by_weight

count_shorter_paths('SPIDER-MAN/PETER PAR')

characters = ['SPIDER-MAN/PETER PAR', 'GREEN GOBLIN/NORMAN ', 'WOLVERINE/LOGAN ', 'PROFESSOR X/CHARLES ', 'CAPTAIN AMERICA']

total_short_paths = 0
for character in characters:
  total_short_paths += count_shorter_paths(character)

