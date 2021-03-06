"""Mykate URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from content import views as content_views
from kate.views import ulist as kate_ulist
from kate.views import handler404, handler500, handler403

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', content_views.UserViewSet)
router.register(r'groups', content_views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', content_views.test, name='test'),

    url(r'^$', content_views.index, name='index'),
    url(r'^index/$', content_views.index, name='index'),

    # url(r'^account/', include('users.urls')),
    url(r'^ulist/$', kate_ulist, name='ulist'),

    url(r'^aboutme/$', content_views.about_me, name='aboutme'),

    url(r'^add/$', content_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', content_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', content_views.add2, name='add2'),

]
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
handler404 = handler404
handler403 = handler403
handler500 = handler500
