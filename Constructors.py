class Point :
    # __init__ adalah singkatan dari inisialisasi
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')


point = Point(10,20)
point.x = 12
print(f"{point.x} and {point.y}")