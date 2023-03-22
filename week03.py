# week03_prime_number_quiz v0.9

start_no, end_no = input("Enter starting number and ending number : ").split()

is_prime = True

for k in range(int(start_no), int(end_no)+1):
    if k < 2:
        is_prime = False
    else:
        for i in range(2, k):
            if k % i == 0:
                is_prime = False
                break
        if is_prime:
            print(k, end=' ')
