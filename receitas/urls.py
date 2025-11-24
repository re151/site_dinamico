from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'receitas'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:receita_id>/', views.detail_receita, name='detail'),
    path('update/<int:receita_id>/', views.update_receita, name='update'),
    path('delete/<int:receita_id>/', views.delete_receita, name='delete'),
    path('search/', views.search_receita, name='search'),
    path('create/', views.create_receita, name='create'),
    path('<int:receita_id>/createcomments/', views.create_comment, name='create_comment'),
    path('<int:receita_id>/comments/', views.view_comments, name='view_comments'),
    path('categoria/', views.CategoryView.as_view(), name='categoria'),
    path("categorias/<int:categoria_id>/", views.category_detail, name="category_detail"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)