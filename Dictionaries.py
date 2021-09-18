costumer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verified" : True
}
#Jika key tidak ada di dalam Dictionaries, kita bisa menambahkan default value
#get digunakan untuk mencari nilai  
print(costumer.get("birthdate", "Jan 1 1980"))

#kita juga bisa menambahkan nilai diluar dari kurung kurawal
costumer["almamater"] = "Universitas Teknologi Yogyakarta"
print(costumer["almamater"])

#kita juga bisa mengupdate nilai dari Dictionary
costumer['name'] = "Jim smith"
print(costumer["name"])