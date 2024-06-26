from django.urls import path 

from .views import Listitems,Detailitem,Listcategory,ListUsers,Detailcategory,DetailUsers,ListRecipes,DetailedRecipe

urlpatterns = [
    path('Users/Items/',Listitems.as_view()),
    path('Items/<int:pk>/',Detailitem.as_view()),
    path('Users/',ListUsers.as_view()),
    path('categories/',Listcategory.as_view()),
    path('categories/<int:pk>/',Detailcategory.as_view()),
    path('Users/<int:pk>/',DetailUsers.as_view()),
    path("Recipe/",ListRecipes.as_view()),
    path('Recipe/<int:pk>/',DetailedRecipe.as_view())
] 