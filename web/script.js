
function Player_Names(){
    eel.player_names();
    eel.give_roles();
}
eel.expose(grab_info)
function grab_info(roles){
    console.log(roles.key + " is " + roles.value);
}
function turn(kill, check, save){
    eel.turn(kill, check, save)
}