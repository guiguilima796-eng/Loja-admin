from django.contrib import admin
from .models import Produto
# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','preco','estoque')
    list_filter = ('ativo',)
    search_fields = ('nome',) 
