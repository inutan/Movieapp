from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib import admin
#from movieApp.views import movie



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finalTry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^movieApp/$', 'movieApp.views.index'),
    url(r'^search/$', 'movieApp.views.search'),
    #urlpatterns = patterns('dbe.movieApp.views',
   #(r"", "main"),
#)
)
