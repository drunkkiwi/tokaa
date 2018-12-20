from django.urls                    import path
from home                           import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('a/<slug:title>/', views.article_view, name='article_view'),
    path('iV12241120181008mtfaaA', views.about, name='about'),
    path('c/<str:category>', views.category_view, name='category_view'),
    path('flake', views.flake_view, name='flake_view'),

    # Search
    path('s', views.search_view, name='search_view'),
]
