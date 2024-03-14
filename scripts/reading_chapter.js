function NavigateToChapterInfo(chapter_id) {
    console.log("start");
    fetch(`/chapter/info/${chapter_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch chapter information');
            }
            console.log("receive response");
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('chapterInfo', JSON.stringify(data)); // Storing chapter info
            console.log("chapter data: ", data);
            localStorage.setItem("chapter_id_read_last",chapter_id)

            window.location.href = "reading_chapter.html"; // Redirecting to another page
        })
        .catch(error => {
            console.error('Error fetching chapter information:', error);
        });
}


document.addEventListener('DOMContentLoaded', function () {
    const bookName = localStorage.getItem('book_name_last');
    
    const commentForm = document.getElementById('commentForm');
    const commentResponse = document.getElementById('comment_response');

    if (commentForm) {
        commentForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const formData = new FormData(this);
            const jsonData = {};
            formData.forEach((value, key) => { jsonData[key] = value });
            jsonData.chapter_id = localStorage.getItem('chapter_id_read_last')
            // jsonData.username = localStorage.getItem('username')
            jsonData.username = "Mozaza"
            console.log("new comment : ",jsonData)
            const jsonDataString = JSON.stringify(jsonData);
            
            console.log("new comment : ",jsonDataString)

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
    showChapter(bookName);
    showComment(bookName);

});

function back_to_book_info() {
    console.log("back to book")
    localStorage.removeItem("chapter_id_read_last")
    displayBookInfoAndNavigate(localStorage.getItem('book_name_last'))
}