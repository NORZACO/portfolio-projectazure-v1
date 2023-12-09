from django.urls import path


from .views import index_Views


urlpatterns = [
    path("", index_Views.index, name="Home"),
    path("contact", index_Views.contact, name="contact"),
    path("about", index_Views.about, name="about"),
    path("property_grid", index_Views.property_grid, name="property_grid"),
    path("property_single", index_Views.property_single, name="property_single"),
    path('property-single/<int:property_id>', index_Views.property_single, name="property_single"),
    path("search_properties", index_Views.search_properties, name="search_properties"),
]


# urlpatterns += [
#     path("add-to-cart", cart_Views.add_to_cart, name="add_to_cart"),
#     path("delete-from-cart", cart_Views.delete_from_cart, name="cart_delete"),
#     path("update-cart", cart_Views.update_cart, name="cart_update"),
#     path("cart_summary", cart_Views.cart_summary, name="cart_summary"),
#     path("single-product/<int:single_product_id>/", cart_Views.single_product, name="single_product"),
# ]
