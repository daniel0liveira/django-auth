from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class AuthenticationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # Defina as URLs que você quer liberar (como a página de login)
        self.exempt_urls = [reverse('login')]  # ajuste 'login' para o nome correto da URL

    def __call__(self, request):
        # # Verifica se o usuário está autenticado ou a URL atual está na lista de URLs liberadas
        # if not request.user.is_authenticated and request.path not in self.exempt_urls:
        #     # Redireciona para a página de login
        #     return redirect('login')

        return self.get_response(request)
