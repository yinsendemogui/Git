"""muggle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import answer, detail, home, Login, profile, register, search,vote
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^answer/', answer, name="answer"),
    url(r'^detail/(?P<question_id>\d+)/$', detail, name="detail"),
    url(r'^home/', home, name="home"),
    url(r'^login/$', Login, name="login"),
    url(r'^profile/', profile, name="profile"),
    url(r'^register/$', register, name="register"),
    url(r'^search/', search, name="search"),
    url(r'^vote/(?P<id>\d+)/$', vote, name="vote"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
