def render_date(date, is_infinity: bool=False):
    if is_infinity:
        return 'бессрочно'
    if date:
        return str(date)
    return ''
