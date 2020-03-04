from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    re_path( r'^login/$',auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    # path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    # path('logout/', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page= 'index'), name='logout'),
    path("orderhistory", views.orderhistory, name="orderhistory"),
    path("profile", views.profile, name="profile"),

    path("password", views.change_password, name="change_password"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='./accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('social-auth/', include('social_django.urls', namespace="social")),

    path("myorders", views.myorders, name="myorders"),
    path("myorderdetails", views.myorderdetails, name="myorderdetails"),
    path("mywishlist", views.mywishlist, name="mywishlist"),
    path("childinformation", views.childinformation, name="childinformation"),
    path("manageaddress", views.manageaddress, name="manageaddress"),
    path("pancardinformation", views.pancardinformation, name="pancardinformation"),
    path("aadharcardinformation", views.aadharcardinformation, name="aadharcardinformation"),
    path("deleteaddress/<int:id>", views.address_delete, name="delete-address"),
    path("deletechild/<int:id>", views.childs_delete, name="delete-child"),

    # path("edit/<int:id>", views.address_edit, name="edit-address"),
]