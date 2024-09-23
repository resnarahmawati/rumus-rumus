# KALOR JENIS ES
# Q = m × c × t

print('''
\033[97m
=============================
       KALOR JENIS ES
=============================
''')

m = float(input('Masukan massa benda:'))
c = float(input('Masukankalor jenis es (dalam Joule per kilogram per derajat Celsius) :'))
t = float(input('Masukan perubahan suhu es:'))
Q =  m * c * t

print('\033[36m\033[36mKALOR JENIS ES:', round(Q))

