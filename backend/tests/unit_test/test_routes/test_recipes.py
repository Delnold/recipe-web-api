import json


def test_create_recipe(client):
    data = {
        "name": "string",
        "description": "string",
        "instructions": "string",
        "prep_time": 0,
        "cook_time": 0,
        "total_time": 0,
        "servings": "string"
    }
    response = client.post("/recipes/create-recipe/", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["name"] == "string"
    assert response.json()["prep_time"] == 0
