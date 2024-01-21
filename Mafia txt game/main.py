import random
import time


players = []
no_of_players = None
roles_1 = []
playing = None
Role = None
ans = None
k = None
dying = []
saving = None
roles_dict = {}
votes = []
highest_count = 0

def input_name():
    global no_of_players
    no_of_players = input('How Many Players are playing?\n')

def Players():
    global players
    for i in range(0, int(no_of_players)):
        x = i + 1
        players.append(input("enter player %s's name:\n"%x))

def give_roles():
    global roles
    global no_of_players
    global roles_1
    global players
    global roles_dict
    roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Mafia", "Villager", "Villager"]
    for i in range(0, int(no_of_players)):
        roles_1.append(roles[i])
    random.shuffle(roles_1)
    for i in range(0, len(players)):
        roles_dict[players[i]] = roles_1[i]

def player_turns(role):
    global playing
    global Role
    global roles_1
    global ans
    for i in range(0, len(players)):
        playing = players[i]
        Role = roles_1[i]
        if role == (i+1):
            print("""
            PLAYING : %s
            """ %playing)
            ans = input('ready?(Y/N)')
            if ans == "Y" or "y":
                Run_Turns(Role)
                role = role + 1
            else:
                player_turns(Role)

def Run_Turns(role):
    global k, ans, dying, saving
    if role == "Mafia":
        i = "kill?"
        k = 1
    if role == "Detective":
        i = "spy on?"
        k = 2
    if role == "Doctor":
        i = "save?"
        k = 3
    if role == "Villager":
        k = 0
    if k != 0:
        ans = input('Who do you want to %s\n' % i)
        if ans == playing:
            Run_Turns(role)
        elif ans in players:
            if k == 3:
                if ans != saving:
                    dying.append(ans)
            if k == 2:
                if roles_1[players.index(ans)] == "Mafia":
                    print("👍")
                else:
                    print("👎")
            if k == 1:
                saving = ans
                if saving == dying:
                    dying.remove(saving)
        else:
            Run_Turns(role)
    else:
        print("Villager (No activities)")
    time.sleep(2)
    print("""
    ================================================================================================================\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    """)

def display_and_voting():
    global dying
    global dead
    global players
    global ans
    global votes
    global highest_count
    if len(dying) > 1:
        dead = dying[0]+"and"+dying[1]
        players.remove(dying[0])
    else:
        dead = dying[0]
    print(dead+" died")

    votes = []
    for i in range(0, len(players)):
        playing = players[i]
        print("""
        PLAYING : %s
        """ %playing)
        ans = input('Who Do You Vote For?\n')
        if ans == playing:
            ans = input('Who Do You Vote For?\n')
        elif ans in players:
            votes.append(ans)
        highest_count = 0
        for i in players:
            if highest_count < votes.count(i):
                highest_count = votes.count(i)
                name = i
        players.remove(name)


print("\n\n\n\n\n\n         Welcome to the Mafia Game!\n\n\n")
input_name()
Players()
give_roles()
while len(players) > 2:
    player_turns(1)
    display_and_voting()
print("\n\n\n\n\n\n         Thanks For Playing!\n\n\n")