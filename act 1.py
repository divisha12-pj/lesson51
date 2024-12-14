with open('sample.txt','w') as file:
    file.write('\ I am penguin and am 5 yrs old')
file.close()
with open('sample.txt','r')as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)
file.close()
