#Digunakan ketika ada multiple conditions

#logical operator ada : 
# 1. And, harus keduanya True baru program bisa dijalankan.
# 2. Or, paling tidak satu yang True maka program bisa dijalankan.
# 3. Not, membalikkan nilai, dari yang true, menjadi false. vice versa.

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record :
    print("Eligible for loan")
else :
    print("Sorry, your not allowed to loan")