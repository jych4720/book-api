from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    },
    {
        'id': 6,
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'publication_year': 1851,
        'genre': 'Adventure Fiction'
    },
    {
        'id': 7,
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'publication_year': 1951,
        'genre': 'Literary Fiction'
    }
]

@app.route('/')
def home():
    return '''
        <html>
            <head><title>Book API</title></head>
            <body>
                <h1>Welcome to the Book API!</h1>
                <p>Click below to request the books in JSON format:</p>
                <a href="/api/books">Request Books</a>
            </body>
        </html>
    '''

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
