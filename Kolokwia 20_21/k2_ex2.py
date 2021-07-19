# 5 pkt

def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0 or num % 3 == 0:
        return False

    a = 5
    while a * a <= num:
        if num % a == 0:
            return False
        a += 2
        if num % a == 0:
            return False
        a += 4

    return True


def rec_div(num, nums, pieces, i):
    if prime(num) and prime(pieces):
        return True

    if i > num:
        return False

    if prime(num % i):
        if rec_div(num // i, [num % i] + nums, pieces + 1, 10):
            return True

    return rec_div(num, [*nums], pieces, i * 10)


def divide(N):
    return rec_div(N, [], 1, 10)
