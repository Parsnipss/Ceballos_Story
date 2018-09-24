import time

num = int(input("Please input an integer to countdown from: "))

for i in range(num + 1):
    print(num)
    num = num - 1
    time.sleep(1)