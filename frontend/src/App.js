import { useEffect, useState } from "react";
import API from "./api";
import "./App.css";

function App() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      setLoading(true);
      const res = await API.get("/books");
      setBooks(res.data);
      setError(null);
    } catch (err) {
      console.error("Fetch error:", err);
      setError("Unable to connect to the server. Please make sure the backend is running at http://localhost:8000");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1 className="title">BOOK HUB</h1>
        <p className="subtitle">Discover and share your favorite reads</p>
      </header>

      {error && (
        <div className="error-state">
          {error}
          <button 
            onClick={fetchBooks}
            style={{ 
              display: 'block', 
              margin: '1rem auto 0', 
              background: 'rgba(255,255,255,0.1)', 
              border: 'none', 
              color: 'white', 
              padding: '0.5rem 1rem', 
              borderRadius: '0.5rem', 
              cursor: 'pointer' 
            }}
          >
            Retry Connection
          </button>
        </div>
      )}

      {loading ? (
        <div className="loading-state">
          <p>Loading your library...</p>
        </div>
      ) : (
        <div className="book-grid">
          {books.length > 0 ? (
            books.map((book) => (
              <div key={book.id} className="book-card">
                <div className="book-author">{book.author}</div>
                <h3 className="book-title">{book.title}</h3>
                <p className="book-description">
                  {book.description || "No description available for this book. Start reading to find out more!"}
                </p>
                <div style={{ marginTop: 'auto', display: 'flex', justifyContent: 'flex-end' }}>
                  <button style={{ 
                    background: 'var(--primary)', 
                    color: 'white', 
                    border: 'none', 
                    padding: '0.5rem 1.25rem', 
                    borderRadius: '0.75rem', 
                    fontWeight: '600',
                    cursor: 'pointer'
                  }}>
                    Read More
                  </button>
                </div>
              </div>
            ))
          ) : (
            <div className="empty-state">
              <h3>No books found</h3>
              <p style={{ color: 'var(--text-secondary)' }}>Your library is currently empty. Add some books to get started!</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;