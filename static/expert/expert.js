function accept(pr_id) {

    alert(pr_id);
  
   $.ajax({
    url: '/accept/',
    type: 'GET',// This is the default though, you don't actually need to always mention it
    data:{
        'id':pr_id
    },
    success: function(response) {
        
        var instance = JSON.parse(response["rs"]);
        alert(instance);
    
    },
    failure: function(response) { 
        alert('Got an error dude');
    }
});
}
function project_close(event,pr_id) {

    alert(pr_id);
  
   $.ajax({
    url: '/project_close/',
    type: 'GET',
    data:{
        'id':pr_id
    },
    success: function(response) {
        $("html").html(response);
    },
    failure: function(response) { 
        alert('Got an error dude');
    }
});
event.preventDefault();
} 
    
    
        
    /*
    function func4(event) {
                 event.stopPropagation();
                 document.getElementById("section").innerHTML=`<div id="s1">
    <h2>Modules</h2>
    <a href="">hello</a>
    <a href="www.google.com" onclick="javascript:test(this);" id="first">click</a>
    <button onclick="document.location='{% url 'expert:module_creation' %}'">HTML Tutorial</button>

    <a href=""  id="create"><div id="progress"><div id="progress1">create module</div></div></a>
    <table   style="position: relative;left: -100px;top: -100px;border-spacing:60px;">
        
    {%for getdata in Modules %}
    <td>
    <div id="b" onclick="alert('div');">
    <a href="" onclick="func3(event)" id="progressm"><div id="close"><div id="close1">80%</div></div></a>
    <a href="" onclick="func5(event)" id="developer"><div id="c"><div id="c1">D</div></div></a>
    <a href="" onclick="func6(event)" id="edit"><div id="progress"><div id="progress1">EDIT</div></div></a>
    <sec  id="f">{{getdata.md_name}}</sec>
    <p id="d">{{getdata.md_description}}</p>
    </div>
    </td>
    {% endfor %}
    
    </table>
    </div>
    
    
    <div id="s2">
    <h2>Review</h2>
    <table  style="position: relative;left: -100px;top: -100px;border-spacing:60px;">
    {%for getdata in Modules_review %}
    <td>
    <div id="b" onclick="alert('div');">
    <a href="" onclick="func3(event);" id="suggestion"><div id="close"><div id="close1">SUGGESTION</div></div></a>
    <a href="" onclick="func5(event)" id="developer"><div id="c"><div id="c1">D</div></div></a>
    <a href="" onclick="func9(event)" id="downm"><img src="{% static '/images/Download.svg'%}" id="download1"></a>
    <a href="" onclick="func6(event)" id="edit"><div id="progress"><div id="progress1">ACCEPT</div></div></a>
    <sec  id="f">{{getdata.md_name}}</sec>
    <p id="d">{{getdata.md_description}}</p>
    </div>
    {% endfor %}
    
    </table>
    </div>
    
    <div id="s3" >
    <h2>Completed</h2>
    <table   style="position: relative;left: -100px;top: -100px;border-spacing:60px;">
    {%for getdata in Modules_completed %}
    <td>
    <div id="b" onclick="alert('div');">
    <a href="" onclick="func1(event)" id="reopen"><div id="accept"><div id="accept1">REOPEN</div></div></a>
    <a href="" onclick="func9(event)" id="downm"><img src="{% static '/images/Download.svg'%}" id="download1"></a>
    <a href="" onclick="func2(event)" id="developer"><div id="c"><div id="c1">D</div></div></a>
    <sec  id="f">{{getdata.md_name}}</sec>
    <p id="d">{{getdata.md_description}}</p>
    </div>
    {% endfor %}
    </table>`;
            alert("upload");
              
            }
            function func2(event) {
                 event.stopPropagation();                             
                 alert("progress");
                 
            }
             
            function accept(pr_id) {

                alert(pr_id);
              
               $.ajax({
                url: '/accept/',
                type: 'GET',// This is the default though, you don't actually need to always mention it
                data:{
                    'id':pr_id
                },
                success: function(response) {
                    
                    var instance = JSON.parse(response["rs"]);
                    alert(instance);
                
                },
                failure: function(response) { 
                    alert('Got an error dude');
                }
            });
            event.stopPropagation();

            
                
                 
                 
               
              
            }
            function func3() {
                 event.stopPropagation();
                 document.location.replace("{% url 'expert:module_creation' %}");
             
                 alert("project details");
              
            }
    /*popup*/
    
    
    /*layout
    function button1() {
        alert(8);
        
        
      }
      
    function click()
    {
    document.getElementById("a22").innerHTML="Home";   
    document.getElementById("home").style.filter="invert(100%)";
    document.getElementById("mywork").style.filter="invert(0%)";
    document.getElementById("review").style.filter="invert(100%)";
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
    document.getElementById("a1").addEventListener("click",click);
    
    function click1()
    {
    document.getElementById("a22").innerHTML="My works";    
    document.getElementById("mywork").style.filter="invert(100%)";
    document.getElementById("home").style.filter="invert(0%)";
    document.getElementById("review").style.filter="invert(100%)";
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
    document.getElementById("review").style.filter="invert(0%)";
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
    document.getElementById("a22").innerHTML="Completed";     
    document.getElementById("home").style.filter="invert(0%)";
    document.getElementById("mywork").style.filter="invert(0%)";
    document.getElementById("review").style.filter="invert(100%)";
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
    alert(6);
    event.preventDefault();

    }
    document.getElementById("a44").addEventListener("click",click7);
    function click8()
    {
    document.getElementById('section').innerHTML = 'lavender';
    
    }*/
    