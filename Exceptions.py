try :
    age = int(input("Age : "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError :
    print('Age cannot be !0')
except ValueError:
    print("Invalid Value")

#Kalau exit code 0 : program success
#Kalau exit code 1 or other : program mengalami crash.
#untuk mengatasi itu kita membutuhkan yang nama nya exceptions. seperti ini
#ValueError untuk mengatasi str yang di ubah ke int
#zZeroDivisionError digunakan untuk mengatasi angka yang di bagi dengan 0