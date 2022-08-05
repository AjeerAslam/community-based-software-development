function accept(pr_id) {
    $.ajax({
    url: '/accept/',
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

}
function description1(description){
    alert(description);
    //document.getElementById("section").innerHTML=description;
}
function download(pr_id) {
    $.ajax({
        url: '/accept/',
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
    
} 
