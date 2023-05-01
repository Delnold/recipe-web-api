import json


def test_create_user(client):
    data = {"login":"testuser","email":"testuser@nofoobar.com","hashed_password":"testing"}
    response = client.post("/users/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@nofoobar.com"