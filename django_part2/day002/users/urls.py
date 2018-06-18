from django.conf.urls import url
from . import views
urlpatterns = [
    url('^cookie_set$', views.cookie_set),
    url('^cookie_get$', views.cookie_get),
    url('^session_set', views.session_set),
    url('^session_get', views.session_get),
    url('^show$', views.show),
    url('^RegisterView$', views.RegisterView.as_view())

]