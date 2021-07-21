#Exception handiling = 

a = 5
b = 2


try:
	print("resource open")
	print(a/b)
	k = int(input("enter a number"))
	print(k)

	print("resource close")

except zeroDivisionError as e:
	print("hy you cannot divide a number by zero",e)
except valueError as e:
	print("Invalid input")

except Exception as e:
	print("something went wrong")
finally:
	print("Exexuted finally")