def logo_filter(response):
    """
    This function tries to find a logo and complete the logo src
    :param response: response from request
    :return: logo src
    """
    # find logo but with more responsibility
    logo = response.xpath("""
        //img[
            contains(
                translate(./@class, 'LOGO', 'logo'),
                'logo'
            )]/@src
        """).get()
    if logo is None:
        # find logo the next logo with less responsibility
        logo = response.xpath("""
            //img/@src[
                contains(
                    translate(., 'LOGO', 'logo'),
                    'logo'
                )]
            """).get()
    if logo is not None:
        if logo.startswith('http'):
            return logo  # if logo src is complete
        elif logo.startswith('//'):
            return 'http:' + logo  # if src is complete but not totally
        else:
            return response.urljoin(logo)  # if src is from the same site
