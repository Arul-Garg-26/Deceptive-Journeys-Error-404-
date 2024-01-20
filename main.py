import eel
import random
import cgi

eel.init('web')
form = cgi.FieldStorage()
theme = None
player_names = []
T_roles = []
assign_roles =[]

@eel.expose
def classic_theme():
    global theme
    global T_roles
    theme = "Classic"
    T_roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Villager", "Mafia", "Villager"]

@eel.expose
def Player_Names():
    global player_names
    for i in range(1,10):
        #player_names.append(form.getvalue("P_%s" %i))
        pass
    player_names = ["Rishabh", "Dev", "Arul", "Apurv", "Dhanvi", "Nakul"]

@eel.expose
def give_roles():
    global assign_roles
    global player_names
    global T_roles
    if len(T_roles) > len(player_names):
        l = (9-len(player_names))
        if l > 1:
            for i in range(0,l):
                T_roles.pop((l-1))
    for i in range(len(player_names)):
        j=random.randint(-1, len(T_roles))
        print(j)
        x = T_roles[j-1]
        print(x)
        assign_roles.append(x)
        T_roles.pop(T_roles.index(x))
    T_roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Villager", "Mafia", "Villager"]

classic_theme()
Player_Names()
give_roles()
print(player_names)
print(assign_roles)
