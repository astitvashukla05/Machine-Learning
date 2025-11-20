# # Read a file
import os
# with open('test.txt','r') as file:
#  #   content=file.read()
#   #  print(content)
#    for line in file:
#        print(line.strip()) # removes the new line character
    

# with open('test.txt','w') as file:
#     file.write("Hello \n")
#     file.write("This is all testing")
    
# # with open('test.txt','r') as file:
# #  #   content=file.read()
# #   #  print(content)
# #    for line in file:
# #        print(line.strip())

# with open('test.txt','a') as file:
#     file.write('\nI am trying to append something\n')

# with open('test.txt','r') as file:
#     content=file.read()
#     print(content)
    
# To read data from source file and write it in the destination file

# with open('source.txt','r') as file:
#     content=file.readlines()
#     print(content)

# with open('destination.txt','w') as file:
#     file.writelines(content)

#os.mkdir('PACAKGES')
items=os.listdir('.')
print(items)

## Joining Paths
dir_name='folder'
file_name='text.txt'
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)