import colorama 
from colorama import init
from colorama import Fore, Back, Style

Fore
print('''
●▬▬▬▬▬▬ஜ۩۞۩ஜ۩۞۩ஜ۩۞۩ஜ▬▬▬▬▬▬●
┏┓┏┓┏┓╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋┃┃╋╋╋╋╋╋╋╋╋╋╋╋┃┃
┃┃┃┃┃┣━━┫┃┏━━┳━━┳┓┏┳━━┫┃
┃┗┛┗┛┃┃━┫┃┃┏━┫┏┓┃┗┛┃┃━╋┛
┗┓┏┓┏┫┃━┫┗┫┗━┫┗┛┃┃┃┃┃━╋┓
╋┗┛┗┛┗━━┻━┻━━┻━━┻┻┻┻━━┻┛
●▬▬▬▬▬▬ஜ۩۞۩ஜ۩۞۩ஜ۩۞۩ஜ▬▬▬▬▬▬●''')
print("This programm is only for Igor,Vika and Dima!!!!!")
name1 = "Igor"
name2 = "Vika"
name3 = "Dima"

def krasota():
    print("●▬▬▬▬▬▬ஜ۩۞۩ஜ۩۞۩ஜ۩۞۩ஜ▬▬▬▬▬▬●")

name_person = input("Input your name:  ")

def name_1():
    sex_person = int(input("Input your sex | MALE(1),FEMALE(2)"))
    Man = 1
    Woman = 2 
    if sex_person == Man:
        print("Man")
    elif sex_person == Woman:
        print("Woman")

    age_person = int(input("Input your age:  "))

    if age_person <= 18:
        print("Go and do your homework!!!")
    elif age_person >= 19 and age_person <=25:
        print("Owww....You are adult!")
    elif age_person >= 26 and age_person <= 35:
        print("Go and chill, you works a lot!")
    elif age_person >= 36 and age_person <= 45:
        print("Let*s drunk together!")
    elif age_person >= 46 and age_person <= 55:
        print("ohhh.... You so lucky!!)))")
    else:
        print("Go to PENSIYA")
    
    picture_for_person = str(input("I can show u a  picture. Do u whant?      Yes|No    "))
    Yes = "Yes"
    No = "No"
    if picture_for_person == Yes:
       print('''
___________$$$$$$$$$,
________$$$$$__$__$$$$$,
_____$$$_______$_______$$$,
__$$$_________$$$_________$$$
_$$___________$$$___________$$,
$$____________$$$____________$$,
$$___________$$$$$___________$$,
$$_________$$$$_$$$$_________$$,
$$_____$$$$$$_____$$$$$$_____$$,
$$__$$$$$_____________$$$$$__$$,
_$$$$_____________________$$$$,
__$$_______________________$$,
____$$$$_______________$$$$,
________$$$$_______$$$$,
____________$$$$$$$''')
    if picture_for_person == No:
        print("Bye!")

def name_2():
    sex_person = int(input("Input your sex | MALE(1),FEMALE(2)"))
    Man = 1
    Woman = 2 
    if sex_person == Man:
        print("Man")
    elif sex_person == Woman:
        print("Woman")

    age_person = int(input("Input your age:  "))    

    if age_person <= 18:
        print("You are so beautifull!!!!!!")
    elif age_person >= 19 and age_person <=25:
        print("Krasotka!!!!")
    elif age_person >= 26 and age_person <= 35:
        print("Zhenshina krasivaya...")
    elif age_person >= 36 and age_person <= 45:
        print("ZHinka!!")
    elif age_person >= 46 and age_person <= 55:
        print("Skoro bydesh babyshka!")
    else:
        print("Ti yshe babyshka!")
    
    picture_for_person = str(input("I can show u a  picture. Do u whant?      Yes|No    "))
    Yes = "Yes"
    No = "No"
    if picture_for_person == Yes:
        print('''
        ______________________________|`_\/_\/_\,',_
______________________________;__________`_\/\,._
_____________________________:_______________`_\,/_
______Bart___________________|__________________/_
_________Simpson_____________;_________________:_
____________________________:__________________;_
____________________________|______,---.______/_
___________________________:_____,'_____`,-.__\_
___________________________;____(___o____\___`'_
__________________________:______.______,'__o_;_
________________________/,.`______`.__,'`-.__,_
________________________\___________________\_
_______________________,'__/_`,__________`.,'_
____________________,'`-.__\_/_`,._________;_
________________;_,'______`-.`-'./_`--.____)_
___________,-'____________,--\^-'_
_________,:___________,-'_____\_
________(,'_____`--.__\;-._____;_
________:____Y______`-/____`,__:_
________:____:_______:_____/_;'_
________:____:_______|____:_
_________\____\______:____:_
__________`-.__`-.__,_\____`._
_____________\___\__`._\_____`._
___________,-;____\---)_\_,','/_
___________\__`---'--'"_,'^-;'_
___________(_`_____---'"_,-')_
___________/_`--.__,._,-'____\_
__-hrr-____)-.__,--_||___,--'_`-._
__________/._______,|__________,'\_
__________`--.____,'|_________,-'_

         ''')
    elif picture_for_person == No:
        print("Bye!")

def name_3():
    sex_person = int(input("Input your sex | MALE(1),FEMALE(2)"))
    Man = 1
    Woman = 2 
    if sex_person == Man:
        print("Man")
    elif sex_person == Woman:
        print("Woman")
    age_person = int(input("Input your age:  "))

    if age_person <= 18:
        print("Go and do your homework!!!")
    elif age_person >= 19 and age_person <=25:
        print("Owww....You are adult!")
    elif age_person >= 26 and age_person <= 35:
        print("Go and chill, you works a lot!")
    elif age_person >= 36 and age_person <= 45:
        print("Let*s drunk together!")
    elif age_person >= 46 and age_person <= 55:
        print("ohhh.... You so lucky!!)))")
    else:
        print("Go to PENSIYA")
    
    picture_for_person = str(input("I can show u a  picture. Do u whant?      Yes|No    "))
    Yes = "Yes"
    No = "No"
    if picture_for_person == Yes:
       print('''
       ____________$$$$$$$
___________$$___________$$$$$$$$
___________$______________$$
___________$$$$$$$$$$$$$$$$$$
___________$$$$___________$_$$
___________$__$$_________$___$
____$$$$$$$$$__$________$___$$$$$$$$$
__$$$$____$$$$__$______$__$$$_$_____$$
_$$$______$$_$$__$____$__$$___$$_____$$$
$$______$$$___$$__$$$$$__$$____$$_____$$$
$$_____$$$_____$__$$___$$$$$$$$$$$$____$$
$$_____$$_____$$__$$$$$$$$$____$$$_____$$
_$$___________$$_________$$___________$$
__$$_________$$___________$$$_______$$$
____$$$$$$$$$_______________$$$$$$$$$

___________''')
    if picture_for_person == No:
        print("Bye!")

if name1 == name_person:
    name_1()
if name2 == name_person:
    name_2()
if name3 == name_person:
    name_3()

krasota()