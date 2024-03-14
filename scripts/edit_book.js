function displayBookEditAndNavigate(bookName) {
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
            console.log("book_namee",bookName)
            window.location.href = "edit_book.html";
        })
        .catch(error => {
            console.error('Error fetching book information:', error);
        });
}

document.addEventListener('DOMContentLoaded', async function () {
    const editBookForm = document.getElementById('editBookForm');
    const responseDiv = document.getElementById('response');
    const old_genre = document.getElementById('old_genre');
    const old_name = document.getElementById('old_name');
    const old_pseudonym = document.getElementById('old_pseudonym');
    const old_age_restricted = document.getElementById('old_age_restricted');
    const old_status = document.getElementById('old_status');
    const old_age_restricted = document.getElementById('old_age_restricted');
    const old_age_restricted = document.getElementById('old_age_restricted');


    try {
        const book_old_name = localStorage.getItem('book_name_edit_last')
        const response = await fetch(`/book/info/${book_old_name}`);
        if (!response.ok) {
            throw new Error('Failed to fetch book information');
        }
        const bookData = await response.json();

        // Populate form fields with existing book information
        old_name.value = bookData.name;
        old_genre.value = bookData.genre;
        old_pseudonym.value = bookData.pseudonym;
        old_status.value = bookData.status;
        old_age_restricted.value = bookData.age_restricted;
        old_prologue.value = bookData.prologue;
        old_age_restricted.value = bookData.date_time;
        old_age_restricted.value = bookData.age_restricted;

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

                go_to_pre_edit_book();
            } catch (error) {
                console.error('Error editing book:', error);
            }
        });
    }
});
function go_to_pre_edit_book() {
    const book_name = localStorage.getItem("book_name_last")
    // const chapterId = "Shin_chan-1"
    displayPreEditBookAndNavigate(book_name)
}

