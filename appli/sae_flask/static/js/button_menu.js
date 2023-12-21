function myFunction() {
     document.getElementById("myDropdown").classList.toggle("show");
} 

document.addEventListener('DOMContentLoaded', function () {
     var toggleChecker = document.getElementById('toggleChecker');
     var dropdown = document.getElementById('myDropdown');
 
     document.addEventListener('click', function (event) {
         var isClickInsideMenu = dropdown.contains(event.target);
         var isClickOnToggleChecker = event.target === toggleChecker;
 
         if (!isClickInsideMenu && !isClickOnToggleChecker && toggleChecker.checked) {
             toggleChecker.checked = false; // Fermer le menu si le clic est en dehors du menu
             dropdown.classList.remove('show'); // Supprimer la classe "show"
         }
     });
 });
 