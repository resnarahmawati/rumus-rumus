print('='*40)
print('     PROGRAM KERUCUT')
print('='*40)

r = float(input('Masukkan Jari-jari : '))
s = float(input('Masukkan sisi : '))
phi = 3.14
l = phi*r*s
lp = phi*r*s + phi *r*r

print ('Luas : ', l, 'cm')
print ('Luas Permukaan : ',lp,'cm')