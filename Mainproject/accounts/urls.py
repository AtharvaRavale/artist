from django.urls import path
from .views import login_view, register_view, logout_view, index_view
from .views import add_artist, hire_artists,admin_dashboard

urlpatterns = [
    path("", index_view, name="index"),  # Home Page
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),


    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path("hire-artists/", hire_artists, name="hire_artists"),
    path("add-artist/", add_artist, name="add_artist"),
]
