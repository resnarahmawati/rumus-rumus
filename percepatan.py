# PERCEPATAN RATA-RATA
# a= V2 - V1 / t2 - t1

print('''
\033[94m
=============================
    PERCEPATAN RATA-RATA
=============================
''')

v1 = float(input('Masukan kecepatan 1:'))
v2 = float(input('Masukan Kecepatan 2:'))
t1 = float(input('Masukan waktu 1:'))
t2 = float(input('Masukan waktu 2:'))
a = v1 - v2 / t2 - t1

print('\033[92m\033[01mPERCEPATAN RATA-RATA:', round(a))

