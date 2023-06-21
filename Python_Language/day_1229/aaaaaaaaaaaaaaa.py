while True:

    switch = True
    nums1 = []

    a = (input("(1) 숫자를 입력하세요. : "))
    

    if len(a)>1:
        nums1.append(int(a))


    cal = input("(1)계산 방식을 입력하세요. : ")

    nums1 = []
    if cal == "+":
        b = (input("(2) 숫자를 입력하세요. : "))
        nums1.append(int(b))
        n=0
        for i in nums1:
            print(i)
        break
    # elif cal == "-":
    #     b = (input("(2) 숫자를 입력하세요. : "))
    #     nums2.append(int(b))
    #     print(*nums1-nums2)
    #     break
    # elif cal == "*":
    #     b = (input("(2) 숫자를 입력하세요. : "))
    #     nums2.append(int(b))
    #     print(*nums1*nums2)
    #     break
    # elif cal == "/":
    #     b = (input("(2) 숫자를 입력하세요. : "))
    #     nums2.append(int(b))
    #     print(*nums1/nums2)
    #     break