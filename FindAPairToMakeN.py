Find a pair to make N
Problem Statement
You have several sticks of different lengths, and a stick a case of a fixed length. We want to find 2 sticks that just fit in the case.
Input and Output Specification

def solution(A, Y)

Input
[L1, L2, ..., Ln], target
The first argument(array of length n) is a list of integers, which represents the lengths of the sticks. The second argument contains an integer target. This integer represents the length of the case.

Output
Return a pair of lengths whose sum is equal to target.
[La, Lb]
Returned values should be ordered in ascending order. (e.g. [1,2] is acceptable. [2,1] is not)

If you find 2 or more pairs, return the pair which contains the stick of the shortest length. (e.g. If the target is 5, and you find both [1,4] and [2,3], return [1,4])

In case there is no such pairs, return an empty array [];

Example Input
[1,2,3,4,5],6
Output
[1,5]


Solution:

def solution(A, Y): 
  result = []
  for i in range(len(A)): 
    for j in range(i+1, len(A)): 
      if A[i] + A[j] == Y: 
        result.append([A[i], A[j]])
  if len(result) > 0: 
    result.sort(key=lambda x: x[0])
    return result[0]
  else: 
    return []
