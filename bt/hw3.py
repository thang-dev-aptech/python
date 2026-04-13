list = [1,2,3,4,5,6,7,8,9,10]


def tong_le(list):
    sum = 0
    for i in list :
        if(i % 2 != 0) :
            sum = sum + i
    return sum
sum = tong_le(list)

print(sum)



