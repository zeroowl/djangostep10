from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from step10 import views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djangostep10/', include('djangostep10.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^saveResults/',views.saveResults),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^login/$', login),
    (r'^logout/$', logout,{'next_page':'/'}),    
    (r'^$',views.mainView),
)

#    application = webapp.WSGIApplication([('/', MainHandler),
#                                          ('/initdb',initdbHandler),
#                                          ('/saveResults',saveResultsHandler),
#                                          ('/showMyResults',showMyResultsHandler),
#                                          ('/changeLanguage',changeLanguageHandler),