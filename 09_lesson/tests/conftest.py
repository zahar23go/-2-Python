"""
Фикстуры для pytest
"""
import pytest
from database import SessionLocal


@pytest.fixture
def db_session():
    """Фикстура для создания сессии БД"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
