def longestCommonPrefix(S):
    if "" in S or S == []:
        return ""
    preix = S[0]
    for i in range(1, len(S)):
        while (preix != ""):
            try:
                if str.index(str(S[i]), preix) == 0:
                    break
                else:
                    preix = preix[:-1]
            except:

                preix = preix[:-1]
    return preix


def prefix(list):
    if not list: return 'list is empty.'
    string1 = min(list)
    string2 = max(list)
    for i, c in enumerate(string1):
        if c != string2[i]:
            return string1[:i]
    return string1

def inputer():
    # Method by hamed
    print("how can you calcul prefix fast ??")
    list = []
    n = int(input("Enter the list size:"))

    print("\n")
    for i in range(0, n):
        print("Enter string at index", i)
        item = str(input())
        list.append(item)
    print("list is :", list)
    return list

if __name__ == "__main__":
    string_list = inputer()

    # Method by hamed
    print(prefix(string_list))
    # Method by somebody
    print(longestCommonPrefix(string_list))
