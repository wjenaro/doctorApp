$(document).ready(function(){
    $("#search").click(function(event) {
        var spec=$("#spec").val();
        var address=$("#address").val();
        if(spec==="" && address===""){
            event.preventDefault();
        // Display an error message (you can customize this part)
        $("#message").text("Please Enter at least one parameter");
        }
      });
 
  });

  