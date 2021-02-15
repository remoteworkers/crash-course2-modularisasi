from geometri.persegipanjang import hitung_luas_persegi_panjang
from geometri.segitiga import hitung_luas_segitiga

hitung_luas_segitiga(30,60)
print(f'Hasil perhitungan segitiga{hitung_luas_segitiga(30,60)}')

print('\nATAU')
from geometri.segitiga import hitung_luas_segitiga as Ls

alas = 30
tinggi = 60
print(f'Hasil perhitungan segitiga {Ls(alas,tinggi)}')

Geometri(20,10)
print(f'Menghitung Luas Persegi Panjang dengan fungsi {Geometri(20,15)}')

print('\nATAU')
from Geometri.Persegipanjang import Geometri as LPP
print(f'Menghitung Luas Persegi Panjang dengan fungsi {LPP(20,15)}')

print('\nATAU')
panjang = 15
lebar = 15
print(f'Menghitung Luas Persegi Panjang dengan fungsi {LPP(panjang,lebar)}')
