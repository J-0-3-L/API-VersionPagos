from . import api
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'pagos', api.PagoViewSet, 'pagos'),


# router.register('user', views.GetUsers)

urlpatterns = router.urls