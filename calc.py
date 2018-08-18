''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def calc():
	# This function adds two numbers 
	def add(x, y):
   		return x + y

	# This function subtracts two numbers 
	def subtract(x, y):
   		return x - y

	# This function multiplies two numbers
	def multiply(x, y):
   		return x * y

	# This function divides two numbers
	def divide(x, y):
   		return x / y

	print("Select operation.")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")

	# Take input from the user 
	choice = input("Enter choice(1/2/3/4):")
#print type(choice)
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
#print type(num1)
#print type(num2)
	if choice == 1:
   		print  num1,"+",num2,"=", add(num1,num2)

	elif choice == 2:
   		print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == 3:
   		print(num1,"*",num2,"=", multiply(num1,num2))

	elif choice == 4:
   		print(num1,"/",num2,"=", divide(num1,num2))
	else:
   		print("Invalid input")

	return render_template('homepage.html', console_gave = [output, errors])

if __name__ == "__main__":
    app.run()
