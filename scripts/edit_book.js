function displayBookInfoAndNavigate(bookName) {
    console.log("start");
    fetch(`/book/${bookName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch book information');
            }
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('bookInfo', JSON.stringify(data));
            localStorage.setItem('book_name_last', bookName);
            console.log(localStorage.getItem('book_name_last'));
            console.log("book_namee",bookName)
            window.location.href = "book_info.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}

document.addEventListener('DOMContentLoaded', async function () {
    const editBookForm = document.getElementById('editBookForm');
    const responseDiv = document.getElementById('response');
    const bookIdInput = document.getElementById('book_id');
    const bookNumberInput = document.getElementById('book_number');
    const nameInput = document.getElementById('name');
    const contextInput = document.getElementById('context');
    const costInput = document.getElementById('cost');

    try {
        const bookId = 'Shin_chan-1'; // Provide the book ID you want to edit
        const response = await fetch(`/book/info/${bookId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch book information');
        }
        const bookData = await response.json();

        // Populate form fields with existing book information
        bookIdInput.value = bookData.book_id;
        nameInput.value = bookData.name;
        bookNumberInput.value = bookData.book_number;
        contextInput.value = bookData.context;
        costInput.value = bookData.price;
    } catch (error) {
        console.error('Error fetching book information:', error);
    }

    if (editBookForm) {
        editBookForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            try {
                const formData = new FormData(this);
                const jsonData = {};
                formData.forEach((value, key) => {
                    jsonData[key] = value;
                });

                const response = await fetch('/edit_book', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonData)
                });

                if (!response.ok) {
                    throw new Error('Failed to edit book');
                }

                const data = await response.json();
                if (response) {
                    responseDiv.innerText = data.message;
                }

                go_to_book_info();
            } catch (error) {
                console.error('Error editing book:', error);
            }
        });
    }
});

function go_to_book_info() {
    const bookId = "Shin_chan-1"; // Provide the book ID to navigate to
    NavigateToBookInfo(bookId);
}
