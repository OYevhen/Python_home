import pytest
from database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()