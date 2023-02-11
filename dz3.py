import main

audi = main.Auto('AUDI', 5,)
mersedes = main.Auto('Mersedes', 2)

max = main.Human('Max')
yaryna = main.Human('Yaryna')
vitalik = main.Human('Vitalik')
arsen = main.Human('Arsen')

audi.add_passenger(max)
audi.add_passenger(yaryna)
audi.add_passenger(vitalik)
audi.add_passenger(arsen)

mersedes.add_passenger(max)
mersedes.add_passenger(yaryna)
mersedes.add_passenger(vitalik)

mersedes.print_all_passenger()
audi.print_all_passenger()
audi.print_wheels()