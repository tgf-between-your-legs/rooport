# Django REST Framework (DRF) Basics

Introduction to building REST APIs with Django using DRF.

## Core Concept

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs on top of Django. It simplifies serialization, request/response handling, authentication, permissions, and routing for APIs.

## Key Components

1.  **Serializers (`serializers.py`):**
    *   **Purpose:** Convert complex data types (like Django model instances or querysets) into native Python datatypes that can then be easily rendered into JSON, XML, or other content types. Also handle deserialization and validation of incoming data.
    *   **`serializers.Serializer`:** Base class for custom serialization logic. Define fields explicitly.
    *   **`serializers.ModelSerializer`:** A shortcut for automatically creating serializer fields based on a Django model. Includes default `create()` and `update()` implementations. **(Most commonly used)**.
    *   **Fields:** Similar to Django Forms (`CharField`, `IntegerField`, `BooleanField`, `DateTimeField`, `EmailField`, `URLField`, `PrimaryKeyRelatedField`, `HyperlinkedRelatedField`, `Nested Serializers`).
    *   **Validation:** Define `validate_<field_name>()` methods for field-specific validation or `validate()` method for object-level validation. Raise `serializers.ValidationError` on failure.

    ```python
    # myapp/serializers.py
    from rest_framework import serializers
    from .models import Post, Category
    from django.contrib.auth.models import User

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ['id', 'name', 'slug']

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = User # Assuming Author links to User
            fields = ['id', 'username', 'first_name', 'last_name']

    class PostSerializer(serializers.ModelSerializer):
        # Read-only field showing related author details
        author = AuthorSerializer(read_only=True)
        # Writable field using primary key for relationships
        categories = serializers.PrimaryKeyRelatedField(
            queryset=Category.objects.all(), many=True, required=False
        )
        # Custom field validation
        def validate_title(self, value):
            if len(value) < 5:
                raise serializers.ValidationError("Title must be at least 5 characters long.")
            return value

        class Meta:
            model = Post
            # Specify fields to include
            fields = ['id', 'title', 'slug', 'author', 'content', 'publish_date', 'status', 'categories']
            # Make some fields read-only in API output
            read_only_fields = ['publish_date']
    ```

2.  **Views (`views.py`):**
    *   **Purpose:** Handle incoming API requests, use serializers to process data, interact with models, and return responses.
    *   **`APIView`:** Base class for DRF views. Similar to Django's `View`, but with DRF-specific request/response handling and exception management. Define methods like `get()`, `post()`, `put()`, `delete()`.
    *   **Generic Views (`generics.*`):** Provide pre-built views for common patterns (List, Retrieve, Create, Update, Destroy). Examples: `ListAPIView`, `RetrieveAPIView`, `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`. Require `queryset` and `serializer_class` attributes.
    *   **ViewSets (`viewsets.*`):** Combine logic for a set of related views (e.g., list, retrieve, create, update for a single resource) into a single class. Often used with Routers. Examples: `ViewSet`, `GenericViewSet`, `ModelViewSet` (provides full CRUD implementation automatically).

    ```python
    # myapp/views.py
    from rest_framework import viewsets, permissions, generics
    from .models import Post, Category
    from .serializers import PostSerializer, CategorySerializer
    from .permissions import IsAuthorOrReadOnly # Example custom permission

    # ModelViewSet provides full CRUD automatically based on the serializer
    class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.filter(status='published') # Only show published posts by default
        serializer_class = PostSerializer
        # Configure permissions - only authenticated users can write, anyone can read
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
        lookup_field = 'slug' # Use slug instead of pk in URL for detail view

        # Override queryset for specific actions if needed
        # def get_queryset(self):
        #     if self.request.user.is_staff:
        #         return Post.objects.all()
        #     return Post.objects.filter(status='published')

        # Automatically set author on create
        def perform_create(self, serializer):
            # Assuming Author model has one-to-one with User
            serializer.save(author=self.request.user.author)

    # Example using generic views for simpler read-only endpoint
    class CategoryListView(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = [permissions.AllowAny] # Anyone can list categories
    ```

3.  **URLs (`urls.py`):**
    *   Map URL patterns to DRF views.
    *   **Routers (`routers.*`):** Used with ViewSets to automatically generate URL patterns for standard CRUD operations (list, create, retrieve, update, partial_update, destroy). Examples: `SimpleRouter`, `DefaultRouter` (includes a default API root view).

    ```python
    # myapp/urls.py
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from . import views

    app_name = 'myapp_api' # Namespace for API URLs

    # Create a router and register ViewSets with it.
    router = DefaultRouter()
    router.register(r'posts', views.PostViewSet, basename='post') # 'post' is the base name for URL reversing

    # The API URLs are now determined automatically by the router.
    # Examples: /posts/, /posts/{slug}/, etc.
    urlpatterns = [
        path('', include(router.urls)),
        # Add other non-ViewSet URLs if needed
        path('categories/', views.CategoryListView.as_view(), name='category-list'),
    ]

    # Include this in your project's root urls.py:
    # path('api/v1/', include('myapp.urls', namespace='myapp_api')),
    ```

4.  **Authentication & Permissions:**
    *   DRF provides pluggable authentication (e.g., `SessionAuthentication`, `TokenAuthentication` for API keys/JWT) and permission classes (`AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`, custom permissions).
    *   Configure defaults in `settings.py` (`REST_FRAMEWORK` dictionary) or per-view using `authentication_classes` and `permission_classes`.

## Request/Response Handling

*   **`Request` Object:** DRF's `Request` object extends Django's `HttpRequest`, providing parsed request data (`request.data` handles JSON, form data, etc.) and authentication context (`request.user`, `request.auth`).
*   **`Response` Object:** DRF's `Response` object handles content negotiation, allowing you to return Python data that DRF renders into the appropriate format (JSON by default) with the correct content type. Takes `data` and optional `status`.

DRF significantly speeds up API development in Django by providing well-structured components for common tasks.

*(Refer to the official Django REST Framework documentation: https://www.django-rest-framework.org/)*