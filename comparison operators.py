# comparison operators artinya operator pembanding

# Operator pembanding ada : 
# 1. >, besar dari 
# 2. <, kecil dari
# 3. ==, sama dengan
# 4. >=, besar dari sama dengan
# 5. <=, kecil dari sama dengan
# 6. !=, tidak sama dengan

name = input('Enter your name : ')
if len(name) < 3 :
    print('Name must be at least 3 characters')
elif len(name) > 50 :
    print('name can be maximum of 50 characters')
else :
    print("name looks good!")