list_programming = ["java", "python", "c#"]

if __name__ == '__main__':
    print(list_programming)
    node = input("hi please write node:")
    if  int(node)>len(list_programming):
        print("I can not delete node")
    else:
        del list_programming[int(node)]
    print(list_programming)