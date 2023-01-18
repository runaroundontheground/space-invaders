var c = document.getElementById("c");
var ctx = c.getContext();

window.onload = function onload() {
    ctx.fillStyle = "black";
    ctx.fillRect(100,100,100,100);
    ctx.fillText("apple", 0, 20);
    console.log("aaa");
}

setInterval(aaaa, 1000);
function aaaa () {
    ctx.fillText("water", 100, 100);
}

