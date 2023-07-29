$(document).ready(function(){
    $("#search").click(function(event) {
        var spec=$("#spec").val();
        var address=$("#address").val();
        if(spec==="" && address===""){
            event.preventDefault();
        // Display an error message (you can customize this part)
        alert("Please fill in at least one field.");
        }
      });
 
  });