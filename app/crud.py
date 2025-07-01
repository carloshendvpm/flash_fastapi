from sqlalchemy.orm import Session

from . import models, schemas

def get_deck(db: Session, deck_id: int):
    return db.query(models.Deck).filter(models.Deck.id == deck_id).first()

def get_decks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Deck).offset(skip).limit(limit).all()

def create_deck(db: Session, deck: schemas.DeckCreate):
    db_deck = models.Deck(name=deck.name)
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck

def get_flashcards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Flashcard).offset(skip).limit(limit).all()

def create_flashcard(db: Session, flashcard: schemas.FlashcardCreate, deck_id: int):
    db_flashcard = models.Flashcard(**flashcard.model_dump(), deck_id=deck_id)
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard