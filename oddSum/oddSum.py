
def odd_sum(seq):
    result = sum(seq)
    return result

if __name__ == "__main__":
    n, q = input().split(' ')
    result = kfactorization(int(n), int(q))
    text = ""
    for i in result:
        text += str(i) + " "
    print(text)
