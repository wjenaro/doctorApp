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
    function alertOnButtonClick() {
      alert("You clicked the button!");
    }
    
    // Get the button element.
    const button = document.getElementById("search");
    
    // When the button is clicked, call the alertOnButtonClick() function.
    button.addEventListener("click", alertOnButtonClick);