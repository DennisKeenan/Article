from rest_framework import routers
from Article.viewsets import Article_ViewSets

router=routers.DefaultRouter()
router.register(r'article',Article_ViewSets)