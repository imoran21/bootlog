from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home_base', name='home_base'),
    url(r'^logged_in/', 'home.views.logged_in', name='logged_in'),
    url(r'^create_bill/', 'home.views.create_bill', name='create_bill'),
    url(r'^logout_view/', 'home.views.logout_view', name='logout'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^home/', include('home.urls')),

)
