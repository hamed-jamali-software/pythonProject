number = input("Enter number:")
print(number)

list1 = list(number)

list.re



list1.reverse()
reverseNumber = "".join(list1)
print("Reverse number is " + reverseNumber)


def reverse(x):
    print(type(x))
    ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0


print(reverse(int(number)))
