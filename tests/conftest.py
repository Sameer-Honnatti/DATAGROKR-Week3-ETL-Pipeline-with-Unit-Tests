import pytest

@pytest.fixture
def sample_users():
    return [
        {
            "id": 1,
            "name": "John Doe",
            "username": "johnd",
            "email": "john@example.com",
            "address": {
                "city": "Bengaluru"
            },
            "company": {
                "name": "Example Corp"
            }
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "username": "janes",
            "email": "jane@example.com",
            "address": {
                "city": "Mysore"
            },
            "company": {
                "name": "Sample Ltd"
            }
        },
        {
            "id": 3,
            "name": "Alex Kumar",
            "username": "alexk",
            "email": "alex@example.com",
            "address": {
                "city": "Bengaluru"
            },
            "company": {
                "name": "Tech Solutions"
            }
        }
    ]