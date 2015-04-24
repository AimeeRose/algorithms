# rselect takes a list, length and an i order statistic as parameters
# A, n, i
# if length n is 1, return A[0]
# otherwise, partition A

# A = array of ints
# n = length of A
# i = ith order statistic of interest
# returns the value of the ith order statistic of A
def partition(A, n, i):
  if n == 1:
    return A[0]
  # pick randomly from A
  random_index = random.randint(0, n - 1)
  p = A[random_index]
  # Swap it with the first element
  first_element = A[0]
  A[0] = p
  # instantiate the cursor and p's index
  p_index = 0
  cursor = 1
  # loop from 0 to n
  while (cursor < n):
    # current element
    q = A[cursor]
    if q <= p:
      # swap
      # Find the value at one place greater than the position index
      r = A[p_index + 1]
      A[cursor] = r
      A[p_index] = q
      cursor += 1
      p_index += 1
    else:
      cursor += 1
  if p_index == i:
    return A[p_index]
  elif p_index < i:
    subarray = A[p_index:n]
    partition(subarray, len(subarray), i - p_index)
  else:
    subarray = A[0:i-1]
    partition(subarray, len(subarray), i)
  print A
  return A[p_index]


import random

A = []

for _ in range(9): A.append(random.randint(0,100))

A

median = len(A) / 2

median

partition(A, len(A), median)
