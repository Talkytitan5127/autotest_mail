from typing import Type
import pytest


class TestStrObject:
    def test_1(self):
        class Foo:
            def __init__(self, number):
                self.number = number
            def __str__(self):
                return f'Foo {self.number}'
        
        f = Foo(5)
        assert str(f) == 'Foo 5'


    @pytest.mark.parametrize(("orig", "dest"), [(100, '100'), ('string', 'string'), (['a', 'b'], "['a', 'b']"), ({'a': 1}, "{'a': 1}")])
    def test_2(self, orig, dest):
        assert str(orig) == dest

    def test_3(self):
        try:
            test = 'test_setitem'
            test[5] = 'a'
            assert test[5] == 'a'
        except TypeError:
            pass


class TestSetObject:
    def test_1(self):
        try:
            assert set([set([set([1]),2]),3]) == {1,2,3}
        except TypeError:
            pass

    @pytest.mark.parametrize("x", [['1','2','3'], '123', {'1':6, '2':5, '3':4}])
    def test_2(self, x):
        assert set(x) == {'1','2','3'}

    def test_3(self):
        set('not understand the task') == {'t', 'h', 'a', 'd', 's', 'r', ' ', 'n', 'k', 'u', 'o', 'e'}
