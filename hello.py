def app(environ, start_response):
    qs = environ['QUERY_STRING'].split('&')
    status = '200 OK'
    start_response(status, [('Content-Type', 'text/plain')])
    return [bytes(query + '\n', 'utf-8') for query in qs]
