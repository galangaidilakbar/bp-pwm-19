#METHODS IN LIST

#.append digunakan untuk menambahkan item di list
#.insert digunakan untuk memasukkan item dengan lebih spesifik
#.remove digunakan untuk menghapus item di list
#.clear untuk menghapus data
#.pop untuk menghapus data paling akhir
#.index digunakan untuk melihat item ada di index keberapa?
#in digunakan untuk men cek ada atau tidak item di list
#.count digunakan untuk menghitung ada berapa data yang sama di list.
#.sort untuk mengurutkan data dari yang terkecil ke yang terbesar
#.reserve digunakan untuk mengurutkan ddata dari yang terbesar ke yang terkecil, wajib di kasih .sort dulu
#.copy untuk mengkopi data di list


numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)