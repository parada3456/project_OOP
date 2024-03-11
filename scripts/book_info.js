// script.js

function displayBookInfoAndNavigate(bookName) {
    fetch(`/book/${bookName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            window.location.href = "book_info.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}


document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('commentForm');
    const commentResponse = document.getElementById('comment_response');

    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            const jsonData = {};
            formData.forEach((value, key) => { jsonData[key] = value });
            const jsonDataString = JSON.stringify(jsonData);

            fetch(`/comment/${jsonData.chapter_id}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonDataString
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to submit comment');
                }
                return response.json();
            })
            .then(data => {
                console.log("Submitted comment data:", data);
                if (commentResponse) {
                    commentResponse.innerText = JSON.stringify(data);
                }
                showComment(jsonData.chapter_id);
            })
            .catch(error => {
                console.error('Error submitting comment:', error);
            });
        });
    }

    function showComment(chapter_id) {
        fetch(`/chapter/${chapter_id}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to fetch comments for chapter ${chapter_id}`);
                }
                return response.json();
            })
            .then(data => {
                console.log(`Received comments for chapter ${chapter_id}:`, data);
                
                // Store the comment data in sessionStorage
                sessionStorage.setItem('commentData', JSON.stringify(data));
                
                
            })
            .catch(error => {
                console.error('Error fetching comments:', error);
            });
    }
});