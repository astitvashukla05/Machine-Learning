import numpy as np
import shutil
import os
# print(1+1)
# for i in range(1,5):
#     if i==3:
#         pass
#         print(i)
#     print(i)

# my_set=set([1,2,3,4,5],[10])
# print(my_set)
print(np.__version__)
word="count unique letters in a sentence"
spi=word.split('t')
print(set(spi))
unique=set(word)
print(unique)
my_set={}
my_dict={}
print(type(my_set),type(my_dict))
new_dict={"m":1,"p":0,"I":0}
for keys in new_dict.keys():
    print(f"{keys} : {new_dict[keys]}")
    
squares_even={x:x**2 for x in range(10) if x%2==0}
print(squares_even)

## count freq in list 
numbers=[1,2,3,4,5,6,77,6,5,4,3,2,1,23,35,7,8]
freq_dict={}
for number in numbers:
    if number in freq_dict:
        freq_dict[number]=freq_dict[number]+1
    else:
      freq_dict[number]=1
print(freq_dict)
add=lambda a,b:a+b
print(add(2,3))

## square 
numbers=[1,2,3,4,5,6,7,8];

square=lambda x:x**2
squared=list(map(square,numbers)) 
print(squared)
# converting string of list  into numbers
str1=['1','2','3','4']
print(list(map(int,str1)))

print(os.getcwd())
print(np.array([1,2,3,4]))
shutil.copyfile("source.txt","destination.txt")

