from django.urls import path
from .views import ProjectListView, ProjectDetailView, ReviewCreateView, CategoryListView, AboutView, ContactView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='review_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
