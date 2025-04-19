# Django: Authentication & Authorization

Using Django's built-in system for managing users, permissions, and access control.

## Core Concept: Secure User Management

Django includes a robust authentication (`contrib.auth`) and authorization system that handles user accounts, groups, permissions, and cookie-based user sessions.

**Key Components:**

*   **User Model:** Represents users. Django provides a default `User` model (`django.contrib.auth.models.User`) with fields like `username`, `password` (hashed), `email`, `first_name`, `last_name`, `is_staff`, `is_active`, `is_superuser`. Can be swapped for a custom user model if needed.
*   **Authentication Backend:** Verifies user credentials (e.g., username/password). Django provides a default backend and allows custom ones.
*   **Permissions:** Flags assigned to users or groups that designate whether they can perform specific actions (e.g., `myapp.add_article`, `myapp.change_article`). Permissions are typically created automatically for models when `django.contrib.auth` is in `INSTALLED_APPS`.
*   **Groups:** A way to categorize users and assign permissions to multiple users at once.
*   **Password Management:** Securely handles password hashing and validation.
*   **Session Framework:** Manages user sessions (typically using signed cookies) to keep users logged in between requests.
*   **Views & Forms:** Provides built-in views (`LoginView`, `LogoutView`, `PasswordChangeView`, etc.) and forms (`AuthenticationForm`, `UserCreationForm`) for common authentication tasks.

## Configuration (`settings.py`)

*   Ensure `django.contrib.auth` and `django.contrib.contenttypes` (needed by auth) are in `INSTALLED_APPS`.
*   Ensure `django.contrib.sessions.middleware.SessionMiddleware` and `django.contrib.auth.middleware.AuthenticationMiddleware` are in `MIDDLEWARE`.
*   `AUTH_USER_MODEL`: If using a custom user model, set this to `'yourapp.YourUserModel'`.
*   `LOGIN_URL`: URL name or path where users are redirected if `@login_required` fails (default: `/accounts/login/`).
*   `LOGIN_REDIRECT_URL`: URL name or path where users are redirected after successful login (default: `/accounts/profile/`).
*   `LOGOUT_REDIRECT_URL`: URL name or path where users are redirected after logout.
*   `AUTHENTICATION_BACKENDS`: List of authentication backends to use.

## Using the Built-in `User` Model

```python
# views.py
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm # Example custom form

# --- Accessing the Logged-in User ---
@login_required
def user_profile(request):
    # request.user is the currently logged-in User instance (or AnonymousUser)
    user = request.user
    is_editor = user.groups.filter(name='Editors').exists()
    can_add = user.has_perm('myapp.add_article')

    context = {
        'user': user,
        'is_editor': is_editor,
        'can_add_article': can_add,
    }
    return render(request, 'myapp/profile.html', context)

# --- Login / Logout ---
# Often use Django's built-in views via urls.py:
# path('accounts/', include('django.contrib.auth.urls')),
# Or implement custom login/logout views:
def custom_login(request):
    if request.method == 'POST':
        # Use Django's AuthenticationForm or a custom one
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome back, {username}!")
                return redirect('myapp:profile') # Redirect to desired page
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('myapp:home') # Redirect to home or login page

# --- User Creation ---
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # Use UserCreationForm or a custom subclass
        if form.is_valid():
            user = form.save()
            login(request, user) # Optional: log user in immediately
            messages.success(request, "Registration successful!")
            return redirect('myapp:profile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# --- Permissions ---
@permission_required('myapp.add_article', login_url='/login/')
def add_article_view(request):
    # Only users with the 'add_article' permission can access this view
    # ... view logic ...
    pass

def check_perms_manually(request):
    if not request.user.has_perm('myapp.change_article'):
        return HttpResponseForbidden("You don't have permission to change articles.")
    # ... view logic ...
    pass

# --- Groups ---
# Assign user to a group (e.g., in admin or programmatically)
# editor_group = Group.objects.get(name='Editors')
# user.groups.add(editor_group)
```

## Custom User Models

*   If the default `User` model isn't sufficient (e.g., you need email as username, different required fields), create a custom user model.
*   **Best Practice:** Do this at the *start* of a project if needed. Changing later is complex.
*   Inherit from `AbstractBaseUser` (for full control) or `AbstractUser` (to keep most default fields/methods).
*   Define required fields (`USERNAME_FIELD`, `REQUIRED_FIELDS`).
*   Create a custom `BaseUserManager`.
*   Set `AUTH_USER_MODEL = 'yourapp.YourUserModel'` in `settings.py`.

## Security Considerations

*   Always use Django's password hashing (`set_password`, `check_password`).
*   Protect views requiring login with `@login_required` or `LoginRequiredMixin`.
*   Use `@permission_required` or `PermissionRequiredMixin` (or manual `has_perm` checks) for authorization.
*   Ensure forms use CSRF protection (`{% csrf_token %}`).

Django's auth system provides a secure and flexible foundation for user management. Leverage the built-in views and forms where possible, and customize the `User` model early if necessary. Always use the provided decorators/mixins for access control.