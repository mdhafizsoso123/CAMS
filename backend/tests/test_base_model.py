from database.base_model import BaseModel


def test_base_model():
    assert BaseModel.__abstract__ is True