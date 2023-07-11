      // Get the section element
      //const section = document.querySelector('#searchresults');

      //function displaySection(event) {
        // Prevent the default form submission behavior
        //event.preventDefault();
       // alert("Good");

        // Check if at least one input field is filled
        //const spec = document.querySelector('#spec');
        //const address=document.querySelectorAll("#address");
       // if (spec.value.trim() !== '' || address.value.trim() !=='') {
          // Display the section by removing the "hidden" class
         // alert("good");
          //section.classList.remove('hidden');
       // }
    //  }
    document.getElementById("search").addEventListener("click", function(event) {
      var specification = document.getElementById("spec").value;
      var address = document.getElementById("address").value;
  
      if (specification.trim() === "" || address.trim() === "") {
        event.preventDefault(); // Prevent form submission
        
        alert("Please fill in all fields."); // Display alert message
      }
    });
  
  