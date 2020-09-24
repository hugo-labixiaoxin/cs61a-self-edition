def split(n):
    return n//10,n%10
def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
    return sum_digits(all_but_last)+last
def card_num_sum(n):
    if n<10:
        return n
    else:
        all_but_last,last=split(n)
    return last+double_sum(all_but_last)
def double_sum(n):
    all_but_last,last=split(n)
    double_digit=sum_digits(2*last)
    if n<10:
        return double_digit
    else:
        return card_num_sum(all_but_last)+double_digit
    