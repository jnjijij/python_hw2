# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
#                                - другий повертає всі записи
def create_todo_list():
    todos = []

    def add_todo(todo):
        todos.append(todo)

    def get_todos():
        return todos

    return add_todo, get_todos
add_todo, get_todos = create_todo_list()

add_todo("Зробити покупки")
add_todo("Прибрати кухню")

todos = get_todos()
print(todos)



# 2) протипізувати перше завдання
def create_todo_list():
    todos = []

    def add_todo(todo):
        todos.append(todo)

    def get_todos():
        return todos

    return add_todo, get_todos


add_todo, get_todos = create_todo_list()


add_todo("Зробити покупки")
add_todo("Прибрати кухню")


todos = get_todos()
print(todos)


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(n: int) -> str:
    digits = list(str(n))
    result = []

    for i, digit in enumerate(digits):
        if digit != '0':
            result.append(digit + '0' * (len(digits) - i - 1))

    return ' + '.join(result)
print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій
def count_calls_decorator(func):
    count = 1

    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        return result

    return wrapper

def print_call_count(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.count += 1
        print(f"Функція {func.__name__} була викликана {wrapper.count} разів")
        return result

    wrapper.count = 0
    return wrapper
@count_calls_decorator
def greet(name):
    print(f"Привіт, {name}!")

greet("Анна")
greet("Петро")
greet("Іван")

@print_call_count
def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(6, 7))