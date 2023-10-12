from GIT.homework.hw5.algorithms.main import found_near
from GIT.homework.hw5.algorithms.main import count_worlds

def test_found_near():
    assert 5 == found_near("3 51 8 49 -1 3 50 7 4 4 4 9 6 6 6 5\n5")

def test_found_near2():
    assert 3 == found_near("1 3 7 9\n4")

def test_found_near3():
    assert "-3 или -5" == found_near("-1 -3 -5 -7 -9\n-4")


def test_count_worlds():
    assert 3 == count_worlds('pen pensil pen school')

def test_count_worlds2():
    assert 1 == count_worlds('pen pen pen')

def test_count_worlds3():
    assert 3 == count_worlds('hello world hello universe')


