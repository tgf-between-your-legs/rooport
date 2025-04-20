# Django: Django REST Framework (DRF) Basics

Building REST APIs on top of Django applications using DRF.

## Core Concept: Toolkit for Building Web APIs

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs with Django. It simplifies the process of creating RESTful interfaces for your Django models and logic.

**Key Features:**

*   **Serialization:** Provides `Serializer` classes (especially `ModelSerializer`) to convert complex data types (like Django model instances and QuerySets) into native Python datatypes that can then be easily rendered into JSON, XML, or other content types. Also handles deserialization and validation of incoming data.
*   **Views & ViewSets:** Offers generic views (`APIView`, `GenericAPIView`) and ViewSets (`ViewSet`, `ModelViewSet`) specifically designed for building API endpoints. `ModelViewSet` provides default implementations for standard CRUD operations (list, retrieve, create, update, destroy) for a model with minimal code.
*   **Routers:** Work with ViewSets to automatically generate URL patterns for standard CRUD operations, reducing boilerplate URL configuration.
*   **Authentication & Permissions:** Pluggable authentication (TokenAuthentication, SessionAuthentication, etc.) and permission classes (IsAuthenticated, IsAdminUser, custom permissions) integrate seamlessly with Django's auth system to secure API endpoints.
*   **Request & Response Objects:** Extends Django's standard `HttpRequest` and `HttpResponse` with API-specific features, including content negotiation (`request.data`) and flexible response rendering.
*   **Browsable API:** Provides a user-friendly HTML interface for browsing and interacting with your API during development.

## Core Components & Workflow

**1. Serializers (`serializers.py`):**

*   Define how model instances or other Python objects are converted to JSON (and vice-versa).
*   `ModelSerializer` automatically generates fields based on a Django model.

```python
# myapp/serializers.py
from rest_framework import serializers
from .models import Article, Author, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name'] # Only expose needed fields

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # Nested read-only serializer
    class Meta:
        model = Author
        fields = ['user', 'bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ArticleSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField for simpler representation of relationships
    # author = serializers.SlugRelatedField(slug_field='user__username', read_only=True)
    # Or nest the full serializer (can cause N+1 query issues if not optimized in view)
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True) # For ManyToMany

    # Add custom fields or override existing ones
    author_username = serializers.CharField(source='author.user.username', read_only=True)
    # Example validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    class Meta:
        model = Article
        # Specify fields to include
        fields = [
            'id', 'title', 'slug', 'author', 'author_username', 'categories',
            'content', 'publish_date', 'status', 'is_featured',
            'created_at', 'updated_at'
        ]
        # Make certain fields read-only in API responses
        read_only_fields = ['created_at', 'updated_at', 'author_username']
        # Optionally specify fields needed only for writing (not included in response)
        # write_only_fields = ['internal_notes']
```

**2. Views / ViewSets (`views.py`):**

*   Handle API request logic, using serializers for data conversion and validation.
*   `ModelViewSet` provides default CRUD actions (`list`, `retrieve`, `create`, `update`, `partial_update`, `destroy`).

```python
# myapp/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
# from .permissions import IsAuthorOrReadOnly # Example custom permission

class CategoryViewSet(viewsets.ReadOnlyModelViewSet): # Read-only access
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] # Allow anyone to read categories

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-publish_date')
    serializer_class = ArticleSerializer
    # Define permissions - e.g., only authenticated users can modify
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # , IsAuthorOrReadOnly]

    # Optimize queryset for nested serializers
    def get_queryset(self):
        queryset = super().get_queryset()
        # Only show published articles in list view by default for non-staff
        if self.action == 'list' and not self.request.user.is_staff:
             queryset = queryset.filter(status='published')
        # Optimize related fields needed by serializer
        return queryset.select_related('author__user').prefetch_related('categories')

    # Automatically set author on creation
    def perform_create(self, serializer):
        # Assuming Author profile is linked via request.user.author_profile
        serializer.save(author=self.request.user.author_profile)

    # Example Custom Action
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def publish(self, request, pk=None):
        article = self.get_object()
        if article.status != 'published':
            article.status = 'published'
            article.publish_date = timezone.now()
            article.save()
            serializer = self.get_serializer(article)
            return Response(serializer.data)
        else:
            return Response({'status': 'already published'}, status=status.HTTP_400_BAD_REQUEST)

```

**3. URLs (`urls.py`):**

*   Use DRF Routers to automatically generate URLs for ViewSets.

```python
# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'myapp_api' # Use a distinct namespace for API urls

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet, basename='article') # 'article' is the base name for URL reversing
router.register(r'categories', views.CategoryViewSet, basename='category')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # Add any non-ViewSet API views manually here
]

# --- In project/urls.py ---
# urlpatterns = [
#     ...
#     path('api/v1/', include('myapp.urls', namespace='myapp_api')),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # Adds login/logout views to browsable API
#     ...
# ]
```

DRF significantly speeds up API development in Django. Key steps involve creating serializers to define the API representation of your models, using ViewSets (especially `ModelViewSet`) for standard CRUD logic, and registering ViewSets with a Router for automatic URL generation. Remember to configure authentication and permissions appropriately.

*(Refer to the official Django REST Framework tutorial and documentation.)*