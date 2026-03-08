"""
Тесты для модели Student
"""
from models import Student
from datetime import datetime, timezone


class TestStudent:
    """Тесты CRUD операций для студентов"""

    def test_create_student(self, db_session):
        """Тест создания студента"""
        student = Student(
            name="Цирулин Захар",
            email="zahar-c23@mail.ru"
        )
        db_session.add(student)
        db_session.commit()

        assert student.id is not None
        saved = db_session.get(Student, student.id)
        assert saved.name == "Цирулин Захар"
        assert saved.email == "zahar-c23@mail.ru"
        assert saved.deleted_at is None

        db_session.delete(saved)
        db_session.commit()

    def test_update_student(self, db_session):
        """Тест обновления студента"""
        student = Student(
            name="Цирулин Захар",
            email="zahar-c23@mail.ru"
        )
        db_session.add(student)
        db_session.commit()

        student.name = "Захар Цирулин"
        student.email = "zahar.updated@mail.ru"
        db_session.commit()

        updated = db_session.get(Student, student.id)
        assert updated.name == "Захар Цирулин"
        assert updated.email == "zahar.updated@mail.ru"

        db_session.delete(updated)
        db_session.commit()

    def test_delete_student(self, db_session):
        """Тест мягкого удаления"""
        student = Student(
            name="Цирулин Захар",
            email="zahar-c23@mail.ru"
        )
        db_session.add(student)
        db_session.commit()
        student_id = student.id

        student.deleted_at = datetime.now(timezone.utc)
        db_session.commit()

        deleted = db_session.get(Student, student_id)
        assert deleted.deleted_at is not None
        assert deleted.name == "Цирулин Захар"
        assert deleted.email == "zahar-c23@mail.ru"

        db_session.delete(deleted)
        db_session.commit()
