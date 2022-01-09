"""
Reverse Integer

Solution
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
"""

class Solution:
    def reverse(self, x: int) -> int:
        #s = IntToStr(x)
        minus = 0 
        
        if x < 0:
            s = str(x)[1:]
            minus = 1
        else:
            s = str(x)
            
        s = s[::-1]
        print(s)
        if s.isnumeric() and int(s) < 2147483648: 
            if minus == 0:
                s = int(s)
                return s
            else:
                s = int(s)
                return '-'+str(s)
        else:
            return 0
        