from django.conf import settings

class SeparateSessionMiddleware:
    """
    Middleware para manter sessões separadas entre o Django Admin e o Portal do Aluno.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/aluno/"):  # Se for uma rota do Portal do Aluno
            request.session.save()
            request.session.set_expiry(86400)  # Sessão de 1 dia
            request.session.modified = True
            request.session["portal_aluno"] = True  # Marcador para evitar conflito com Admin
        elif request.path.startswith("/admin/"):  # Se for uma rota do Django Admin
            request.session.save()
            request.session.set_expiry(86400)  # Sessão de 1 dia
            request.session.modified = True
            request.session["admin_user"] = True  # Identificador para Admin
        return self.get_response(request)
