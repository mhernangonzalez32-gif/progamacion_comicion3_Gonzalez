import random
num_carton = random.sample(range(1,51), 25)
carton = []
for i in range(5):
    fila = num_carton[i*5 : (i+1)*5] 
    carton.append(fila)
        

