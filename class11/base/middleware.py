from django.http import Http404

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("Before run view function")

        response = self.get_response(request)

        print("After run view function")

        # Code to be executed for each request/response after
        # the view is called.

        return response