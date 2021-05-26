def A(s):
    return s[::-1]

def B(s: str):
    return ' '.join([A(w) for w in s.split(' ')])


if __name__ == '__main__':
    test_a = 'junyiacademy'
    ans_a = 'ymedacaiynuj'
    assert A(test_a) == ans_a

    test_b = 'flipped class room is important'
    ans_b = 'deppilf ssalc moor si tnatropmi'
    assert B(test_b) == ans_b
