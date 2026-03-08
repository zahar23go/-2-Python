"""
Дополнительные модели для тестирования
"""
from sqlalchemy import Column, Integer, String
from database import Base


class Subject(Base):
    """Модель предмета для тестов"""
    __tablename__ = 'test_subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    hours = Column(Integer)
    department = Column(String(50))

    def __repr__(self):
        return f"<Subject(name='{self.name}', hours={self.hours})>"
