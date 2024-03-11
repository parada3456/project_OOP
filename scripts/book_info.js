// script.js
// document.addEventListener('DOMContentLoaded', function() {
// script.js

function displayBookInfoAndNavigate(bookName) {
    // Fetch book information asynchronously
    fetch(`/book/${bookName}`)
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            // Store book information in sessionStorage
            sessionStorage.setItem('bookInfo', JSON.stringify(data));

            // Navigate to book_info.html
            window.location.href = "book_info.html";
            
        })
        .catch(error => {
            console.error('Error:', error);
        });

}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('commentForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Get form data
        const formData = new FormData(this);
        
        // Convert form data to JSON object
        const jsonData = {};
        formData.forEach((value, key) => { jsonData[key] = value });
        const jsonDataString = JSON.stringify(jsonData);
        
        // Send POST request to FastAPI server
        fetch(`/comment/${jsonData.chapter_id}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonDataString
        })
        .then(response => response.json())
        .then(data => {
            // Display response from server
            console.log(JSON.stringify(data))
            document.getElementById('comment_response').innerText = JSON.stringify(data);
            show_comment(jsonData.chapter_id)
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

function show_comment(chapter_id){
    fetch(`/chapter/comment`)
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            // Store book information in sessionStorage
            sessionStorage.setItem('comment', JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
