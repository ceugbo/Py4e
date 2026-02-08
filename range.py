nums1 = []
while True:
    num = input("Enter a number: ")
    try:
        num2 = float(num)
        nums1.append(num2)
        continue
    except:
        if num == "end":
            break
        else:
            print("enter a number!")
nums1.sort()
print("The range is " + str(nums1[-1] - nums1[0]) + ".")