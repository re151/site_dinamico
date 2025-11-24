from django.db import models
from django.conf import settings
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    data_postagem = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredients = models.TextField(max_length=500, null=True)
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField(default = 0,
                                        help_text= "tempo em minutos")  # tempo em minutos
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.title  

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} - {self.text}'  
    
class Category(models.Model):
    receitas = models.ManyToManyField(Post)
    CATEGORIAS = [
        ("DOC", "Doce"),
        ("SAL", "Salgado"),
        ("VEG", "Vegetariano"),
        ("VEGANO", "Vegano"),
        ("BEB", "Bebida"),
        ("NAT", "Natal"),
    ]
    categoria = models.CharField(max_length=200, choices=CATEGORIAS, null=True, blank=True)

    def __str__(self):
        return self.categoria
    

