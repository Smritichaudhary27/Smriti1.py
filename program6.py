#Write a program to find maximum and minimum of  numbers 
s=[2,5,7,9,8]
min= s[0]
max= s[0]


for i in s:
    if max<i:
        max=i
    if min>i:
        min=i
print("max :  " , max)
print("min  : "  , min)