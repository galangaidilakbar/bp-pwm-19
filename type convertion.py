birth_year = input('Birth year? : ')
print(type(birth_year))         # type digunakan untuk melihat tipe data
age = 2020 - int(birth_year)
print(type(age))
print(age)

# tidak bisa melakukan operasi aritmatika antara str dengan int. jadi solusi nya dengan mengubah str ke int.  cara mengubahnya dengan mendefinisikan variabel tersebut ke tipe data yang kita inginkan. seperti pada baris 2, birth yang seharusnya str diubah ke int. agar bisa diketahui berapa umur nya. tipe data = int(), str(), bool(), float()


# little exercise
weight = input('What is your weight (in pounds) ? : ')
kg = int(weight) * 0.45
print(kg)
