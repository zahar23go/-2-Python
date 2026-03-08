"""
Тесты для модели Subject
"""
from models_test import Subject


class TestSubject:
    """Тесты CRUD операций для предметов"""

    def test_create_subject(self, db_session):
        """Тест создания предмета"""
        subject = Subject(
            name="Математика",
            hours=120,
            department="Точные науки"
        )
        db_session.add(subject)
        db_session.commit()

        assert subject.id is not None
        saved = db_session.get(Subject, subject.id)
        assert saved.name == "Математика"
        assert saved.hours == 120
        assert saved.department == "Точные науки"

        db_session.delete(saved)
        db_session.commit()

    def test_update_subject(self, db_session):
        """Тест обновления предмета"""
        subject = Subject(
            name="Физика",
            hours=100,
            department="Науки"
        )
        db_session.add(subject)
        db_session.commit()

        subject.hours = 140
        subject.department = "Точные науки"
        db_session.commit()

        updated = db_session.get(Subject, subject.id)
        assert updated.hours == 140
        assert updated.department == "Точные науки"

        db_session.delete(updated)
        db_session.commit()

    def test_delete_subject(self, db_session):
        """Тест удаления предмета"""
        subject = Subject(
            name="Химия",
            hours=80,
            department="Науки"
        )
        db_session.add(subject)
        db_session.commit()
        subject_id = subject.id

        db_session.delete(subject)
        db_session.commit()

        deleted = db_session.get(Subject, subject_id)
        assert deleted is None
