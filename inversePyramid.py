def inversePyramid(num):
    count = 1
    for n in range(1, num+1):
        print((n-1) * " ", end='')
        print((num*2 - count) * "*")
        count += 2

inversePyramid(4)