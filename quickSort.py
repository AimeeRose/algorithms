# Overall idea of quicksort is:
#   1. Take a random element p from array A
#   2. Partition A so that all elements less than p are to its left, and all elements greater than p are to its right
#   3. Recurse on the left and right subarrays in A
#
import random

# Dumb partition takes an array A,
# and partitions around the first element p.
# Keep track of a partition index, where the cursor is between the sorted and unsorted elements.
# Keep track of a p position index, where the element p would go to be between elements less than
# and elements greater than.
#
# Iterate through each element in A,
#  if the element is less than p,
#  Swap the element with first element after the p position index,
#  and increment the p position index. Increment the partition index.
#  if it is greather than p, increment the partition index.
# 
def dumb_partition(A):
  p = A[0]
  i = 1 # p position index
  j = 1 # p partition index
  while (j < len(A)):
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
  # swap p with the element right before i
  s = A[i - 1]
  A[i - 1] = p
  A[0] = s
  return A


A = []

for _ in range(9): A.append(random.randint(0,100))

A

dumb_partition(A)
