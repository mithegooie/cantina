from django.conf.urls import patterns, include, url
from django.contrib import admin
from payments import views
from main.urls import urlpatterns as main_json_urls
from djangular_polls.urls import urlpatterns as djangular_polls_json_urls

admin.autodiscover()

main_json_urls.extend(djangular_polls_json_urls)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index', name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),

    # user registration/authentication
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^report$', 'main.views.report', name='report'),

    # api urls
    url(r'^api/v1/', include(main_json_urls)),
)
