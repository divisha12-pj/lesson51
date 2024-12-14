#create new file
#file=open('new-file.txt','x')
#file.close()

#check if file exist
import os
if os.path.exists('my-file.txt'):
    print("file exists")
else:
    print('file does not exist')
file=open("my file.txt","w")
file.write("hey i am cat and am 5 yrs old")
file.close()

os.remove('my file.txt')
