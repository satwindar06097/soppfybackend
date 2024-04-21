from django.urls import path
from base.views import product_views as views


urlpatterns = [
    
    path('', views.getProducts, name='products'),
    path('create/', views.createProduct, name='create-product'),
    path('upload/',views.uploadImage, name = 'image-upload'),

    path('<str:pk>/reviews/', views.createProductReview, name='create-reviews'),
    path('top/',views.getTopProducts,name='top-product'),
    path('<str:pk>/', views.getProduct, name='product'),
    
    path('update/<str:pk>/', views.updateProduct, name='product-update'),
    path('delete/<str:pk>/', views.deleteProduct, name='product-delete'),
    
]
