from django.contrib import admin
from django.urls import include, path

from django.shortcuts import render
from blogicum.views import RegisterUpView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', RegisterUpView.as_view(), name='registration'),
]

def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    return render(request, 'pages/500.html', status=500)


handler404 = 'blogicum.urls.page_not_found'
handler500 = 'blogicum.urls.server_error'
handler403 = 'blogicum.urls.csrf_failure'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
