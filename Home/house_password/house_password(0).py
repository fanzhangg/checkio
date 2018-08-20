def checkio(data: str) -> bool:
    data = str(data)
    result = True

    if len(data) < 10:
        result = False
    if not any(i.isdigit() for i in data):
        result = False
    if not any(i.isupper() for i in data):
        result = False
    if not all(i.isdigit() or i.isalpha() for i in data):
        result = False
    return result


if __name__ == '__main__':
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"






