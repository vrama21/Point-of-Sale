function showOptionalWindow(argument) {
    var toggle  = document.getElementById("customer_status_toggle");
    var content = document.getElementById("customer-info-optional-container");
    
    toggle.addEventListener("click", function() {
        content.classList.toggle("show");
    });
}