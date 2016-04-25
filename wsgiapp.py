def app(environ, start_response):
    """ A barebones WSGI application.
        This is a starting point for your own web framework:)
    """
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return['Hello World from a simple WSGI application!\n']