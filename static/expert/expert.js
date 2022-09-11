

function accept(pr_id) {
    
  
   $.ajax({
    url: "/expert/accept/",
    type: 'GET',// This is the default though, you don't actually need to always mention it
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
preventDefault();
}

function project_close(event,pr_id) {
    
  
   $.ajax({
    url: '/expert/project_close/',
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
function module_page(event,pr_id) {
    
  
   $.ajax({
    url: "/expert/ex_new_modules/",
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
function project_download(event,pr_id) {
    
  
   $.ajax({
    url: '/expert/download_request/',
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
function approve_module(pr_id) {
    
  
   $.ajax({
    url: '/expert/approve_module/',
    type: 'GET',// This is the default though, you don't actually need to always mention it
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
preventDefault();
}
function module_suggestion(event,md_id) {

  
   $.ajax({
    url: '/expert/module_suggestion/',
    type: 'GET',
    data:{
        'id':md_id
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
function des() {
    document.getElementById("section").innerHTML=document.getElementById("description").value;
}