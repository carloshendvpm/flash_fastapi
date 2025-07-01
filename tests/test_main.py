from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_create_deck(client):
    response = client.post("/decks/", json={"name": "Test Deck"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Deck"

def test_read_decks(client):
    response = client.get("/decks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_flashcard_for_deck(client):
    deck_response = client.post("/decks/", json={"name": "Another Deck"})
    deck_id = deck_response.json()["id"]
    response = client.post(
        f"/decks/{deck_id}/flashcards/",
        json={"question": "What is FastAPI?", "answer": "A web framework"},
    )
    assert response.status_code == 200
    assert response.json()["question"] == "What is FastAPI?"