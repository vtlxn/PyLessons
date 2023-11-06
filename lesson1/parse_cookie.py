def parse_cookie(query: str) -> dict:
    cookies = {}
    if not query:
        return cookies

    parts = query.split(';')
    for part in parts:
        key_value = part.split('=', 1)
        if len(key_value) == 2:
            key, value = key_value
            cookies[key] = value

    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}

    # Additional assertions
    assert parse_cookie('foo=;') == {'foo': ''}
    assert parse_cookie(' ') == {}
    assert parse_cookie('foo=1;bar=1=2=3=4;') == {'foo': '1', 'bar': '1=2=3=4'}
    assert parse_cookie('==foo;') == {'': '=foo'}
    assert parse_cookie('bar=1===2=3') == {'bar': '1===2=3'}
