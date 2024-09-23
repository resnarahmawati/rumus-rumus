
# JARAK LENSA OBJEKTIF DAN LENSA OKULER
# d = fob + 4 fp + fok

print('''
\033[93m
======================================
JARAK LENSA OBJEKTIF DAN LENSA OKULER
======================================
''')

f_ob = float(input('Masukkan Jarak fokus lensa objektif :'))
fp = float(input('Masukkan Jarak fokus lensa pembalik  :'))
f_ok = float(input('Masukkan Jarak fokus lensa okuler :'))
d = f_ob + 4 + fp + f_ok

print('\033[35m\033[035mJARAK LENSA OBJEKTIF DAN LENSA OKULER:', round(d))