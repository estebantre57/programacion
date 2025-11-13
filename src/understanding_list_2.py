# SLICING
players = ["cr7" , 'messi' , 'Travis' , 'chicha' , 'corona']
print(players[0:3]) 
# slice es trabajar con un grupo especifico 
# de elementos de una lista
print(players[1:4]) #  ['messi' , 'Travis' , 'chicha']
print(players[:4]) # players = ["cr7" , 'messi' , 'Travis' , 'chicha']
print(players[2:]) 

print(players[-3:])

print(players[-3:-1])
print(players[4:2])

# Slicing en for 
players = ["axel" , 'ignacio' , 'Travis' , 'chicha' , 'corona']
first_three_player = players[0:4]
print("first_three_player:", first_three_player)

print("Aqui vienen los tres mejores del salon")
for player in players[0:3]:
    print(player.upper())
    
# Copia de listas
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
# copy_of_food = my_food # Manera erronea de copiar una lista 
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

# Modificando elementos
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
cars[3]="totoya"

    