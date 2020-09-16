def convert_number(phoneNumber):
    phoneNumber = phoneNumber.replace('-', '')
    if len(phoneNumber) == 10:
        phoneNumber = '1' + phoneNumber
    return phoneNumber

