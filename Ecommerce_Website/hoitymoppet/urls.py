from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:id>", views.category_wise_products, name="category-wise-products"),
    path("company/", views.company, name="company"),
    path("shop/", views.shop, name="shop"),
    path("quickview/<int:id>", views.quickview, name="quickview"),
    path("productdetails/<int:id>", views.productdetails, name="productdetails"),
    path("productcompare/", views.productcompare, name="productcompare"),
    path("checkout/", views.checkout, name="checkout"),
    path("tracker/", views.tracker, name="tracker"),
    path("hoitymoppetlookbook/", views.hoitymoppetlookbook, name="hoitymoppetlookbook"),
    path("hoitymoppetlookbookdetails/<int:id>", views.hoitymoppetlookbookdetails, name="hoitymoppetlookbookdetails"),
    path("hoitymoppetblog/", views.hoitymoppetblog, name="hoitymoppetblog"),
    path("hoitymoppetblogdetails/", views.hoitymoppetblogdetails, name="hoitymoppetblogdetails"),
    path("contactus/", views.contactus, name="contactus"),
    path("faq/", views.faq, name="faq"),
    path("careinstructions/", views.careinstructions, name="careinstructions"),
    path("privacypolicy/", views.privacypolicy, name="privacypolicy"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("termsconditions/", views.termsconditions, name="termsconditions"),
    path("productsearch/", views.productsearch, name="productsearch"),

    path("addtocart/", views.add_to_cart, name="addtocart"),
    path("addcart/<int:id>", views.add_product_to_cart, name="update-cart"),
    path("deletecartitem/<int:id>", views.delete_product_from_cart, name="delete-cart-item"),


    path("addusercustomsize/<int:id>", views.add_user_custom_size, name="add-user-custom-size"),


    path("productwishlist/", views.productwishlist, name="productwishlist"),
    path("addwishlist/<int:id>", views.addWishList, name="add-wishlist"),
    path("deletewishlist/<int:id>", views.deleteWishList, name="delete-wishlist"),
]