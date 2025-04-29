import sepp01 as s

assert s.create_user("abc","abc@gmail.com","9036076747","Ma63621111ma") == "Account created successfully"
assert s.create_user("def","def@gmail.com","635412","abcdefgh586453") == "Invalid phone number"
assert s.verify_otp("123456","123456") == "otp verified"
assert s.verify_captcha("AB75m") == "Captcha verified"
