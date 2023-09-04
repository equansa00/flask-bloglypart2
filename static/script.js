document.addEventListener("DOMContentLoaded", function() {
    // Sample function to show an alert when a button is clicked
    let buttons = document.querySelectorAll(".button");
    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            alert("Button clicked!");
        });
    });
});
