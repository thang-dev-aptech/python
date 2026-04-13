nums = [1,2,3,4,5,6,7,8,9,10]

def tach_chan_le(num):
    so_chan = []
    so_le = []

    for i in num:
        if i % 2 == 0:
            so_chan.append(i)
        else:
            so_le.append(i)

    return {
        "so chan": so_chan,
        "so le" : so_le,
        "tong chan": sum(so_chan),
        "tong le": sum(so_le)
    }

print(tach_chan_le(nums))