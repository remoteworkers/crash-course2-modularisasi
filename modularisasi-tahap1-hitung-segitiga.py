"""
PROGRAM MENGHITUNG LUAS SEGITIGA
LUAS SEGITIGA = alas x tinggi /2

"""

print('Menghitung Luas Segitiga #1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi /2
print(f'segitiga dengan alas ={alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nMenghitung Luas Segitiga #2 dengan copy paste')
alas = 20
tinggi = 6
luas_segitiga = alas * tinggi /2
print(f'segitiga dengan alas ={alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas,tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(hitung_luas_segitiga(10,6))
print(hitung_luas_segitiga(20,6))

print('\natau')
print(f'mengitung luas segitiga dengan fungsi = {hitung_luas_segitiga(10,6)}')
print(f'menghitung luas segitiga dengan fungsi = {hitung_luas_segitiga(20,6)}')
print(f'menghitung luas segitiga dengan fungsi = {hitung_luas_segitiga(30,200)}')

print('\natau')
alas = 10
tinggi = 6
print(f'menghitung dengan fungsi, segitiga dengan alas ={alas} dan tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga(alas,tinggi)}')