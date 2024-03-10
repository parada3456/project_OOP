async function getBookInfo() {
    const bookName = document.getElementById("bookNameInput").value;
    const response = await fetch(`/book-info?book_name=${bookName}`);
    const data = await response.json();

    const bookInfoElement = document.getElementById("bookInfo");
    if (data.error) {
        bookInfoElement.textContent = data.error;
    } else {
        bookInfoElement.innerHTML = `
            <p><strong>Name:</strong> ${data.name}</p>
            <p><strong>Author:</strong> ${data.author}</p>
            <p><strong>Genre:</strong> ${data.genre}</p>
        `;
    }
}
