from django.urls import path
from .views import login_view, register_view, logout_view, index_view
from .views import add_artist, hire_artists,admin_dashboard,artist_detail,update_artist,delete_artist

urlpatterns = [
    path("", index_view, name="index"),  # Home Page
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),


    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path("hire-artists/", hire_artists, name="hire_artists"),
    path("add-artist/", add_artist, name="add_artist"),
    path("artist/<int:artist_id>/", artist_detail, name="artist_detail"),  # Dynamic artist detail page
    path("artist/<int:artist_id>/update/", update_artist, name="update_artist"),  # Update artist
    path("artist/<int:artist_id>/delete/", delete_artist, name="delete_artist"), 

]
