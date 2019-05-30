from django.urls import path
# from django.conf.urls import url
# from .views import home_page
from .views import *

app_name = 'blogapp'
urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('about-us/', AboutView.as_view(), name="about"),
    path('login/', LoginView.as_view(), name="login"),
    path('base1/', BaseView.as_view(), name="base1"),
    path('register/', RegisterView.as_view(), name="register"),
    path('location/', LocationView.as_view(), name="location"),
    path('test/', TestView.as_view(), name="test"),
    path('student/list/', StudentListView.as_view(), name="studentlist"),
    path('student/<int:pk>/detail/',
         StudentDetailView.as_view(), name="studentdetail"),
    path('student/add/', StudentCreateView.as_view(), name="studentcreate"),
    path('student/<int:pk>/delete/',
         StudentDeleteView.as_view(), name="studentdelete"),
    path('student/<int:pk>/update/',
         StudentUpdateView.as_view(), name="studentupdate"),
    path('book/list/', BookListView.as_view(), name="booklist"),
    path('book/<int:pk>/detail/', BookDetailView.as_view(), name="bookdetail"),
    path('book/add', BookCreateView.as_view(), name="bookcreate"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="bookupdate"),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name="bookdelete"),
    path('blog/list/', BlogListView.as_view(), name="bloglist"),
    path('blog/<int:pk>/detail/', BlogDetailView.as_view(), name="blogdetail"),
    path('blog/add/', BlogCreateView.as_view(), name="blogcreate"),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name="blogupdate"),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name="blogdelete"),
    path('search/result', SearchResultView.as_view(), name="searchresult"),

]
