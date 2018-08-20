import string

upper = set(string.ascii_uppercase)
lower = set(string.ascii_lowercase)
digits = set(string.digits)


def checkio(data):
    letters = set(data)
    return bool(len(data) >= 10 and upper & letters and lower & letters and digits & letters)


if __name__ == '__main__':
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
