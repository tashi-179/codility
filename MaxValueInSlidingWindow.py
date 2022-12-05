Max value in sliding window
Problem Statement
Given a window size, w and a stream of numbers, s. You can see only w numbers in the window. Each time you receive a number from stream s, compute max numbers in sliding window.

Input and Output Specification

def solution(X, B)

Input
w, [N_1, N_2, ..., N_n]
WHere W is the window size , and N_1, ..., N_n represent elements in the stream.

Note that, you can assume following things. * The window size w will be an integer in the range, 0 < W <= 2,147,483,647 * An element in the stream will be an integer in the range, -2,147,483,648 <= N_i <= 2,147,483,647.

Output
After you read first W-1 numbers, each time you read a number from the input, append the max number in the sliding window to an array. The solution function must return the array after storing all the max numbers in the window into it.

[V1, V2, ...]
...

Input Example 
(Window size W=2 and number stream is S=[2,1,2,-1,3]
2, [2,1,2,-1,3]

Output Example
[2,2,2,3]

def solution(w, s):
  output = []
  window = s[:w]
  output.append(max(window))
  for i in range(w, len(s)):
    window.pop(0)
    window.append(s[i])
    output.append(max(window))
  return output
