class Solution:
    def romanToInt(self, s: str) -> int:
        temp={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        num=0
        s=s.replace("IV","IIII")#4 some exceptional cases
        s=s.replace("IX","VIIII")#9
        s=s.replace("XL","XXXX")#40
        s=s.replace("XC","LXXXX")#90
        s=s.replace("CD","CCCC")#400
        s=s.replace("CM","DCCCC")#900
        for char in s:
          num=num+temp[char]
        return num    
        
