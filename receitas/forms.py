from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 
                  'ingredients', 'modo_preparo',
                  'tempo_preparo', 'image']
        labels = {
            'title': 'Nome da Receita',
            'ingredients': 'Indredientes (separados por vírgula)',
            'modo_preparo': 'Modo de Preparo',
            'tempo_preparo': 'Tempo de Preparo (em minutos)',
            'image': 'URL da imagem da receita',}
        
class ReviewForm(ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
        labels = {
            'text': 'Comentário',
        }