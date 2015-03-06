import random
import math
import heapq

# Helper functions
def parent(i):
  return int(math.floor((i-1)/2))

def right_child(i):
  return (i*2) + 2

def left_child(i):
  return (i*2) + 1

def is_leaf(L, i):
  return left_child(i) > len(L)

def has_single_child(L, i):
  return right_child(i) == len(L)

def swap(L, idx1, idx2):
  val1 = L[idx1]
  val2 = L[idx2]
  L[idx1] = val2
  L[idx2] = val1

# Take the value at L[idx] and compare it with its parent
# If the parent is greater, swap and sift up
#
def sift_up(L, idx):
  if idx > 0:
    parent_idx = parent(idx)
    parent_val = L[parent_idx]
    current_val = L[idx]
    if parent_val > current_val:
      swap(L, parent_idx, idx)
      sift_up(L, parent_idx)
  return

# Graph as list
G = []

for _ in range(18): G.append(random.randint(0,100))

G1 = G[:]

def my_heapify(G):
  # Nodes to visit
  todo = [0]
  while len(todo) > 0:
    # Get next thing todo
    current_idx = todo[0]
    # delete it from the todo list
    del todo[0]
    # append its children
    left_index = left_child(current_idx)
    right_index = right_child(current_idx)
    if right_index < len(G): todo.insert(0, right_index)
    if left_index < len(G): todo.insert(0, left_index)
    # get the values at all the indices
    current_val = G[current_idx]
    #
    # The other way to do this would be to determine if the node is a leaf node or has only one child
    # If leaf node, do nothing.
    if not is_leaf(G, current_idx):
      left_val = G[left_index]
      # If one child only compare with the one child.
      #
      if has_single_child(G, current_idx):
        if left_val < current_val:
          swap(G, current_idx, left_index)
          sift_up(G, current_idx)
      # If two children, get both and do the comparison
      #
      else:
        right_val = G[right_index]
        if left_val < current_val or right_val < current_val:
          if right_val < left_val:
            swap(G, current_idx, right_index)
            sift_up(G, current_idx)
          else:
            swap(G, current_idx, left_index)
            sift_up(G, current_idx)

my_heapify(G1)

G1
