from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'players', views.UserViewSet)
router.register(r'servers', views.ServerViewSet)
router.register(r'characters', views.CharacterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
    url(r'^add-character/$', views.add_character_view, name='add_character_view'),
    url(r'^signup/$', views.signup_view, name='signup_view'),
    url(r'^queue/(?P<character_id>[0-9])$', views.queue_character_view, name='queue_character_view'),
    url(r'^dequeue/(?P<character_id>[0-9])$', views.dequeue_character_view, name='dequeue_character_view'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
