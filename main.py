import eel
import random

#initiate eel
eel.init('web')
#variables, lists, etc
theme = None
player_names = []
T_roles = []
assign_roles =[]
roles = {}
killing = None
checking = None
saving = None

#Setting the theme to Classic
@eel.expose
def classic_theme():
    global theme, T_roles
    theme = "Classic"
    T_roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Mafia", "Villager"]

#Setting the theme to Ayodhya
@eel.expose
def ayodhya_theme():
    global theme, T_roles
    theme = "Ayodhya"
    T_roles = ["Drohi", "Gusmath", "Vaidya", "Gramvasi", "Gramvasi", "Gramvasi", "Drohi", "Gramvasi"]

#Setting the theme to Lakshadweep 
@eel.expose
def lakshadweep_theme():
    global theme, T_roles
    theme = "Lakshadweep"
    T_roles = ["Crime Lord", "Inspector", "Chemist", "Fisherman", "Fisherman", "Fisherman", "Crime Lord", "Fisherman"]

#Assigning player names that they entered in the form
@eel.expose
def Player_Names(a, b, c, d, e, f, g, h):
    global player_names
    player_names = [a, b, c, d, e, f, g, h]
    if h == None:
        player_names.pop(-1)
    if g == None:
        player_names.pop(-1)

#Gives random roles to players
@eel.expose
def give_roles():
    eel.init('Assigning roles')
    global roles, assign_roles, player_names, T_roles
#Finds which roles are to be given
    if len(T_roles) > len(player_names):
        l = (8-len(player_names))
        if l > 1:
            for i in range(0,l):
                T_roles.pop(j-1)
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
#Runs JS function 'grab_info()'
    eel.grab_info(player_names, assign_roles)

#Mafia's killing and doctor's saving
@eel.expose
def turn(kill, save):
    eel.init('Web')
    global killing, saving
    killing = kill
    saving = save

#Checking if saved person that is trying to be killed
    if killing == save:
        eel.display2all("No one died.")
    else:
        player_names.pop(killing)
        eel.display2all(player_names[player_names.index[killing]]+" died.")
        
#The detective checks wether the selected player is the 'Mafia' or not.
@eel.expose
def check(check):
    global checking
    checking = check
    if roles[checking] == "Mafia":
        eel.display2detective(True)
    elif roles[checking] == "Crime Boss":
        eel.display2detective(True)
    elif roles[checking] == "Drohi":
        eel.display2detective(True)
    else:
        eel.display2detective(False)

#Setting random theme without input
if random.randint(0,3) == 0:
    classic_theme()
elif random.randint(0,2) == 0:
    ayodhya_theme()
else:
    lakshadweep_theme()