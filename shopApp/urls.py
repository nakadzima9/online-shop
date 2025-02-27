from django.urls import path
from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListUser, DetailUser, ListCart, DetailCart, \
    OrderItemCreateAPIView
from .views import CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('categories/', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('books/', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('users/', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),
    
    path('carts/', ListCart.as_view(), name='carts'),
    path('carts/<int:pk>/', DetailCart.as_view(), name='cartdetail'),
    
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    path('order-item/', OrderItemCreateAPIView.as_view(), name='order-item'),
    
    # path('orders', OrderView.as_view(), name='ordera'),
    # path('orders/<int:pk>/', OrderDetailView.as_view(), name='orderdetail'),
    
]
