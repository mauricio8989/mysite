from django.db import models
from django.contrib.auth.models import User

STATUS =(
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Esta variável armazena o título do post
    slug = models.SlugField(max_length=200, unique=True) # Esta variável armazena a identificação do post 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # Esta variável armazena o autor do post
    updated = models.DateTimeField(auto_now=True) # Esta variável armazena ultima atualização do post
    content = models.TextField() # Esta variável armazena O conteúdo do post
    created_on = models.DateTimeField(auto_now_add=True) # Esta variável armazena a datada criação
    status = models.IntegerField(choices=STATUS, default=0) # Esta variável define se é um rascunho ou um post


class Meta:
    ordering =['-created_on']

def __str__(self):
    return self.title