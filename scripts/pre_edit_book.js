document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addChapterButton').addEventListener('click', function() {
        window.location.href = "create_chapter.html"; 
    });

    function displayPreEditChapterAndNavigate(bookName) {
        console.log("start");

        fetch(`/book/${bookName}`)
            .then(response => response.json())
            .then(data => {
                console.log("oooo")
                sessionStorage.setItem('PreEditChapter', JSON.stringify(data));

                const PreEditChapter = JSON.parse(sessionStorage.getItem('PreEditChapter'));

                console.log("Retrieved book information:", data);

                if (PreEditChapter && PreEditChapter.genre && PreEditChapter.name && PreEditChapter.pseudonym && PreEditChapter.prologue && PreEditChapter.writer_name && bookInfo.date_time) {

                    document.getElementById('genre').textContent = PreEditChapter.genre;
                    document.getElementById('bookName').textContent = PreEditChapter.name;
                    document.getElementById('prologueInfo').textContent = PreEditChapter.prologue;
                    document.getElementById('prologueDisplay').textContent = PreEditChapter.prologue;
                    document.getElementById('pseudonymInfo').textContent = PreEditChapter.pseudonym;
                    document.getElementById('pseudonymDisplay').textContent = PreEditChapter.pseudonym;
                    document.getElementById('writer_username').textContent = PreEditChapter.writer_name;
                    document.getElementById('date_time').textContent = PreEditChapter.date_time;
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});
