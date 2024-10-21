from django.contrib import admin
from django.urls import path
from inventoryapp.views import GetItems,Item
import inventoryapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('items',inventoryapp.views.GetItems.as_view(),name='get_items'),   #CBV
    # path('item/<int:pk>',inventoryapp.views.Item.as_view(),name='item'),    #CBV
    path('items',inventoryapp.views.GetItems,name='get_items'),   #FBV
    path('item/<int:pk>',inventoryapp.views.Item,name='item'),    #FBV
]
