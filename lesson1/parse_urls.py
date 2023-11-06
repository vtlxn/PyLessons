from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query)
    flat_params = {}
    for key, value in query_params.items():
        flat_params[key] = value[0]
    return flat_params


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}

    # Additional assertions
    assert parse('https://example.com/path/to/page?name=John%20Doe&age=25&city=New%20York') == (
        {'name': 'John Doe', 'age': '25', 'city': 'New York'}
    )
    assert parse('https://example.com/path/to/page?name=Alice&name=Bob&name=Charlie') == {'name': 'Alice'}
    assert parse('https://example.com/path/to/page?name=&age=30') == {'age': '30'}
    assert parse('https://example.com/path/to/page?param1&param2=42&param3') == {'param2': '42'}
    assert parse('https://example.com/path/to/page?query=coffee%20%26%20tea&price=$5%20%26%20up') == (
        {'query': 'coffee & tea', 'price': '$5 & up'}
    )
