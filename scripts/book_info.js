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


//     async function add_comment(context){
//         if (event) {
//             event.preventDefault();
//             event.stopPropagation();
//             }
        
//             const urlParams = new URLSearchParams(window.location.search);
//             const bookId = urlParams.get('id');
//             const input = document.getElementById("comment").value;
        
//             const response = await axios.post(
//             `http://127.0.0.1:8000/comment?Reader_id=${account_id}&Book_id=${bookId}&comment=${input}`
//             );
        
//             console.log(response.data);
//     }

// });