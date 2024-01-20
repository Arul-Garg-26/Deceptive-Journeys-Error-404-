import "eel";

function Player_Names(){
    eel.Player_Names();
    eel.give_roles();
}

function grab_info(Arr_names, Arr_roles){
        const NamesArray = Arr_names;
        const RolesArray = Arr_roles;
        var i = Math.floor(Math.random()*NamesArray);
        var Name = NamesArray[i];
        var Role = RolesArray[i];
}
eel.expose(grab_info)

function turn(kill, save){
    eel.turn(kill, save)
}

function check(check){
    eel.check(check)
}
function display2all(txt){

}
eel.expose(display2all)

function display2detective(Bool){

}
eel.expose(display2detective)

window.onload = Player_Names;