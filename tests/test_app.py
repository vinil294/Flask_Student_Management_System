import pytest

import app as student_app
import database


@pytest.fixture()
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "students_test.db"
    monkeypatch.setattr(database, "DB_PATH", str(test_db))
    database.create_database()
    student_app.app.config.update(TESTING=True)
    with student_app.app.test_client() as test_client:
        yield test_client


def test_main_pages_load(client):
    for route in ("/", "/dashboard", "/register", "/view", "/search"):
        response = client.get(route)
        assert response.status_code == 200, route


def test_student_database_crud(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "crud.db"))
    database.create_database()

    database.insert_student("VINIL", "AIML001", "AIML", 8.5)
    student = database.search_student("AIML001")
    assert student is not None
    assert student[1] == "VINIL"
    assert student[2] == "AIML001"
    assert database.total_students() == 1

    database.update_student(student[0], "VINIL REDDY", "AIML001", "AIML", 9.0)
    updated = database.search_student("AIML001")
    assert updated[1] == "VINIL REDDY"
    assert updated[4] == 9.0

    assert database.delete_student("AIML001") == 1
    assert database.search_student("AIML001") is None
    assert database.total_students() == 0
