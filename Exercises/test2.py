def is_prime(num):
    if num % 2 == 0:
        return False
    i = 3
    while i <= num ** 0.5:
        if num % i == 0:
            return False
        i += 2
    return True


def next_prime():
    cur_num = 3
    prime_index = 2
    while True:
        cur_num += 2
        if is_prime(cur_num):
            prime_index += 1
            yield (cur_num, prime_index)
            

