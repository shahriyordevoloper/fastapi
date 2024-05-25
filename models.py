from sqlalchemy import Boolean ,Column, ForeignKey,Integer,String
from datebase import Base

class Quetions(Base):
    __tablename__ = 'quetions'
    id = Column(Integer, primary_key=True, index=True)
    quetion_text= Column(String, index=True)
    
class Choices(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True, index=True)
    choices_text= Column(String, index=True)
    is_correct = Column(Boolean ,default=False)
    quetion_id = Column(Integer, ForeignKey("quetions.id"))