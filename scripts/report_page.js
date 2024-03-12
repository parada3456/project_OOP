document.addEventListener('DOMContentLoaded', function() {
    const reportForm = document.getElementById('reportForm');
    const reportResponse = document.getElementById('report_response');
    localStorage

    if (reportForm) {
        reportForm.addEventListener('submit', async function(event) {
            event.preventDefault();

            try {
                const formData = new FormData(this);
                const jsonData = Object.fromEntries(formData); // Convert FormData to JSON object
                const username = localStorage.getItem('login_username');
                jsonData.username = username;
                const jsonDataString = JSON.stringify(jsonData);
                console.log(jsonDataString)

                const response = await fetch(`/report/${jsonData.book_name}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: jsonDataString
                });

                if (!response.ok) {
                    throw new Error('Failed to submit report');
                }

                const data = await response.json();
                console.log("Submitted report data:", data);

                if (reportResponse) {
                    reportResponse.innerText = JSON.stringify(data);
                }

                showComment(jsonData.book_name);
            } catch (error) {
                console.error('Error submitting report:', error);
            }
        });
    }
});
