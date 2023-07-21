def has_33(check_list):
    flag = False
    for i in range(len(check_list)-1):
        if check_list[i] == 3 & check_list[i+1] == 3:
            return True
            break
    return flag


check_list = [2, 4, 5, 1, 3, 3, 5]
print(has_33(check_list))