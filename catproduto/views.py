from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catproduto.models import Categoria, Produto


class IndexView(TemplateView):
    template_name = 'index.html'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produtos/categorias.html'
    context_object_name = 'categorias'


class ProdutosListView(ListView):
    model = Produto
    template_name = 'produtos/listarprodutos.html'
    context_object_name = 'produtos'
    queryset = Produto.disponiveis.all()

    def get_queryset(self, slugcat=None):
        qs = super().get_queryset()
        if slugcat:
            cat = Categoria.get(slug=slugcat)
            qs = qs.filter(categoria=cat)
        return qs

    def get_context_data(self, slugcat=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if slugcat:
            context['categoria'] = Categoria.objects.get(slug=slugcat)
        return context
