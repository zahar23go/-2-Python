"""
Модели данных для работы с базой данных
"""
from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime, timezone


class Student(Base):
    """
    Модель студента
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Student(name='{self.name}', email='{self.email}')>"

    def to_dict(self):
        """Преобразует объект в словарь"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
            'deleted_at': self.deleted_at
        }
