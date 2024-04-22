document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the clear button
    document.getElementById('clearButton').addEventListener('click', function() {
        // Send an asynchronous request to the /clear route
        fetch('/clear', {
            method: 'POST'
        }).then(function(response) {
            // Reload the page after clearing inputs
            location.reload();
        });
    });
});