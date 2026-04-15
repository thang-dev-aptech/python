def analyze_numbers(nums):
    sum_list = sum(nums)
    avg = sum_list/len(nums)
    max_list = max(nums)
    min_list = min(nums)
    event_count = 0
    odd_count = 0
    unique_list = []
    for i in nums:
        if i % 2 == 0:
            event_count +=1
        else:
            odd_count += 1
        if i in unique_list:
            continue
        else:
            unique_list.append(i)

    unique_list = sorted(unique_list)




    return {
        "sum": sum_list,
        "avg": avg,
        "max": max_list,
        "min": min_list,
        "even_count":event_count,
        "odd_count": odd_count,
        "unique_sorted": unique_list
    }


print(analyze_numbers([1,2,4,7,8,9,6,4,3,4,3,2,2,3,4,2,3,5,6,7]))