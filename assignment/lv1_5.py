def remove_duplicates(nums):
    listnums = []
    for i in nums:
        if i in listnums:
            continue
        else:
            listnums.append(i)

    return listnums

print(remove_duplicates([1,2,2,3,1,4]))
    