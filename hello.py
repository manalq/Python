print("Hello World")

#Activity1
#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
first_name = "Manal"
last_name = "Qureishy"

def user():
    print("======================================")
    print(f"My name is {first_name} {last_name}")
    print("======================================")

user()

#Activity2
total_amount = float(input("Enter the total amount: "))
tip_percentage = float(input("Enter the tip percentage: "))

def tip_calculator(total_amount):
   return (total_amount * (tip_percentage / 100))

tip_amount = tip_calculator(total_amount)
print(tip_amount)

