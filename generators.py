def odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

def multiples_of_five(start, end):
    for num in range(start, end + 1):
        if num % 5 == 0:
            yield num

def palindromes(start, end):
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            yield num

if __name__ == "__main__":
    print("Непарні числа від 1 до 20")
    print(list(odd_numbers(1, 20)))
    print("\nЧисла кратні 5 від 1 до 50")
    print(list(multiples_of_five(1, 50)))
    print("\nПаліндроми від 1 до 200")
    print(list(palindromes(1, 200)))

