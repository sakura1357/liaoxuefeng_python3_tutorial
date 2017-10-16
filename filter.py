
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    list_numbers = list(str(n))
    i = 0
    j = len(list_numbers)
    for item in list_numbers:
        if list_numbers[i] != list_numbers[j-1]:
            return False
        else:
            continue
        i = i + 1
        j = j - 1
    return n
output = filter(is_palindrome, range(1, 1000))
print(list(output))