import random
import math

# Helper functions
def parent(i):
  return int(math.floor((i-1)/2))

def right_child(i):
  return (i*2) + 2

def left_child(i):
  return (i*2) + 1

def swap(L, idx1, idx2):
  val1 = L[idx1]
  val2 = L[idx2]
  L[idx1] = val2
  L[idx2] = val1

def sift_up(L, idx):
  if idx > 0:
    parent_idx = parent(idx)
    parent_val = L[parent_idx]
    current = L[idx]
    if parent_val > current:
      swap(L, parent_idx, idx)
      sift_up(L, parent_idx)
  return

# Graph as list
G = []

for _ in range(8): G.append(random.randint(0,100))

G

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
  left_val = 1000000000
  if left_index < len(G): left_val = G[left_index]
  right_val = 100000000
  if right_index < len(G): right_val = G[right_index]
  if current_val > left_val and current_val > right_val:
    if left_val < right_val:
      swap(G, current_idx, left_index)
      sift_up(G, current_idx)
    else:
      swap(G, current_idx, left_index)
      sift_up(G, current_idx)
  elif current_val > right_val:
    swap(G, current_idx, right_index)
    sift_up(G, current_idx)
  elif current_val > left_val:
    swap(G, current_idx, left_index)
    sift_up(G, current_idx)
