from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddressForm
from django.contrib.auth.models import User
from .models import Profile, Address, Child
import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from hoitymoppet.views import get_categ_and_subcateg

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, './accounts/signup.html', {'form': form, 'child_categ': get_categ_and_subcateg()})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required
def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_contact_number = request.POST.get('user_contact_number',0)
        user_sex = request.POST.get('user_sex',False)
        email = request.POST.get('email')
        current_user = User.objects.get(id=request.user.id)
        if current_user:
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.email = email
            current_user.save()
        profile = Profile.objects.get(user=current_user)
        profile.user_sex = user_sex
        profile.user_contact_number = user_contact_number
        profile.save()
        return render(request, './accounts/profile.html')
    return render(request, './accounts/profile.html')


def login(request, user):
    return render(request, './accounts/login.html')


def orderhistory(request):
    return render(request, './accounts/order-history.html')


@login_required
def changepassword(request):
    return render(request, './accounts/change_password.html')


def resetpassword(request):
    return render(request, './accounts/password_reset.html')


@login_required
def myorders(request):
    return render(request, './accounts/my-orders.html')

@login_required
def myorderdetails(request):
    return render(request, './accounts/my-order-details.html')


@login_required
def mywishlist(request):
    return render(request, './accounts/my-wishlist.html')

@login_required
def manageaddress(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        pincode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        landmark = request.POST.get('landmark')
        alternate_no = request.POST.get('alternate_no')
        if not id:
            if name and mobile_no:
                addres = {
                    'user':request.user,
                    'name': name,
                    'mobile_no':mobile_no,
                    'pincode':pincode,
                    'locality':locality,
                    'address':address,
                    'state':state,
                    'city':city,
                    'landmark':landmark,
                    'alternate_no':alternate_no,
                }
                address = Address(**addres)
                address.save()
                objs = Address.objects.filter(user=request.user)
                return render(request, './accounts/manage-address.html', context={'addresses':objs})
        else:
            addr = get_object_or_404(Address, id=id)
            addr.name = name
            addr.mobile_no = mobile_no
            addr.pincode = pincode
            addr.locality = locality
            addr.address = address
            addr.state = state
            addr.city = city
            addr.landmark = landmark
            addr.alternate_no = alternate_no
            addr.save()
            objs = Address.objects.filter(user=request.user)
            return render(request, './accounts/manage-address.html', context={'addresses': objs})
    objs = Address.objects.filter(user=request.user)
    return render(request, './accounts/manage-address.html', context={'addresses': objs})

@login_required
def childinformation(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        child_name = request.POST.get('child_name')
        child_birth_date = request.POST.get('child_birth_date')
        if not id:
            if child_name and child_birth_date:
                chil = {
                    'user': request.user,
                    'child_name': child_name,
                    'child_birth_date': datetime.datetime.strptime(child_birth_date,'%m/%d/%Y'),
                }
                childinformation = Child(**chil)
                childinformation.save()
                objc = Child.objects.filter(user=request.user)
                return render(request, './accounts/child-information.html', context={'childinformations': objc})
        else:
            chill = get_object_or_404(Child, id=id)
            chill.child_name = child_name
            chill.child_birth_date = datetime.datetime.strptime(child_birth_date,'%m/%d/%Y')
            chill.save()
            objc = Child.objects.filter(user=request.user)
            return render(request, './accounts/child-information.html', context={'childinformations': objc})
    objc = Child.objects.filter(user=request.user)
    return render(request, './accounts/child-information.html', context={'childinformations': objc})


@login_required
def address_delete(request, id):
    obj = get_object_or_404(Address, id=id)
    obj.delete()
    return redirect('manageaddress')


@login_required
def childs_delete(request, id):
    obj = get_object_or_404(Child, id=id)
    obj.delete()
    return redirect('childinformation')


@login_required
def pancardinformation(request):
    if request.method == 'POST':
        pancard_name = request.POST.get('pancard_name')
        pancard_number = request.POST.get('pancard_number')
        current_user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=current_user)
        profile.pancard_name = pancard_name
        profile.pancard_number = pancard_number
        profile.save()
        return render(request, './accounts/pan-card-information.html')
    return render(request, './accounts/pan-card-information.html')


@login_required
def aadharcardinformation(request):
    if request.method == 'POST':
        aadharcard_name = request.POST.get('aadharcard_name')
        aadharcard_number = request.POST.get('aadharcard_number')
        current_user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user=current_user)
        profile.aadharcard_name = aadharcard_name
        profile.aadharcard_number = aadharcard_number
        profile.save()
        return render(request, './accounts/aadhar-card-information.html')
    return render(request, './accounts/aadhar-card-information.html')


# def address_edit(request, id):
#     if request.method=='POST':
#         id = request.POST.get('id')
#         addr = get_object_or_404(Address, id=id)
#         addr.name = request.POST.get('name')
#         addr.mobile_no = request.POST.get('mobile_no')
#         addr.pincode = request.POST.get('pincode')
#         addr.locality = request.POST.get('locality')
#         addr.address = request.POST.get('address')
#         addr.state = request.POST.get('state')
#         addr.city = request.POST.get('city')
#         addr.landmark = request.POST.get('landmark')
#         addr.alternate_no = request.POST.get('alternate_no')
#         addr.save()
#         return redirect('manageaddress')
#     return render(request, './accounts/edit-address.html', context={'address': addr})


# def child_edit(request, id):
#     address= get_object_or_404(Child, id=id)
#     form = ChildForm(request.POST or None, instance=address)
#     if form.is_valid():
#         form.save()
#         return redirect('manageaddress')
#     objs = Address.objects.filter(user=request.user)
#     return render(request, './accounts/manage-address.html', context={'addresses': objs})