from datetime import date
from django.contrib import admin
from .models import Aluno, Motorista, Veiculo, Rota

from django.contrib import admin
from django.contrib.auth.models import User


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'escola', 'rota', 'usuario_username', 'senha_temporaria', 'presenca_status')  

    def usuario_username(self, obj):
        return obj.usuario.username if obj.usuario else "Sem usuário"
    usuario_username.short_description = "Usuário"

    def senha_temporaria(self, obj):
        return "Definida automaticamente"  # A senha é gerada automaticamente
    senha_temporaria.short_description = "Senha Inicial"

    def presenca_status(self, obj):
        if obj.data_presenca == date.today():
            return dict(Aluno.PRESENCA_CHOICES).get(obj.presenca, "Não informado")
        return "Não marcada"
    presenca_status.short_description = "Presença Hoje"

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'cnh_categoria', 'cnh_validade')

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'capacidade', 'motorista')

@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'origem', 'destino', 'horario_saida', 'horario_chegada', 'veiculo', 'motorista')


class CustomUserAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff  # Apenas administradores podem acessar o Django Admin

admin.site.unregister(User)  # Remover configuração padrão
admin.site.register(User, CustomUserAdmin)  # Registrar novamente com permissão de admin