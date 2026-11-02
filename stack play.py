'''Problem Definition

You are given a string that contains only the bracket characters (, ), [, ], {, and }. A bracket sequence is considered valid if:

every opening bracket has a matching closing bracket of the same type;

brackets are closed in the correct order.

For example:

([]){} is valid

([)] is invalid

(((()))) is valid

Your task is to write a program that reads the bracket string and determines whether it is valid. If the sequence is valid, your program must also report the maximum nesting depth of the sequence. The nesting depth is the maximum number of currently open brackets at any point while scanning the string from left to right. Examples:

()[]{}: maximum depth = 1

([]): maximum depth = 2

(([])): maximum depth = 3


Input Format

A single line containing a non-empty string of bracket characters only.


Output Format

If the bracket sequence is valid, print two lines:

Line 1: Valid

Line 2: Maximum Depth: X

If the bracket sequence is invalid, print one line:

Invalid


Constraints

The input string length is between 1 and 1000.

The string contains only (, ), [, ], {, and }.


Example 1

Input

([]){}


Output

Valid

Maximum Depth: 2


Example 2

Input

([)]


Output

Invalid'''

s=input()

_open={'(':'s','[':'m','{':'o'}
_close={')':'s',']':'m','}':'o'}

def annih(s):
    stack=[]
    dep=0
    maxdep=0
    for ele in s:
        if ele in _open:
            stack.append(ele)
            dep += 1
            maxdep = max(maxdep, dep)
        elif ele in _close:
            if not stack:
                return 'Invalid', maxdep
            elif _close[ele]!=_open[stack[-1]]:
                return 'Invalid', maxdep
            else:
                stack.pop()
                dep-=1
        else:
            pass
    if dep>0:
        return 'Invalid', maxdep
    return 'Valid', maxdep

a,b=annih(s)
if a=='Valid':
    print(a)
    print('Maximum Depth:',b)
else:
    print(a)