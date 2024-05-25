from fastapi import FastAPI , HTTPException, Depends
from pydantic import BaseModel
from typing import List , Annotated
import models
from datebase import engine , SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Choicebase(BaseModel):
    choice_text : str
    is_correct : bool


class Quetionbase(BaseModel):
    quetion_text : str
    choices : List[Choicebase]
    
def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/quetions/")
async def create_quetions(quetion:Quetionbase,db:db_dependency):
    db_quetion = models.Quetions(quetion_text=quetion.quetion_text)
    db.add(db_quetion)
    db.commit()
    db.refresh(db_quetion)
    for choice in quetion.choices:
        db_choices = models.Choices(choice_text=choice.choice_text , is_correct=choice.is_correct , quetion_id=db_quetion.id)
        db.add(db_quetion)
    db.commit()
    
    