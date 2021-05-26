def f(n):
    return n - n//3 - n//5 + 2*(n//15)


if __name__ == '__main__':
    assert f(15) == 9
