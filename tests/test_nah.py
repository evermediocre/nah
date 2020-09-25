import pytest
import nah


def test_nah_meh():
    @nah.meh
    def fn():
        raise Exception

    assert fn() is None


def test_nah_meh_when_exception():
    @nah.meh(when=ValueError)
    def fn():
        raise ValueError

    assert fn() is None


def test_nah_meh_when_exception_no_matched():
    @nah.meh(when=ValueError)
    def fn(n):
        return n / 0

    with pytest.raises(ZeroDivisionError):
        fn(100)


def test_nah_meh_no_error():
    @nah.meh
    def fn():
        return 100

    assert fn() == 100


def test_nah_gimme():
    @nah.gimme(777)
    def fn():
        raise Exception

    assert fn() == 777


def test_nah_gimme_no_error():
    @nah.gimme(777)
    def fn():
        return 555

    assert fn() == 555


def test_nah_gimme_when_exception():
    @nah.gimme(777, when=ValueError)
    def fn():
        raise ValueError

    assert fn() == 777


def test_nah_gimme_when_exception_no_matched():
    @nah.gimme(777, when=ValueError)
    def fn(n):
        return n / 0

    with pytest.raises(ZeroDivisionError):
        fn(100)


def test_nah_maybe():
    def default(n):
        return 1234 + n

    @nah.maybe(default)
    def fn(n):
        raise Exception

    assert fn(11111) == 12345


def test_nah_maybe_when_exception():
    def default(n):
        return 1234 + n

    @nah.maybe(default, when=ValueError)
    def fn(n):
        raise ValueError

    assert fn(11111) == 12345


def test_nah_maybe_when_exception_no_matched():
    def default(n):
        return 1234 + n

    @nah.maybe(default, when=(ValueError, KeyError))
    def fn(n):
        return n / 0

    with pytest.raises(ZeroDivisionError):
        fn(11111)


def test_nah_maybe_no_error():
    def default(n):
        return 1234 + n

    @nah.maybe(default)
    def fn(n):
        return 100 + n

    assert fn(1) == 101


def test_nah_again():
    @nah.again(3)
    def fn():
        fn.calls += 1
        raise ValueError

    fn.calls = 0

    with pytest.raises(ValueError):
        try:
            fn()
        except:
            assert fn.calls == 3
            raise


def test_nah_again_no_matched_exception():
    @nah.again(3, when=(ValueError, KeyError))
    def fn():
        fn.calls += 1
        return 1 / 0

    fn.calls = 0

    with pytest.raises(ZeroDivisionError):
        try:
            fn()
        except:
            assert fn.calls == 1
            raise


def test_nah_again_no_error():
    @nah.again(3)
    def fn(x, y):
        fn.calls += 1
        return x * y

    fn.calls = 0

    assert fn(2, 3) == 6
    assert fn.calls == 1
