from rest_framework import routers
from filemanager.views.viewsets import DataViewSet

router = routers.DefaultRouter()
router.register(r'files', DataViewSet, base_name='data')