def spyGame(check_list):
    zero_count=0
    for item in check_list:
        if item == 0:
            zero_count += 1
        elif zero_count >= 2 and item == 7:
            return True

    return False



print(spyGame([1, 2, 5, 0, 3, 1, 7]))