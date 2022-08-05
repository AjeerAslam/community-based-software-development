
function func1(event) {
    event.stopPropagation();
    
    alert("upload");
    event.preventDefault();
}


function func2(event) {
    event.stopPropagation();
   
    alert("progress");
 
}
function func3(event) {
    event.stopPropagation();

    alert("project details");
 
}
function accept(md_id) {

alert(md_id);

$.ajax({
url: '/accept/',
type: 'GET',// This is the default though, you don't actually need to always mention it
data:{
'id':md_id
},
success: function(response) {

var instance = JSON.parse(response["rs"]);

},
failure: function(response) { 
alert('Got an error dude');

}
});

event.stopPropagation();
}

function func5(event) {
    event.stopPropagation();
    
    alert("pending");

 
}

function update1(md_id) {

    alert(md_id);
    
    $.ajax({
    url: '/cm_close/',
    type: 'GET',// This is the default though, you don't actually need to always mention it
    data:{
    'id':md_id
    },
    success: function(response) {
    
        
    var instance = JSON.parse(response["rs"]);
    
    },
    failure: function(response) { 
    alert('Got an error dude');
    
    }
    });

    event.stopPropagation();
    
    
    
    }
/*popup


function click1()
{
document.getElementById("a22").innerHTML="MyWork";

document.getElementById("mywork").style.filter="invert(100%)";
document.getElementById("home").style.filter="invert(0%)";
document.getElementById("review").style.filter="invert(0%)";
document.getElementById("completed").style.filter="invert(0%)";
document.getElementById("a2").style.color= "white";
document.getElementById("a1").style.color= "black";
document.getElementById("a3").style.color= "black";
document.getElementById("a4").style.color= "black";
document.getElementById("t1").style.display= "none";
document.getElementById("t2").style.display= "block";
document.getElementById("t3").style.display= "none";
document.getElementById("t4").style.display= "none";
}
document.getElementById("a2").addEventListener("click",click1);

function click2()
{
document.getElementById("a22").innerHTML="Review";
document.getElementById("home").style.filter="invert(0%)";
document.getElementById("mywork").style.filter="invert(0%)";
document.getElementById("review").style.filter="invert(100%)";
document.getElementById("completed").style.filter="invert(0%)";
document.getElementById("a3").style.color= "white";
document.getElementById("a2").style.color= "black";
document.getElementById("a1").style.color= "black";
document.getElementById("a4").style.color= "black";
document.getElementById("t1").style.display= "none";
document.getElementById("t2").style.display= "none";
document.getElementById("t3").style.display= "block";
document.getElementById("t4").style.display= "none";
}
document.getElementById("a3").addEventListener("click",click2);
function click3()
{
document.getElementById("a22").innerHTML="CompletedWorks";
document.getElementById("home").style.filter="invert(0%)";
document.getElementById("mywork").style.filter="invert(0%)";
document.getElementById("review").style.filter="invert(0%)";
document.getElementById("completed").style.filter="invert(100%)";
document.getElementById("a4").style.color= "white";
document.getElementById("a2").style.color= "black";
document.getElementById("a3").style.color= "black";
document.getElementById("a1").style.color= "black";
document.getElementById("t1").style.display= "none";
document.getElementById("t2").style.display= "none";
document.getElementById("t3").style.display= "none";
document.getElementById("t4").style.display= "block";
}
document.getElementById("a4").addEventListener("click",click3);
function click4()
{
document.getElementById('section').innerHTML = 'violet';
}
document.getElementById("a11").addEventListener("click",click4);
function click5()
{
document.getElementById('section').innerHTML = 'black';
}
document.getElementById("a22").addEventListener("click",click5);


function click6()
{
document.getElementById('section').innerHTML = 'puple';
}
document.getElementById("a33").addEventListener("click",click6);
function click7()
{
document.getElementById('section').innerHTML = 'pink';
}
document.getElementById("a44").addEventListener("click",click7);
function click8()
{
document.getElementById('section').innerHTML = 'lavender';

}
document.getElementById("a1").addEventListener("click",click);
function click()
{

document.getElementById("a22").innerHTML="Home";
document.getElementById("home").style.filter="invert(100%)";
document.getElementById("mywork").style.filter="invert(0%)";
document.getElementById("review").style.filter="invert(0%)";
document.getElementById("completed").style.filter="invert(0%)";

document.getElementById("t1").style.display= "block";
document.getElementById("a1").style.color= "white";
document.getElementById("a2").style.color= "black";
document.getElementById("a3").style.color= "black";
document.getElementById("a4").style.color= "black";
document.getElementById("t2").style.display= "none";
document.getElementById("t3").style.display= "none";
document.getElementById("t4").style.display= "none";
}
function click77()
{
document.getElementById("section1").style.display= "block";
}*/
