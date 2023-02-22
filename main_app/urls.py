



######

from django.urls import path, re_path
from .views import BookDetailView, BookListView, AuthorDetailView, AuthorListView, HomeView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_app'

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
]




######


#app_name = 'main_app'

#urlpatterns = [
   #path('', home_view.as_view(),name='home'),
   # path('projects/', projects_view.as_view(),name='projects'),
   # path('travel/', travel_view.as_view(),name="travel"),
   # path('thank_you/', thankyou_view.as_view(),name="thank_you"),
   # path('contact/', ContactFormView.as_view(), name="contact"),
   # path('article/<int:pk>', traveldetail_view.as_view(), name="article-detail"),
   # path('aboutme/', aboutme_view.as_view(),name='aboutme'),
   #path('readings/', readings_view.as_view(),name='readings'),
   # path('book/<int:pk>', bookdetail_view.as_view(),name='book-detail'),
#]


