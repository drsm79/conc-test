import time

print('Hello')
for i in range(20):
    for j in range(3):
        print(f'i is {i}, j is {j}')
        time.sleep(5)
print('So long')