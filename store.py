#Магазин автозапчастей

q = 'radiator'
w = 'front_glass' 
e = 'maslo'
r = 'glass_spray' 
print (q,w,e,r)

def nice():
    print("Такой товар имеется в наличии!")



zapchasty = str(" 'radiator' , 'front_glass', 'maslo' , 'glass_spray' ")
vvod = input("Введите названия товара,чтобы проверить его на наличие:   ")

sproby = 0
while sproby < 20:
    if vvod in zapchasty:
        print("Yest takoe delo!")
    if sproby != zapchasty:
        print(input("Введите названия товара,чтобы проверить его на наличие:   "))
        break
    









# Количество товара
stoemost_tovara = {
    "radiator" : 2000,
    "front_glass" : 2500,
    "glass_spray" : 300,
    "maslo" : 700

}
# Стоимость товара 
kolichestvo_tovara = {
    "radiator" : 8,
    "front_glass" : 2,
    "glass_spray" : 15,
    "maslo" : 3
}

# Имена 
name_1 = "Alex"
name_2 = "Sergio"
name_3 = "Maxim"
name_4 = "Kolya"

# Список потребностей  
Alex_needs = {
    "maslo" : 1,
    "front_glass" : 1
} 

Sergio_needs = {
    "radiator" : 1,
    "glass_spray" : 3
}

Maxim_needs = {
    "maslo" : 2,
    "glass_spray" : 2 
}

Klya_needs = {
    "front_glass" : 1,
    "glass_spray" : 2
}

# Дентги кажлого из клиентов
Alex_money = 5000
Sergio_money = 2000
Maxim_money = 10000
Klya_money = 1000