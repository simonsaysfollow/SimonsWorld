var i = 0;
var txt = "DEVELOPER."; /* The text */
var speed = 200; /* The speed/duration of the effect in milliseconds */

function writeDev(){
   
    if (document.querySelector(".jobTitle")) {
        if (i < txt.length) {
            document.querySelector(".jobTitle").style.color="white";
            document.querySelector(".jobTitle").textContent += txt.charAt(i);
            i++;
            setTimeout(writeDev, speed);
        }
    }
}
writeDev()


function showNumber() {
    var x = document.querySelector(".showNumber");
    if (x.style.display === "flex") {
        x.style.display = "none";
       
    } else {
        x.style.display = "flex";
        x.style.alignItems = "center";
        x.style.justifyContent = "center";
        x.style.backgroundColor = "white";
        x.style.transition = "2s ease";
        x.style.height = "100px";
        x.style.fontSize = "22pt";
        // x.textContent = "Cell: (510)734-9328"
        let anchor = document.createElement("a");
        let linkText = document.createTextNode("Cell: (510)734-9328");
        anchor.appendChild(linkText);
        anchor.href = "tel:5107349328";
        x.appendChild(anchor)

    }
    
}



