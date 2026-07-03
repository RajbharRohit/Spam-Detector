# Binary Search 

prices = [12000, 18000, 24000, 30000, 36000, 42000, 50000]

target = 35000

l = 0
r= len(prices) - 1
answer = -1

while l <= r:
    mid = (l + r) // 2

    if prices[mid] >= target:
        answer = mid
        r = mid - 1
    else:
        l= mid + 1

if answer != -1:
    print("First price :", target, "is", prices[answer])
else:
    print("No product found")
