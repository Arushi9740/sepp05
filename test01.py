import sepp01 as sepp01

assert sepp01.create_user("abc","abc@gmail.com","9036076747","Ma63621111ma") == "Account created successfully"
assert sepp01.create_user("def","def@gmail.com","635412","abcdefgh586453") == "Invalid phone number"
assert sepp01.verify_otp("123456","123456") == "otp verified"
assert sepp01.verify_captcha("AB75m") == "Captcha verified"
