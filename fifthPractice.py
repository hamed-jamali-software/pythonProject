def inputer():
    # Method by hamed
    print("how can you find index number in list")
    list = []
    n = int(input("Enter the list size:"))

    print("\n")
    for i in range(0, n):
        print("Enter number at index", i)
        item = int(input())
        list.append(item)
    print("list is :", list)
    return list


def findNumber(list, number):
    boolean = False
    for i, x in enumerate(list):
        if x == number:
            boolean = True
            print("number is index :", i)

    if boolean == False:
        print("I can not find")


if __name__ == "__main__":
    number = int(input("Enter the number you want to find: "))
    int_list = inputer()
    findNumber(int_list, number)
