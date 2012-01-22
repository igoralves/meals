from django.conf.urls.defaults import patterns

urlpatterns = patterns('meals.views',
 (r'^lista/(?P<model>\w+)/$', 'lista'),
 (r'^adiciona/(?P<model>\w+)/$', 'adiciona_ou_atualiza'),
 (r'^atualiza/(?P<model>\w+)/(?P<key>\d+)/$', 'adiciona_ou_atualiza'),
 (r'^remove/(?P<model>\w+)/(?P<key>\d+)/$', 'remove'),
)