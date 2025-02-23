# #1
# is_next = None
# num = int(input("Enter the number of points: "))
# if num >=83:
#   is_next = True
# else: 
#    is_next = False

# #2
# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience <= 1:
#     developer_type = "Junior"
# elif work_experience <= 5:
#     developer_type = "Middle"
# else:
#     developer_type = "Senior"

# #3
# num = int(input("Enter a number: "))

# if num > 0 and num % 2 == 0:
#     result = "Positive even number"
# elif num > 0:
#     result = "Positive odd number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"


#4
num = int(input("Enter the integer (0 to 100): "))
if 0 <= num <= 100:
    sum = 0
    i = 1

    while i <= num:
        sum += i
        i += 1 

#5
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
   if char == search:
     result += 1


#6
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = int(pool/quantity)
except ZeroDivisionError:
    print('Divide by zero completed!')

#8
def invite_to_event(username):
    return(f"Dear {username}, we have the honour to invite you to our event")


#9
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
        
    apply_discount()

    
    return price


#10
def get_fullname(first_name, last_name, middle_name = ''):
    if middle_name:
      return(f"{first_name} {middle_name} {last_name}")

    else:
        return(f"{first_name} {last_name}")
    

#11
def format_string(string, length):
    if len(string) >= length:
        return string
    else: spaces = (length - len(string)) // 2
    return " " * spaces + string

#12
def first(size, *args ):
   return (size + len(args)) 


def second(size, **kwargs):
    return (size + len(kwargs))


#13
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)

    return numerator // denominator
    
    