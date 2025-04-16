import pytest
from fastapi.testclient import TestClient
from templated_tests.python_fastapi.app.app import app
from datetime import date

client = TestClient(app)


def test_root():
    """测试根路径端点是否返回正确的欢迎信息"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (5, 3, 8),       # 正数测试
        (-5, 3, -2),     # 负数测试
        (0, 0, 0),       # 零值测试
        (100, 200, 300), # 大数测试
    ]
)
def test_add(num1, num2, expected):
    """测试加法端点是否正确执行加法操作"""
    response = client.get(f"/add/{num1}/{num2}")
    assert response.status_code == 200
    assert response.json() == {"result": expected}

@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (5, 3, 15),       # positive numbers
        (-5, 3, -15),     # negative and positive
        (0, 5, 0),        # zero multiplication
        (100, 200, 20000) # large numbers
    ]
)
def test_multiply(num1, num2, expected):
    """Test that multiply endpoint returns correct results"""
    response = client.get(f"/multiply/{num1}/{num2}")
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_days_until_new_year():
    """Test days_until_new_year endpoint returns correct calculation"""
    today = date.today()
    next_new_year = date(today.year + 1, 1, 1)
    expected_days = (next_new_year - today).days
    
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    assert response.json() == {"days_until_new_year": expected_days}


def test_current_date():
    """Test that current_date endpoint returns today's date"""
    response = client.get("/current-date")
    assert response.status_code == 200
    assert response.json() == {"date": date.today().isoformat()}


@pytest.mark.parametrize(
    "num1,num2,expected_status,expected_result",
    [
        (10, 2, 200, 5.0),     # normal division
        (0, 5, 200, 0.0),      # zero numerator
        (10, 0, 400, None),    # zero denominator
        (-10, 2, 200, -5.0),   # negative division
    ]
)
def test_divide(num1, num2, expected_status, expected_result):
    """Test division endpoint with various inputs"""
    response = client.get(f"/divide/{num1}/{num2}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == {"result": expected_result}
    else:
        assert response.json()["detail"] == "Cannot divide by zero"


@pytest.mark.parametrize(
    "number,expected_status,expected_result",
    [
        (4, 200, 2.0),          # positive number
        (0, 200, 0.0),          # zero
        (-4, 400, None),        # negative number (should raise error)
        (2.25, 200, 1.5),       # decimal number
    ]
)
def test_sqrt(number, expected_status, expected_result):
    """Test square root endpoint with various inputs"""
    response = client.get(f"/sqrt/{number}")
    assert response.status_code == expected_status
    if expected_status == 200:
        assert response.json() == {"result": expected_result}
    else:
        assert response.json()["detail"] == "Cannot take square root of a negative number"


@pytest.mark.parametrize(
    "number,expected",
    [
        (5, 25),      # positive number
        (-3, 9),       # negative number
        (0, 0),        # zero
        (10, 100),     # double digit
    ]
)
def test_square(number, expected):
    """Test that square endpoint returns correct results"""
    response = client.get(f"/square/{number}")
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_divide_by_zero():
    """Test that division by zero raises HTTPException"""
    response = client.get("/divide/5/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (5, 3, 2),       # positive numbers
        (-5, 3, -8),      # negative and positive
        (0, 0, 0),        # zeros
        (100, 200, -100), # large numbers
    ]
)
def test_subtract(num1, num2, expected):
    """Test that subtraction endpoint returns correct results"""
    response = client.get(f"/subtract/{num1}/{num2}")
    assert response.status_code == 200
    assert response.json() == {"result": expected}


