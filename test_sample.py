import pytest





#
# def inc(x):
#     return x+1
#
# def test_answer():
#     assert inc(3)==5



@pytest.fixture(scope="function")
def login():
    print("登录")
    yield
    print("注销登录")

def test_demo01():
    a = 1
    b = 2
    assert a==b
    print("测试用例")

def test_demo02(login):
    print("测试用列")










if __name__ == "__main__":
    pytest.main(["test_sample.py","-s"])




