import bisect

def odd_sum(seq):
    result = 0
    min_pos_odd = False
    max_neg_odd = False
    for i in seq:
        if(i < 0):
            if i % 2 == 1:
                if not bool(max_neg_odd) or i > max_neg_odd:
                    max_neg_odd = i
        else:
            if i % 2 == 0: #even_pos
                result += i
            else: #odd_pos
                result += i
                if not bool(min_pos_odd) or i < min_pos_odd:
                    min_pos_odd = i
    if result % 2 == 1:
        return result
    minus_pos_odd = False
    if bool(min_pos_odd):
        minus_pos_odd = result - min_pos_odd #least positive odd
    plus_neg_odd = False
    if bool(max_neg_odd):
        plus_neg_odd = result + max_neg_odd #least negative odd
    if not bool(minus_pos_odd):
        return plus_neg_odd
    elif not bool(plus_neg_odd):
        return minus_pos_odd
    if minus_pos_odd > plus_neg_odd:
        return minus_pos_odd
    return plus_neg_odd

if __name__ == "__main__":
    n = int(input())
    seq = [int (x) for x in input().split(' ')]
    print(odd_sum(seq))
