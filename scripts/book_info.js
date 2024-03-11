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
    const commentForm = document.getElementById('commentForm');
    const commentResponse = document.getElementById('comment_response');

    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
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
                    if (commentResponse) {
                        commentResponse.innerText = JSON.stringify(data);
                    }
                    console.log(jsonData.chapter_id)
                    showComment(jsonData.chapter_id)
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    }

    function showComment(chapter_id) {
        console.log(`Fetching comments for chapter ${chapter_id}`);
        fetch(`/chapter/${chapter_id}`)
            .then(response => {
                console.log('Response:', response);
                if (!response.ok) {
                    throw new Error(`Response returned with status ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Received comment data:', data);
                if (data) {
                    sessionStorage.setItem('commentData', JSON.stringify(data));
                } else {
                    console.error('Received comment data is empty or undefined.');
                }
            })
            .catch(error => {
                console.error('Error fetching comments:', error.message);
            });
    }
    
    
});
