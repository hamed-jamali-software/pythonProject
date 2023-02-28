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


def findNumber(list):
    for i, x in enumerate(list):
        if x == 2:
            print("number is index :", i)


if __name__ == "__main__":
    int_list = inputer()
    findNumber(int_list)

