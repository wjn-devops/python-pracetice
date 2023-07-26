#1.判斷n是否為質數
#2.找出小於n的所有的質數
#3.n對質數逐一相除


def factorPrime(num):
    prime_list = []
    factor_list = []
    result = []
    for i in range(2, num+1):
        count = 0
        # print(f"i={i}")
        for j in range(2, i+1):
            # print(f"j={j}")
            if int(i % j) == 0:
                count += 1
        # print(f"count={count}")
        if count <= 1:
            prime_list.append(i)
    for item in prime_list:
        while int(num % item) == 0:
            # print(item)
            factor_list.append(item)
            num = int(num / item)
    for index, factor in enumerate(factor_list):
        if index == len(factor_list) - 1:
            print(f"{factor}")
        else:
            print(f"{factor} x ", end='')
    # return prime_list

factorPrime(4)
