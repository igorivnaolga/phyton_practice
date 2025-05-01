# Suppose you have a backpack with a maximum capacity of 50 weight units. You have 3 items with the following weights and values:

# Item 1: weight = 10, value = 60

# Item 2: weight = 20, value = 100

# Item 3: weight = 30, value = 120

# Функція для обчислення максимальної вартості
def knapSack(W, wt, val, n):
    # Basic case
    if n == 0 or W == 0:
        return 0
    
    # Якщо вага n-го предмета більше, ніж місткість рюкзака, то цей предмет не можна включити у рюкзак
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
    
    # повертаємо максимум із двох випадків:
    # (1) n-ий предмет включено
    # (2) не включено
    else:
        return max(
            val[n-1] + knapSack(W - wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1),
        )
    

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# викликаємо функцію
print(knapSack(capacity, weight, value, n))  # 220