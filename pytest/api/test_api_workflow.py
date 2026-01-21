import requests

BASE_URL = "http://localhost:4000/api/v1"

# Test login API

def test_login():
    payload = {
        "email": "satya256prakash@gmail.com",
        "password": "satya@99380"
    }
    response = requests.patch(f"{BASE_URL}/user/login", json=payload)
    print("Login response:", response.status_code, response.text)
    assert response.status_code == 200
    assert response.json().get("success") is True

# Test health check API

def test_health_check():
    response = requests.get(f"{BASE_URL}/health/ping")
    assert response.status_code == 200
    assert "OK" in response.json().get("message", "")

# Add more tests for class, student, attendance, dashboard APIs as needed
