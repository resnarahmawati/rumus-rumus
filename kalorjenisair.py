# KALOR JENIS AIR
# Q = m × c air × t

print('''
\033[92m
=============================
       KALOR JENIS AIR
=============================
''')

m = float(input('Masukan massa benda:'))
c_air = float(input('Masukan kalor jenis air (dalam Joule per kilogram per derajat Celsius) :'))
t = float(input('Masukan perubahan suhu air:'))
Q3 =  m * c_air * t

print('\033[35m\033[01mKALOR JENIS AIR:', round(Q3))