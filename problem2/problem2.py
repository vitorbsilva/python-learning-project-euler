last_numbers = [0, 1]
n = 1
even_numbers = 0
while n < 4*10**6:
    n = sum(last_numbers)
    last_numbers[0] = last_numbers[1]
    last_numbers[1] = n
    if n % 2 == 0:
        even_numbers += n
print(even_numbers)