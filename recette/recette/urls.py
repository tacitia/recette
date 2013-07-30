from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views as hpViews


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recette.views.home', name='home'),
    # url(r'^recette/', include('recette.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
	url(r'^kitchen/', include('kitchen.urls', namespace='kitchen')),
	url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', hpViews.index, name='index'),
)
