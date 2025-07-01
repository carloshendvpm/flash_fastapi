# Flashcard API

This is a simple Flashcard API built with FastAPI.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/carloshendvpm/flash_fastapi.git
    cd flash_fastapi
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

*   `GET /`: Server status.
*   `POST /decks/`: Create a new deck.
*   `GET /decks/`: Get a list of all decks.
*   `GET /decks/{deck_id}`: Get a specific deck by ID.
*   `POST /decks/{deck_id}/flashcards/`: Create a new flashcard for a specific deck.
*   `GET /flashcards/`: Get a list of all flashcards.
