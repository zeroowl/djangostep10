from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from step10 import views
import settings
from step10.models import AnswerSet
from django.views.generic import date_based


admin.autodiscover()

answer_set_info = {
    "queryset"   : AnswerSet.objects.all(),
    "date_field" : "date"
}


urlpatterns = patterns('',
    # Example:
    # (r'^djangostep10/', include('djangostep10.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^saveResults/',views.saveResults),
    (r'showMyResults/',views.showMyResults),
    (r'^about/',views.about),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (settings.LOGIN_URL[1:], login),
    (settings.LOGOUT_URL[1:], logout,{'next_page': settings.LOGIN_REDIRECT_URL}),
    ('accounts/register/',views.register),
    (r'^answersets/$', date_based.archive_index, answer_set_info),
    (r'^$',views.mainView),
)

#    application = webapp.WSGIApplication([('/', MainHandler),
#                                          ('/initdb',initdbHandler),
#                                          ('/saveResults',saveResultsHandler),
#                                          ('/showMyResults',showMyResultsHandler),
#                                          ('/changeLanguage',changeLanguageHandler),
