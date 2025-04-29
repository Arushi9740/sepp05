import sepp01 as s

def test_account_valid():
    assert s.create_user("abc","abc@gmail.com","9036076747","Ma63621111ma") == "Account created successfully"


def test_phone_invalid():
    assert s.create_user("def","def@gmail.com","635412","abcdefgh586453") == "Invalid phone number"


def test_otp():
    assert s.verify_otp("123456","123456") == "otp verified"


def test_captcha():
    assert s.verify_captcha("AB75m") == "Captcha verified"
