from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.recipe_list,name='recipe_list'),
  path('create/',views.recipe_create,name='recipe_create'),
  path('update/<int:recipe_id>/',views.recipe_update,name='recipe_update'),
  path('delete/<int:recipe_id>/',views.recipe_delete,name='recipe_delete'),
  path('login/',views.user_login,name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)