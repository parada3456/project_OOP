function NavigateToChapterInfo(chapter_id) {
    console.log("start");
    fetch(`/chapter/info/${chapter_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch chapter information');
            }
            console.log("receive response")
            return response.json();
        })
        .then(data => {
            sessionStorage.setItem('chapterInfo', JSON.stringify(data)); // Storing chapter info
            console.log("chapter data: ", data);
            // window.location.href = "reading_chapter.html"; // Redirecting to another page
        })
        .catch(error => {
            console.error('Error fetching chapter information:', error);
        });
}