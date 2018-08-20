def checkio(data: str) -> bool:
    data = str(data)
    result = True

    if len(data) < 10:
        # print("The length of the password is less than 10 symbols")
        result = False
    if not any(i.isdigit() for i in data):
        # print("The password does not contain any digit")
        result = False
    if not any(i.isupper() for i in data):
        # print("The password does not contain any uppercase letter")
        result = False
    if not all(i.isdigit() or i.isalpha() for i in data):
        # print("The password does not contain only ASCII latin letters or digits")
        result = False
    return result


if __name__ == '__main__':
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"






