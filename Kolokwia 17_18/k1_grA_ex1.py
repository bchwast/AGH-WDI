def to_k_system(num, k):
    l = 0
    c_num = num
    while c_num > 0:
        c_num //= k
        l += 1

    new_num = [0]*l
    for i in range(l-1, -1, -1):
        new_num[i] = num%k
        num //= k

    return new_num
#end def


def are_different(num1, num2):
    sys = 2
    for sys in range(2, 17):
        number1 = to_k_system(num1, sys)
        number2 = to_k_system(num2, sys)

        different = True
        for i in range(len(number1)):
            if not different:
                break
            for j in range(len(number2)):
                if number1[i] == number2[j]:
                    different = False
                    break
            #end for
        #end for

        if different:
            return sys
    #end for
    return "taka podstawa nie istnieje"
#end def


print(are_different(123, 522))
