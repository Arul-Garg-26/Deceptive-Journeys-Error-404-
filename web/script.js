
function Player_Names(){
    eel.Player_Names();
    eel.give_roles();
}

function grab_info(roles){
    console.log(roles.key + " is " + roles.value);
}
eel.expose(grab_info);

function turn(kill, save){
    eel.turn(kill, save)
}

function check(check){
    eel.check(check)
}