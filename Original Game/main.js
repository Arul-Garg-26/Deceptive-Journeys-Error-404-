
let theme = null;
let playerNames = [];
let T_Roles = [];
let assignRoles = [];
let roles = {};
let killing = null;
let checking = null;
let saving = null;

// Setting the theme to Classic
function classicTheme() {
    theme = "Classic";
    T_Roles = ["Mafia", "Detective", "Doctor", "Villager", "Villager", "Villager", "Mafia", "Villager"];
}

// Setting the theme to Ayodhya
function ayodhyaTheme() {
    theme = "Ayodhya";
    T_Roles = ["Drohi", "Gusmath", "Vaidya", "Gramvasi", "Gramvasi", "Gramvasi", "Drohi", "Gramvasi"];
}

// Setting the theme to Lakshadweep
function lakshadweepTheme() {
    theme = "Lakshadweep";
    T_Roles = ["Crime Lord", "Inspector", "Chemist", "Fisherman", "Fisherman", "Fisherman", "Crime Lord", "Fisherman"];
}

// Assigning player names that they entered in the form
function playerNamesFunction(a, b, c, d, e, f, g, h) {
    playerNames = [a, b, c, d, e, f, g, h];
    if (h === null) {
        playerNames.pop();
    }
    if (g === null) {
        playerNames.pop();
    }
    temp = giveRoles();
    givingRoles(temp);
}

// Gives random roles to players
function giveRoles() {
    assignRoles = [];
    // Finds which roles are to be given
    if (T_Roles.length > playerNames.length) {
        const l = 8 - playerNames.length;
        if (l > 1) {
            for (let i = 0; i < l; i++) {
                T_Roles.pop();
            }
            T_Roles.pop();
        }
    }
    // Assigning roles
    for (let i = 0; i < playerNames.length; i++) {
        const j = Math.floor(Math.random() * T_Roles.length);
        const x = T_Roles[j];
        assignRoles.push(x);
        T_Roles.splice(j, 1);
    }
    if (theme === "Classic") {
        classicTheme();
    } else if (theme === "Ayodhya") {
        ayodhyaTheme();
    } else if (theme === "Lakshadweep") {
        lakshadweepTheme();
    }
    for (let i = 0; i < playerNames.length; i++) {
        roles[playerNames[i]] = assignRoles[i];
    }
    return roles;
}

// Mafia's killing and doctor's saving
function turn(kill, save) {
    killing = kill;
    saving = save;

    // Checking if saved person that is trying to be killed
    if (killing === save) {
        //display2all("No one died.");
    } else {
        //playerNames.splice(killing, 1);
        //display2all(playerNames[playerNames.indexOf(killing)] + " died.");
    }
}

// The detective checks whether the selected player is the 'Mafia' or not.
function check(check) {
    checking = check;
    if (roles[checking] === "Mafia" || roles[checking] === "Crime Boss" || roles[checking] === "Drohi") {
        //display2detective(true);
    } else {
        //display2detective(false);
    }
}

// Setting random theme without input
if (Math.floor(Math.random() * 4) === 0) {
    classicTheme();
} else if (Math.floor(Math.random() * 3) === 0) {
    ayodhyaTheme();
} else {
    lakshadweepTheme();
}