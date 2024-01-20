import eel
import random
import cgi

eel.init('web')
form = cgi.FieldStorage()
theme = None
player_names = []
T_roles = []
assign_roles =[]

#Setting the theme to Classic
@eel.expose
def classic_theme():
    global theme
    global T_roles
    theme = "Classic"
    T_roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Mafia", "Villager"]

#Setting the theme to Ayodhya
@eel.expose
def ayodhya_theme():
    global theme
    global T_roles
    theme = "Ayodhya"
    T_roles = ["Drohi", "Gusmath", "Vaidya", "Gramvasi", "Gramvasi", "Gramvasi", "Drohi", "Gramvasi"]

#Setting the theme to Lakshadweep 
@eel.expose
def lakshadweep_theme():
    global theme
    global T_roles
    theme = "Lakshadweep"
    T_roles = ["Mafia", "Inspector", "Chemist", "Fisherman", "Fisherman", "Fisherman", "Mafia", "Fisherman"]

#Assigning player names that they entered in the form
@eel.expose
def Player_Names():
    global player_names
    for i in range(1,9):
        player_names.append(form.getvalue("P_%s"%i))

#Gives random roles to players
@eel.expose
def give_roles():
    global assign_roles
    global player_names
    global T_roles
    #Finds which roles are to be given
    if len(T_roles) > len(player_names):
        l = (8-len(player_names))
        if l > 1:
            for i in range(0,l):
                T_roles.pop((8-l))
            T_roles.pop(7)
    #Assigning roles
    for i in range(len(player_names)):
        j=random.randint(-1, len(T_roles))
        x = T_roles[j-1]
        assign_roles.append(x)
        T_roles.pop(T_roles.index(x))
    if theme == "Classic":
        classic_theme()
    if theme == "Ayodhya":
        ayodhya_theme()
    if theme == "Lakshadweep":
        lakshadweep_theme()

#Running everything independantly
if random.randint(0,3) == 0:
    classic_theme()
elif random.randint(0,2) == 0:
    ayodhya_theme()
else:
    lakshadweep_theme()
Player_Names()
give_roles()
print(player_names)
print(assign_roles)