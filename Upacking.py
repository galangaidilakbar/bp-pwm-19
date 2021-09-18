#digunakan untuk mengelompokkan nilai dalam tuple atau list ke variabel, variable yang singkat dan tidak berulang
#digunakan jika kita ingin melakukan suatu komplex expression

coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates[2]
# kan panjang, untuk mempersingkat nya kita pasti
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# hmm masih pajang, agar lebih ringkas lagim di python ada yang namaya unpacking, bentuknya seperti ini
x,y,z = coordinates
#jadi nilai nilai dalam tuple akan di simpan masing - masing ke variable. LEBIH SINGKAT KAN 
print(x)