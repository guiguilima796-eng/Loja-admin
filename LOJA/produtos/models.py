from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(
        "Nome do Produto",
        max_length=100,
        help_text="Informe o nome do produto"
    )
    preco = models.CharField(
        "Preço de Venda",
        max_digits=8,
        decimal_place=2,
        help_text="Informe o Preço Unitario em Reais do Produto"
        )
    estoque = models.PositiveIntegerField(
        "quantidade_em_estoque",
        default=0,
        help_text="Quantidade de produtos em estoque"
    )
    ativo = models.BooleanField(
        "Disponivel para Venda",
        default= True,
        help_text="Marque-se o produto que está ativo"
    )
    class Meta:
        verbose_name = "Produto",
        verbose_name_plural ="Produtos",
        ordering = ["nome"]
    def __str__(self):
        return f"{self.nome} (R${self.preco:.2f})"