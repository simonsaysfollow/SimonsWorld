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
    let anchor = document.createElement("a");
    
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
        //x.textContent = "Cell: (510)734-9328"

        if (x.getElementsByTagName('a').length < 1 ){ 
            let linkText = document.createTextNode("(510)734-9328");
            anchor.appendChild(linkText);
            anchor.href = "tel:5107349328";
            x.appendChild(anchor)
        }

    }
    
}



