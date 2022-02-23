// console.log("this is my java script");
// // alert("hello")


// var y= "welcome";
// alert(y);

// let m="choose";
// // let m="milk"

// console.log(m)


// var x;
// for (x=0; x<=5; x++){
//  console.log(x)
// }


function validateform(){
    x=document.forms["loginform"]["email"].value;
    if (x==""){
        document.getElementById("email").placeholder="forget your email";
        document.getElementById("email").style.border="3px solid red";
        var p=document.getElementById("valid");
        p.innerHTML="enter the correct email";
        p.style.color="red";
        p.style.fontFamily="vardana";
        return false;
    }
}

function createlement(){
    x.document.getElementById('id');
    // console.log(x) for checking
    x=ducument.createelement("input");
    z=ducument.createelement("label");
    x.setAttribute("class","name");
    y= document.getElementsByClassName("mydiv");
    y.appendChild(x);
    y.appendChild(x);
}