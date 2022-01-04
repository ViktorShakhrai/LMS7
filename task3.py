# Task 3
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

# Завдання 3
# Вправа на розуміння списку
# Використовуйте розуміння списку, щоб створити список із кортежами (i, j), де "i" має значення від 1 до 10, а "j" відповідає квадрату "i".

z = {key: key * key for key in range(1, 11)}
print(z)
