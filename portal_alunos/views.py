from datetime import date
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Certifique-se de que isso está importado!
from django.core.exceptions import PermissionDenied

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

def login_aluno(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Verifica se o usuário não é staff (admin)
            if not user.is_staff:
                login(request, user)
                request.session.set_expiry(86400)  # Sessão válida por 1 dia
                return redirect('dashboard')
            else:
                return render(request, 'portal_alunos/login.html', {'erro': 'Usuário não permitido'})

        return render(request, 'portal_alunos/login.html', {'erro': 'Usuário ou senha inválidos'})

    return render(request, 'portal_alunos/login.html')

def logout_aluno(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required
def dashboard(request):
    aluno = request.user.aluno
    return render(request, 'portal_alunos/dashboard.html', {'aluno': aluno})


@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Evita logout do usuário
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'portal_alunos/alterar_senha.html', {'form': form})


@login_required
def marcar_presenca(request):
    aluno = request.user.aluno  # Obtém o aluno logado

    if request.method == 'POST':
        presenca = request.POST.get('presenca')
        if presenca:
            aluno.presenca = presenca
            aluno.data_presenca = date.today()  # Registra a data da presença
            aluno.save()
            messages.success(request, "Presença registrada com sucesso!")
        return redirect('dashboard')

    return render(request, 'portal_alunos/marcar_presenca.html', {'aluno': aluno})