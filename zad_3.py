def is_even(number: int) -> bool:
    return number % 2 == 0

to_check = 10
result = is_even(to_check)

if result:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")
