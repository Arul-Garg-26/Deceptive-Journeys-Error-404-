import eel
import random
import cgi

eel.init('web')
form = cgi.FieldStorage()
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
def Player_Names():
    global player_names
    for i in range(1,9):
        player_names.append(form.getvalue("P%s"%i))

#Gives random roles to players
@eel.expose
def give_roles():
    global roles, assign_roles, player_names, T_roles
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
    for i in player_names:
        roles[i] = assign_roles[player_names.index(i)]
    for i in range(0, len(roles)):
        w = random.randint(0, len(roles))
        eel.grab_info(roles[w])
        print(roles[w])
        roles.pop[w]

@eel.expose
def turn(kill, save):
    global killing, saving
    killing = kill
    saving = save
    
    if killing == save:
        pass
        # nothing happens
    else:
        player_names.pop[killing]
        # player dies
        
@eel.expose
def check(check):
    global checking
    checking = check
    if roles[checking] == "Mafia":
        pass
        #Thumbs up
    elif roles[checking] == "Crime Boss":
        pass
        #Thumbs up
    elif roles[checking] == "Drohi":
        pass
        #Thumbs up
    else:
        pass
        #Thumbs down

#Running everything independantly
if random.randint(0,3) == 0:
    classic_theme()
elif random.randint(0,2) == 0:
    ayodhya_theme()
else:
    lakshadweep_theme()
print(player_names)
print(assign_roles)