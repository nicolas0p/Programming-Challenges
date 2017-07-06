
def kfactorization(n, qtd):
    if qtd == 1:
        return [n]
    if (n/2).is_integer():
        result = [2]
        result.extend(kfactorization(int(n/2), qtd - 1))
        return result
    for i in range(3, n, 2):
        if (n/i).is_integer():
            result = [i]
            result.extend(kfactorization(int(n/i), qtd - 1))
            return result


if __name__ == "__main__":
    secret = int(input("Type in the secret:"))
    t = int(input("Type in the t:"))
    prime = int(input("Type in the prime:"))
