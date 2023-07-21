def pyramid(num):
    for n in range(1, num+1):
        print((num-n)*" ", end='')
        print((2*n-1)*"*")

pyramid(6)