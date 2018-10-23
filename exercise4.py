def divisor_list(n):
    try:
        val = int(n)
    except:
        print("That is not a number")
        return []
    if val != float(n):
        print("That is not an integer number")
        return []
    if val < 0:
        print("That is not a positive number")
        return []

    # now we have an integer, positive number to work with
    divisors = []
    for i in range(1, val+1):
        if val % i == 0:
            divisors.append(i)

    return divisors

list_div = divisor_list("dd")

list_div = divisor_list(48.1)
list_div = divisor_list("-48")
list_div = divisor_list("48")
print(list_div)
