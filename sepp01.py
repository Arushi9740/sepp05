def create_user(user,email,mobile,password):
    if not user or not email or not mobile or not mobile:
        return "All fields are required"

    if "@" not in email:
        return "Invalid email"

    if ".com" not in email:
        return "Invalid email"

    if len(mobile) != 10:
        return "Invalid phone number"

    if len(password) < 8:
        return "Password must be 8 character long"
    return "Account created successfully"

def send_email_otp():
    return "123456"

def send_sms_otp():
    return "654321"

def verify_otp(entered,actual):
    if entered == actual:
        return "otp verified"
    return "Invalid otp"

def verify_captcha(captcha):
    if captcha == "AB75m":
        return "Captcha verified"
    return "Captcha failed"

if __name__=='__main__':
    # user = "abcdef"
    # email = "abc@gmail.com"
    # mobile = "9036076747"
    # password = "123654ghu"
    # result = create_user(user,email,mobile,password)

    # print(result)
    entered = 123456
    answer = 123456
    print(verify_otp(entered,answer))
    print(verify_captcha("AB75m"))


