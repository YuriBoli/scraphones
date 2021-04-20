from .phone_validator import phone_validator


def phone_filter(response):
    """
    This function tries to find all phones in the response
    :param response: response from request
    :return: list with all numbers found
    """
    regex_body = '[+\s]?[\s\d]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*'
    # filter numbers in <a> tags with contains "tel:"
    # tel: is used to make calls from links
    numbers_a_filtered = response.xpath('//a/@href[contains(., "tel:")]').getall()
    # filter all numbers in the body using regex
    numbers_body = response.css('body *::text').re(regex_body)
    numbers_a = [n.replace('tel:', '') for n in numbers_a_filtered]
    # merge those two fonts
    numbers = numbers_a + numbers_body
    # extract the language and country if in response
    # default country is US
    lang = response.xpath('/html/@lang').get()
    if lang is None or len(lang) < 3:
        region = 'US'
    else:
        region = lang[3:]
    # find valid and unique phone numbers
    real_numbers = {phone_validator(nb, region) for nb in
                    numbers if len(nb.strip()) > 8}
    if None in real_numbers:
        real_numbers.remove(None)
    return list(real_numbers)
