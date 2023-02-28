import numpy as np
from util import Stack
"""
Input
F
B A
E D C

Goal 
B C
D F
A E 

"""

input="FBE,AD,C"
output="BDA,CFE,"

print(input.split(','))
print(output.split(','))

left=[Stack(),Stack(),Stack()]
for i in left:
    i.push("A")
    i.push("B")
print(left[0].list)

for i in left:
    i.push("A")
    i.push("B")
print(left[1].list)

for i in left:
    i.push("A")
    i.push("B")
print(left[2].list)