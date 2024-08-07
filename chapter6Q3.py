def insert_array(j, temp):
    for i in range(j):
        temp[i] = int( input("Enter the value: "))
    print(temp)
    return temp

def max(final):
    max = final[0]
    for i in range(1, len(final)):
        if (final[i] > max) : 
            max = final[i]
    print('max: ', max)
    return max
# final = [0 for i in range(3)]
final =[]
max_array = []
for i in range(3):
    j = int(input("How many value(s) do you want to add to this array? "))
    if j <= 0:
        final.append([])
        max_array.append([])
        continue
    temp = [0 for  i in range(j)]
    original_array = insert_array(j, temp)
    final.append(original_array)
    max_array.append(max(original_array))

print(final)
print(max_array)

