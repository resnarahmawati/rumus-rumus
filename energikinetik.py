# ENERGI KINETIK
# a= V2 - V1 / t2 - t1

print('''
\033[94m
=============================
        ENERGI KINETIK
=============================
''')

m = float(input('Masukkan massa (kg) :'))
v = float(input('Masukkan kecepatan (m/s) :'))
ek = 1/2 * m * v**2 

print('\033[92m\033[01mENERGI KINETIK:', round(ek))

