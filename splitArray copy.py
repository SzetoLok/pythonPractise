# https://leetcode.com/problems/split-linked-list-in-parts/?envType=daily-question&envId=2024-09-09


from typing import Optional,List


def split(head:Optional[int],k:int) -> Optional[int]:
    output =[]
    if len(head)<k:
        for i in range(0,k):
            if i >= len(head):
                output.append([])
                continue
            else:
                output.append([head[i]])

    elif len(head) % k == 0:
        count = 0
        for i in range(0,k):
            # beware of the 'assign by value' and 'assign by pointer' attributes of array. Sequences of codes matter in this situation.
            inner = []
            print(i)
            for j in range(0,int(len(head)/k)):
                inner.append(head[count])
                count += 1
            output.append(inner)
    else:
        how_many_elements_for_that_index = [int(len(head)/k)for _ in range(k)]
        print(how_many_elements_for_that_index)
        for i in range(0,len(head)%k):
            how_many_elements_for_that_index[i] += 1
            print(how_many_elements_for_that_index)
        #write the data according to the table



    # this need to be reviewed: Why i suddenly become 5.0 in the 2nd iteration? Found it: missing the word 'range'
    # if len(head) % k == 0:
    #     count = 0
    #     inner = []
    #     for i in (0,len(head)/k):
    #         print(i)
    #         for j in range(0,k):
    #             inner.append(head[count])
    #             count += 1
    #         output.append(inner)

    print(output)
    return output

# a = split([1,2,3,4,5,6,7,8,9,10],1)
# a = split([1,2,3,4,5,6,7,8,9,10],2)
# a = split([1,2,3,4,5,6,7,8,9,10],5)
# a = split([1,2,3,4,5,6,7,8,9,10],10)
a = split([1,2,3,4,5,6,7,8,9,10],4)

