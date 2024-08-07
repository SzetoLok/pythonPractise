f1 = open("test.txt",'r')
f2 = open('test2.txt', 'r')
f3 = open ('test3.txt', 'w')
A =[]
# x = f1.readline()
# y = f2.readline()
print('----f1----')
for line in f1:
    line = line.strip()
    A.append(line)
    print(line)
    
print('----f2----')
for line in f2:
    line = line.strip()
    A.append(line)
    print(line)    

for line in A:
    f3.write(line)
# while x and y:
#     final = x

f1.close()
f2.close()
f3.close()

f3 = open('test3.txt', 'r')
print("----f3----")
for line in f3:
    # line = line.strip()
    print(line)
print(A)