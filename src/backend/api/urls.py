from django.contrib import admin
from . import view
from django.urls import path, include, re_path
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/', view.mail),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('djoser.social.urls')),
]
# urlpatterns = [re_path(r'^.*', TemplateView.as_view(template_name='index.ru'))]