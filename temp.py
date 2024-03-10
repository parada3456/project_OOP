from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mock database of books
books = [
    {"name": "Book 1", "author": "Author 1", "genre": "Genre 1", "summary": "Summary 1"},
    {"name": "Book 2", "author": "Author 2", "genre": "Genre 2", "summary": "Summary 2"},
    # Add more books as needed
]

# Route to serve HTML page
@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    with open("Templates/temp2.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# Endpoint to get book information
@app.get("/book/{book_name}")
async def get_book_info(book_name: str):
    for book in books:
        if book["name"] == book_name:
            return book
    return {"message": "Book not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
