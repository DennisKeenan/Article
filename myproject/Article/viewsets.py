from rest_framework import viewsets
from .models import Article
from .serializers import Article_Serializers

class Article_ViewSets(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=Article_Serializers