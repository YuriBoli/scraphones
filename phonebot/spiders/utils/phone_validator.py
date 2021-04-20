import phonenumbers


def phone_validator(phone_n, country_code):
    """
    This function validate phone numbers and return this in a user friendly format
    :param phone_n: phone number to be validated
    :param country_code: country code of phone number
    :return: phone number if is valid
    """
    # remove white spaces
    phone_n = phone_n.strip()
    phone_n_processed = None
    try:
        # verify if the number have country code
        if phone_n[0] == '+':
            phone_n_processed = phonenumbers.parse(phone_n, None)
        else:
            # if not, then we use the country code from the site
            # if the site don't have country code,
            # then the number will be invalid.
            phone_n_processed = phonenumbers.parse(phone_n, country_code)
        # verify the number
        valid = phonenumbers.is_valid_number(phone_n_processed)
    except phonenumbers.NumberParseException:
        # if some error happens then, probably the phone is invalid
        valid = False
    if valid:
        # clear the number
        phone_n_beauty = phonenumbers.format_number(
            phone_n_processed,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        return phone_n_beauty