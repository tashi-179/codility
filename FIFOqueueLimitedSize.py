Implement a FIFO queue with limited size
Problem statement
implement a FIFO queue with limited size. It should support the  following commands:
SIZE - returns number of items currently in the queue without modifying it.
OFFFER xxx - adds the given element xxx to the queue. Returns true if the item was accepted by the queue, or false if the number of elements in the queue reached the size limit. xxx can be any string.

TAKE - take s and element from the queue. Returns the item taken if the queue was not empty. Does not return anything if the queue was empty.
Input and output specification
def solution(X, B)

Input 
C, ["command 1", "command 2", "command N"]
Where C is capacity of the queue (0 <= C<=10000).
Size of the commands array N is (1 <= N <= 10000).

Output
Function solution must return an array containing strings returned by the commands in the same order as they were executed.

Input Example
2, ["OFFER hello", "OFFER world", "OFFER !", "TAKE", "SIZE"]

Output Example 
For the above input, the output should be the following:
["true", "true", "false", "hello", "1"]

Solution

def solution(X, B):
    queue = []
    output = []

    for command in B:
        command_args = command.split()
        command_type = command_args[0]

        if command_type == 'SIZE':
            output.append(str(len(queue)))
        elif command_type == 'OFFER':
            item = command_args[1]
            if len(queue) < X:
                queue.append(item)
                output.append('true')
            else:
                output.append('false')
        elif command_type == 'TAKE':
            if len(queue) > 0:
                output.append(queue[0])
                del queue[0]
            else:
                output.append('')
    return output
