# --- LOGIC DRILL 1: Variable Swapping ---
# Task: Swap the variables without using a third 'temp' variable.
a= 10
b= 20
print(f"Before a={a} and b={b}")

#the logic (pythonic way)
a,b = b,a
print(f"After a={a} and b={b}")

# --- LOGIC DRILL 1: Variable Swapping ---
from datetime import date

today = date.today()
deadline = date(2028, 2, 9)
remaining = deadline - today
print(f"Remaining days until deadline: {remaining.days}")

weeks_left = remaining.days // 7
print(f"Weeks left until deadline: {weeks_left}")

n=int(input("Enter an integer: "))
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else: # This covers everything > 20
    print("Not Weird")

print(f"Calculation Complete.\nInput was: {n}")