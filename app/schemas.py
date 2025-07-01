from pydantic import BaseModel
from typing import List, Optional

class FlashcardBase(BaseModel):
    question: str
    answer: str

class FlashcardCreate(FlashcardBase):
    pass

class Flashcard(FlashcardBase):
    id: int
    deck_id: int

    model_config = {"from_attributes": True}

class DeckBase(BaseModel):
    name: str

class DeckCreate(DeckBase):
    pass

class Deck(DeckBase):
    id: int
    flashcards: List[Flashcard] = []

    model_config = {"from_attributes": True}
