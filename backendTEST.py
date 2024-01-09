import requests

def test_api():
    base_url = "https://flights-api.buraky.workers.dev/"

    response = requests.get(base_url)
    assert response.status_code == 200, f"Başarısız HTTP isteği: {response.status_code}"

    assert "Content-Type" in response.headers, "Content-Type header bulunamadı"
    assert response.headers["Content-Type"] == "application/json", "Content-Type değeri beklenen formatta değil"

    json_response = response.json()
    assert "data" in json_response, "Beklenen 'data' anahtarı bulunamadı"

    flights = json_response["data"]
    for flight in flights:
        assert "id" in flight, "Beklenen 'id' anahtarı bulunamadı"
        assert "from" in flight, "Beklenen 'from' anahtarı bulunamadı"
        assert "to" in flight, "Beklenen 'to' anahtarı bulunamadı"
        assert "date" in flight, "Beklenen 'date' anahtarı bulunamadı"

        assert isinstance(flight["id"], int), "ID integer olmalı"
        assert isinstance(flight["from"], str), "From string olmalı"
        assert isinstance(flight["to"], str), "To string olmalı"
        assert isinstance(flight["date"], str), "Date string olmalı"

    print("Tests completed successfully")

test_api()


