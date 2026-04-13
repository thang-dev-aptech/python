# vòng lặp (for loop)

# while loop
count = 0
while count < 5 : 
    print(count)
    count += 1

# for loop
for i in range(5):
    print(i)

# break
for i in range(5):
    if i == 3:
        break
    print(i)

# continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# else
for i in range(5):
    print(i)
else:
    print("Done")

# nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

