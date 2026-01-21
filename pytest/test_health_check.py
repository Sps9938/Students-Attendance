import requests

def test_health_check():
    url = "http://localhost:4000/api/v1/health/ping"  # Update port if needed
    response = requests.get(url)
    assert response.status_code == 200
    assert "OK" in response.json().get("message", "")
