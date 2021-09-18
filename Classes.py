# Digunakan untuk mendefinisikan type baru
# Gunakan Huruf besar pada penamaan class
class Point :
    # Menambahkan method di body class
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point1 = Point()
# Kita juga bisa menambahkan atribut yang bisa di letakkan di manapun di program kita
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)