import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def post(client, expression, mode="deg"):
    return client.post("/calculate", json={"expression": expression, "angle_mode": mode})


def test_basic_math(client):
    response = post(client, "2+3*4")
    assert response.status_code == 200
    assert response.get_json() == {"result": 14}


def test_float_noise_is_removed(client):
    assert post(client, "sin(30)").get_json() == {"result": 0.5}


def test_angle_mode_is_used(client):
    assert post(client, "sin(pi/2)", "rad").get_json() == {"result": 1}


def test_calculator_error_returns_400(client):
    response = post(client, "1/0")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_missing_body_returns_400(client):
    assert client.post("/calculate").status_code == 400


def test_too_long_expression_is_rejected(client):
    assert post(client, "1+" * 150 + "1").status_code == 400


def test_huge_result_is_rejected(client):
    assert post(client, "9^9^9").status_code == 400


def test_deep_nesting_does_not_crash(client):
    response = post(client, "(" * 190 + "1" + ")" * 190)
    assert response.status_code in (200, 400)


def test_home_page_loads(client):
    assert client.get("/").status_code == 200


def test_static_files_are_served(client):
    assert client.get("/static/style.css").status_code == 200
    assert client.get("/static/script.js").status_code == 200
