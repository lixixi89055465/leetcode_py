string = input()


def Swap(string, i, j):
    """
    交换字符串string中的第i个元素和第j个元素
    """
    string = list(string)
    temp = string[i]
    string[i] = string[j]
    string[j] = temp
    string = "".join(string)
    return string


def Perm(string, k, m):
    """
    依次循环交换
    最外层：第一位数与其后面的各位数进行交换
    次外层：第二位数与其后面的各位数进行交换
    一直循环...
    最后一层：倒数第二位与倒数第一位进行交换
    """
    if (k == m - 1):
        print(string)
    else:
        for i in range(k, m):
            string = Swap(string, k, i)
            Perm(string, k + 1, m)
            string = Swap(string, k, i)


Perm(string, 0, len(string))