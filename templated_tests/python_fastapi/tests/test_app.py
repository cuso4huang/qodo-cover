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
