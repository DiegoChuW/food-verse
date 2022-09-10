const ids =
[ "Chicken", "Beef", "Pork", "Lamb", "Fish", "Other Seafood",
"Potatoes", "Bread", "Rice and grains", "Pasta", "Cereal Products",
"Cheese", "Yogurt", "Butter",
"Chinese Cuisine", "Italian Cuisine", "French Cuisine", "Korean Cuisine", "Spanish Cuisine", "Japanese Cuisine", "Indian Cuisine", "Mexican Cuisine", "No preffered cuisine",

]
function data(){
const map = new Map();
for (let id of ids) {
    if(document.getElementById(id).checked){
        map.set(id,true);
    }
    else {
        map.set(id,false);
    }
}
fetch("/profile", {method: 'POST', body: JSON.stringify(Object.fromEntries(map))});
}

function registration(){
const map = new Map();
map.set("name",document.getElementById("name").value);
map.set("pwd",document.getElementById("pwd").value);
map.set("rpwd",document.getElementById("rpwd").value);
fetch("/register", {method: 'POST', body: JSON.stringify(Object.fromEntries(map))});
}
function login(){
const map = new Map();
map.set("name",document.getElementById("name").value);
map.set("pwd",document.getElementById("pwd").value);
fetch("/login", {method: 'POST', body: JSON.stringify(Object.fromEntries(map))});
}
