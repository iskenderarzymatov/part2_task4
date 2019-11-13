isi = input("Введите число: ").split()
isi1 =int(isi[0])*60*60
isi2 =int(isi[1])*60
isi3 =int(isi[2])
sek = isi1 + isi2 + isi3
bro = input("Введите число: ").split()
bro1 = int(bro[0])*60*60
bro2 = int(bro[1])*60
bro3 = int(bro[2])
sek2 = bro1 + bro2 + bro3
rez = sek2 - sek
print('Результат: ',abs(rez),"сек")
