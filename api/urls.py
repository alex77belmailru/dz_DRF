from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('storages', StorageModelViewSet)
router.register('products', ProductModelViewSet)


urlpatterns = [
              ] + router.urls
