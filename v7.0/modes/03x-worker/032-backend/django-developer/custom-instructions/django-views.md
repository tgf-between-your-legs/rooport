# Django: Views (Request Handling)

Implementing request handling logic using Function-Based Views (FBVs) and Class-Based Views (CBVs).

## Core Concept: Processing Requests, Returning Responses

In Django's MVT pattern, the **View** is responsible for receiving an `HttpRequest` object, performing necessary logic (interacting with models, processing forms), and returning an `HttpResponse` object (often by rendering a template).

Django offers two primary ways to write views:

1.  **Function-Based Views (FBVs):** Simple Python functions that take `request` as their first argument. Easy to understand for simple cases.
2.  **Class-Based Views (CBVs):** Python classes that inherit from `django.views.View` or its subclasses (including generic views). Use methods corresponding to HTTP verbs (`get()`, `post()`, etc.) to handle requests. Offer better code organization, reusability through inheritance and mixins, especially for complex views or standard CRUD operations.

## Function-Based Views (FBVs)

*   A Python function taking `request` and optional URL parameters.
*   Must return an `HttpResponse` object (or subclass like `HttpResponseRedirect`, `JsonResponse`).
*   Use decorators for common tasks like authentication (`@login_required`) or restricting HTTP methods (`@require_http_methods`).

```python
# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Article
from .forms import ArticleForm

# Example: List view
def article_list(request):
    articles = Article.objects.filter(status='published').order_by('-publish_date')
    context = {'articles': articles}
    # Renders template 'myapp/templates/myapp/article_list.html'
    return render(request, 'myapp/article_list.html', context)

# Example: Detail view
def article_detail(request, pk):
    # try:
    #     article = Article.objects.get(pk=pk, status='published')
    # except Article.DoesNotExist:
    #     raise Http404("Article does not exist or is not published")
    # Shortcut:
    article = get_object_or_404(Article, pk=pk, status='published')
    context = {'article': article}
    return render(request, 'myapp/article_detail.html', context)

# Example: Create view (handling GET and POST)
@login_required # Decorator to require login
@require_http_methods(["GET", "POST"]) # Decorator to restrict methods
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES or None) # Pass request.FILES for file uploads
        if form.is_valid():
            # Process the data in form.cleaned_data
            new_article = form.save(commit=False) # Create model instance but don't save yet
            # Assuming author is linked to user, set it here
            # new_article.author = request.user.author_profile
            new_article.save()
            form.save_m2m() # Important for saving ManyToMany relationships on ModelForms
            # Redirect to the detail view of the newly created article
            return redirect('myapp:article_detail', pk=new_article.pk)
    else: # GET request
        form = ArticleForm() # Create an empty form

    context = {'form': form}
    return render(request, 'myapp/article_form.html', context)

# Example: Simple JSON response
def api_article_data(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = {
        'id': article.pk,
        'title': article.title,
        'status': article.status,
    }
    return JsonResponse(data)
```

## Class-Based Views (CBVs)

*   Inherit from `django.views.View` or generic views.
*   Request dispatch happens via the `dispatch()` method, which calls methods named after HTTP verbs in lowercase (e.g., `get()`, `post()`, `put()`, `delete()`).
*   Access request, args, kwargs via `self.request`, `self.args`, `self.kwargs`.
*   Use mixins (e.g., `LoginRequiredMixin`) for common functionality instead of decorators.

```python
# myapp/views.py
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm

# Example: Basic CBV
class MyView(LoginRequiredMixin, View):
    login_url = '/login/' # Required by LoginRequiredMixin if not default
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        # Logic for GET request
        return HttpResponse('This is a GET request')

    def post(self, request, *args, **kwargs):
        # Logic for POST request
        return HttpResponse('This is a POST request')

# --- Generic Class-Based Views ---
# Simplify common patterns (CRUD, list/detail)

# Example: List view using ListView
class ArticleListView(ListView):
    model = Article # Specify the model
    template_name = 'myapp/article_list.html' # Specify the template
    context_object_name = 'articles' # Name for the list in the template context (default is object_list)
    paginate_by = 10 # Optional pagination

    def get_queryset(self):
        # Optionally customize the queryset
        return Article.objects.filter(status='published').order_by('-publish_date')

# Example: Detail view using DetailView
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'myapp/article_detail.html'
    context_object_name = 'article' # Default is object or model name lowercased

    def get_queryset(self):
        # Ensure only published articles are accessible via detail view
        return Article.objects.filter(status='published')

# Example: Create view using CreateView
class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm # Use this form
    template_name = 'myapp/article_form.html'
    success_url = reverse_lazy('myapp:article_list') # Redirect URL after successful creation (use reverse_lazy)
    permission_required = 'myapp.add_article' # Example permission check

    def form_valid(self, form):
        # Optionally modify the instance before saving
        form.instance.author = self.request.user.author_profile # Set author automatically
        return super().form_valid(form) # Call parent method to save and redirect

# Example: Update view using UpdateView
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'myapp/article_form.html'
    # success_url is often derived from get_absolute_url on the model

    def get_queryset(self):
        # Ensure users can only edit their own articles (example)
        return Article.objects.filter(author=self.request.user.author_profile)

# Example: Delete view using DeleteView
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'myapp/article_confirm_delete.html'
    success_url = reverse_lazy('myapp:article_list')

    def get_queryset(self):
        # Ensure users can only delete their own articles (example)
        return Article.objects.filter(author=self.request.user.author_profile)

```

**FBVs vs. CBVs:**

*   Use FBVs for simple, straightforward views or highly custom logic that doesn't fit generic patterns.
*   Use CBVs (especially generic CBVs) for standard CRUD operations and list/detail views to reduce boilerplate code and leverage built-in functionality and mixins.

Views are the core logic handlers in Django. Choose between FBVs and CBVs based on the complexity and reusability requirements of the specific view. Generic CBVs are powerful tools for common tasks.