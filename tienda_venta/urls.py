from rest_framework import routers
from .viewsets import ClienteViewSets
from .viewsets import ClienteLogin


router = routers.SimpleRouter()
router.register('clientes', ClienteViewSets)
router.register('busca', ClienteLogin)





urlpatterns = router.urls

'''
urlpatterns= [
    url(r'^tienda_venta/$',views.Login)
]'''


