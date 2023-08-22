from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('djoser.social.urls')),
]

urlpatterns += [re_path(r'api/^.*', TemplateView.as_view(template_name='index.html'))]