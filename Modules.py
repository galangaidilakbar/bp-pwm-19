# Modules digunakan untuk mengorganisasikan kode menjadi lebih baik, Seperti supermarket yang mengkelompokkan barang2 ny
# Menjadikan file nya berpisah pisah agar kode utama itu tampak simple
# ada 2 cara menggunakan module, ada dengan mengimport semuanya, dan ada dengan mengimpor spesifik part

import Converter
from Converter import kg_to_lbs

# Kalau From dia langsung panggil tanpa menuliskan Converternya
kg_to_lbs(70)

# Kalau langsung impor, penulisannya lebih spesifik
print(Converter.kg_to_lbs(70))