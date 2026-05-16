from urllib.parse import urlparse
from django.conf import settings


class SiteUrlHostMiddleware:
    """
    Forces request host/scheme to match SITE_URL.
    Fixes OAuth callback URLs when the reverse proxy doesn't forward the correct host.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        parsed = urlparse(getattr(settings, 'SITE_URL', ''))
        self.netloc = parsed.netloc
        self.scheme = parsed.scheme

    def __call__(self, request):
        if self.netloc:
            request.META['HTTP_HOST'] = self.netloc
            request.META.pop('HTTP_X_FORWARDED_HOST', None)
        if self.scheme == 'https':
            request.META['HTTP_X_FORWARDED_PROTO'] = 'https'
        return self.get_response(request)
