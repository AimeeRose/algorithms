# Overall idea of quicksort is:
#   1. Take a random element p from array A
#   2. Partition A so that all elements less than p are to its left, and all elements greater than p are to its right
#   3. Recurse on the left and right subarrays in A
#
import random

# Random partition takes an array A,
# and partitions around the a random element p.
#
# First it must swap the random element with the first element so we can keep track of what things
# are sorted and unsorted.
#
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
def partition(A, start_index, end_index):
  # Base case: if this part of the array is only one item, return.
  random_index = random.randint(start_index, end_index)
  p = A[random_index]
  print "Random: " + str(p)
  first_element = A[start_index]
  # swap first and random elements
  A[start_index] = p
  A[random_index] = first_element
  i = start_index + 1 # p position index
  j = start_index + 1 # p partition index
  while (j < end_index):
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
  current_index = i - 1
  # swap p with the element right before i
  s = A[current_index]
  A[current_index] = p
  A[start_index] = s
  return A

A = []

for _ in range(9): A.append(random.randint(0,100))

A

partition(A, 0, 9)

# Overall idea of quicksort is:
#   1. Take a random element p from array A
#   2. Partition A so that all elements less than p are to its left, and all elements greater than p are to its right
#   3. Recurse on the left and right subarrays in A
#
# Takes array A and returns a sorted version.
#

