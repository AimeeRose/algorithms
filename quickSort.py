# quicksort should take an array,
# partition it around a random pivot,
# If the pivot is at place i
# sort the left portions and right portions
import random

def partition(A, start, finish):
  if finish - start <= 1:
    return A
  else:
    # Pick random element between start and finish
    random_index = random.randint(start, finish - 1)
    p = A[random_index]
    # Swap it with the start
    first_element = A[start]
    A[start] = p
    A[random_index] = first_element
    # initialize i and j for start
    i = start + 1
    j = start + 1
    # loop from start to finish
    while (j < finish):
      q = A[j] # the new element
      if q <= p:
        # swap
        # Find the value at one place greater than the position index
        r = A[i]
        A[j] = r
        A[i] = q
        i += 1
        j += 1
      else:
        j += 1
    ps_index = i - 1
    # swap p with the element right before i
    s = A[ps_index]
    A[ps_index] = p
    A[start] = s
    A = partition(A, start, i - 2)
    A = partition(A, i + 1, finish)
    return A

def quicksort(A):
  if len(A) <= 1:
    return A
  else:
    A = partition(A, 0, len(A))
  return A


A = []

for _ in range(9): A.append(random.randint(0,100))

A

quicksort(A)