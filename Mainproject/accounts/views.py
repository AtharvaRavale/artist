from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm



def index_view(request):
    """Render Home Page"""
    return render(request, "accounts/index.html")



def register_view(request):
    """Handles user registration"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page after registering
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    """Handles user login"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")  # Redirect to home page after login
    return render(request, "accounts/login.html")

def logout_view(request):
    """Handles user logout"""
    logout(request)
    return redirect("login")



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Artist
from .forms import ArtistForm

# Function to check if user is admin
def is_admin(user):
    return user.is_staff  # Only admin can access

@login_required
@user_passes_test(is_admin)
def add_artist(request):
    """Allow only admin to add an artist"""
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.added_by = request.user
            artist.save()
            return redirect("hire_artists")
    else:
        form = ArtistForm()
    return render(request, "accounts/add_artist.html", {"form": form})

def hire_artists(request):
    """Show available artists"""
    artists = Artist.objects.all()
    return render(request, "accounts/hire_artists.html", {"artists": artists})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# Function to check if the user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_superuser

def admin_login(request):
    """Custom admin login view"""
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_dashboard')  # Redirect if already logged in

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            return render(request, 'accounts/admin_login.html', {'error': 'Invalid credentials or not an admin'})

    return render(request, 'accounts/admin_login.html')

@login_required
@user_passes_test(is_admin)  # Only admins can access this page
def admin_dashboard(request):
    """Admin dashboard view"""
    return render(request, 'accounts/admin_dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_logout(request):
    """Logout admin and redirect to login"""
    logout(request)
    return redirect('admin_login')


def artist_detail(request, artist_id):
    """Display artist details dynamically"""
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, "accounts/artist_detail.html", {"artist": artist})





@login_required
@user_passes_test(is_admin)
def update_artist(request, artist_id):
    """Allow admin to update artist details"""
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect("artist_detail", artist_id=artist.id)
    else:
        form = ArtistForm(instance=artist)

    return render(request, "accounts/update_artist.html", {"form": form, "artist": artist})

@login_required
@user_passes_test(is_admin)
def delete_artist(request, artist_id):
    """Allow admin to delete an artist"""
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == "POST":
        artist.delete()
        return redirect("hire_artists")

    return render(request, "accounts/delete_artist.html", {"artist": artist})