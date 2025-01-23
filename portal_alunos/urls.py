from django.urls import path
from .views import alterar_senha, login_aluno, logout_aluno, dashboard, marcar_presenca
from .views import marcar_presenca

urlpatterns = [
    path('', login_aluno, name='login'),
    path('logout/', logout_aluno, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('alterar-senha/', alterar_senha, name='alterar_senha'),
    path('marcar-presenca/', marcar_presenca, name='marcar_presenca'),

]
