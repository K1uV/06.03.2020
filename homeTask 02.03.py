import random

print('''
●▬▬▬▬▬▬ஜ۩۞۩ஜ۩۞۩ஜ۩۞۩ஜ▬▬▬▬▬▬●
┏┓┏┓┏┓╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓
┃┃┃┃┃┃╋╋┃┃╋╋╋╋╋╋╋╋╋╋╋╋┃┃
┃┃┃┃┃┣━━┫┃┏━━┳━━┳┓┏┳━━┫┃
┃┗┛┗┛┃┃━┫┃┃┏━┫┏┓┃┗┛┃┃━╋┛
┗┓┏┓┏┫┃━┫┗┫┗━┫┗┛┃┃┃┃┃━╋┓
╋┗┛┗┛┗━━┻━┻━━┻━━┻┻┻┻━━┻┛
●▬▬▬▬▬▬ஜ۩۞۩ஜ۩۞۩ஜ۩۞۩ஜ▬▬▬▬▬▬●''')
name1 = "Igor"
name2 = "Sanya"
name3 = "Dima"

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
    



if name1 == name_person:
    name_1()
if name2 == name_person:
    name_1()
if name3 == name_person:
    name_1()
