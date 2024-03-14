// script.js
// username_use = localStorage.getItem("username")
var username_use = "Pinttttt";
function check_writer(book_name){
    fetch(`/check_writer/${username_use}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch check writer ');
            }
            return response.json();
        })
        .then(data => {
            console.log(data)
            console.log("data.message: ",data.role);
            if (data.role == "writer"){
                displayPreEditBookAndNavigate(book_name);
            }
            else if (data.role == "reader"){
                console.log("navigate_to_not_writer_page");
                navigate_to_not_writer_page();
            }
        })
        .catch(error => {
            console.error('Error fetching check writer :', error);
        });
}
function navigate_to_not_writer_page(){
    console.log("go to not_writer.html");
    window.location.href = "not_writer.html";
}
// Function to display book information and navigate
function displayPreEditBookAndNavigate(bookName) {
        console.log("start");
        console.log("bookName : ",bookName)
        fetch(`/book/${bookName}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to fetch book information');
                }
                return response.json();
            })
            .then(data => {
                sessionStorage.setItem('bookInfo', JSON.stringify(data));
                localStorage.setItem('book_name_edit_last', bookName);
                console.log(localStorage.getItem('book_name_edit_last'));
                console.log("book_namee",bookName);
                window.location.href = "pre_edit_book.html";
            })
            .catch(error => {
                console.error('Error fetching book information:', error);
            });
}

function showChapter(book_name) {
    console.log(`Fetching chapter for book ${book_name}...`);
    fetch(`/book/chapter/${book_name}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Failed to fetch chapter for chapter ${book_name}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(`Received chapter for book ${book_name}:`, data);
            sessionStorage.setItem('chapterData', JSON.stringify(data));
        })
        .catch(error => {
            console.error('Error fetching chapters:', error);
        });
}

function back_to_book_info() {
    console.log("back to book")
    displayBookInfoAndNavigate(localStorage.getItem('book_name_edit_last'))
}



document.addEventListener('DOMContentLoaded', function () {
    const bookName = localStorage.getItem('book_name_edit_last');
    showChapter(bookName);

});
