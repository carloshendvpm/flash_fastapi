from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return { "message": "Server is up and running!"}

@app.post("/decks/", response_model=schemas.Deck)
def create_deck(deck: schemas.DeckCreate, db: Session = Depends(get_db)):
    return crud.create_deck(db=db, deck=deck)


@app.get("/decks/", response_model=List[schemas.Deck])
def read_decks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    decks = crud.get_decks(db, skip=skip, limit=limit)
    return decks


@app.get("/decks/{deck_id}", response_model=schemas.Deck)
def read_deck(deck_id: int, db: Session = Depends(get_db)):
    db_deck = crud.get_deck(db, deck_id=deck_id)
    if db_deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return db_deck


@app.post("/decks/{deck_id}/flashcards/", response_model=schemas.Flashcard)
def create_flashcard_for_deck(
    deck_id: int, flashcard: schemas.FlashcardCreate, db: Session = Depends(get_db)
):
    return crud.create_flashcard(db=db, flashcard=flashcard, deck_id=deck_id)


@app.get("/flashcards/", response_model=List[schemas.Flashcard])
def read_flashcards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    flashcards = crud.get_flashcards(db, skip=skip, limit=limit)
    return flashcards