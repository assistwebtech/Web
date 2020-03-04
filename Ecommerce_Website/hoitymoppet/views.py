from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Color, Styles, Categories, Lookbook, Lookbookcategories, Slider, Photo, Company, Careinstructions, Privacypolicy, Disclaimer, Terms,UserCart, UserWishList
from django.views.decorators.http import require_http_methods

def get_categ_and_subcateg():
    categories = Categories.objects.filter(parent_category=None)
    categ_dict = {}
    for categ in categories:
        c_list = Categories.objects.filter(parent_category=categ).values()
        categ_dict[categ] = c_list
    return categ_dict

def count_for_wish_and_cart(request):
    cart_items = UserCart.objects.filter(user=request.user).count()
    wishlist_items = UserWishList.objects.filter(user=request.user).count()
    request.session['cart_count'] = cart_items
    request.session['wishlist_count'] = wishlist_items

def index(request):
    sliders = Slider.objects.all()
    if request.user.is_authenticated:
        count_for_wish_and_cart(request)
    context = {'sliders': sliders, 'child_categ': get_categ_and_subcateg()}
    return render(request, "./hoitymoppet/master.html", context)


def category_wise_products(request, id):
    products = Product.objects.filter(categories=id)
    photos = []
    for product in products:
        photos.append({product:Photo.objects.filter(product=product)})
    categories = Categories.objects.filter(parent_category=None)
    categ_dict = {}
    for categ in categories:
        c_list = Categories.objects.filter(parent_category=categ)
        categ_dict[categ]= c_list
    context = {'products': products, 'categories':categories, 'photos': photos, 'child_categ':categ_dict}
    return render(request, "hoitymoppet/category-wise-products.html", context)


@require_http_methods(['GET'])
def productsearch(request):
    q = request.GET.get('q')
    if q:
        products = Product.objects.filter(product_name__icontains=q)
        return render(request, 'hoitymoppet/search-results.html', {'products': products, 'query': q,'child_categ': get_categ_and_subcateg()})
    return render(request, "hoitymoppet/search-results.html" ,{'child_categ': get_categ_and_subcateg()})

@login_required
def add_to_cart(request):
    items = UserCart.objects.filter(user=request.user)
    count = items.count()
    categories = Categories.objects.filter(parent_category=None)
    return render(request, "hoitymoppet/shopping-cart.html", {'categories':categories, 'items':items, 'count':count, 'child_categ': get_categ_and_subcateg()})

# Cart Functionalities
@login_required
def add_product_to_cart(request,id):
    user = request.user
    product = Product.objects.get(id=id)
    product_size = product.age.all()

    # p_size = request.GET['size']
    # print("ssssssssssssssssssssssssssssssssssssssssssssssss", p_size)

    print("The size of the product", product_size)
    # print(a)
    if not UserCart.objects.filter(product_id=product).exists():
        cart = UserCart(user=user, product_id=product)
        cart.save()
    return redirect('productdetails', product.id)

def delete_product_from_cart(request, id):
    item=UserCart.objects.get(id=id)
    if item:
        item.delete()
        cart_items = UserCart.objects.filter(user=request.user).count()
        request.session['cart_count'] = cart_items
    return redirect('addtocart')

def productdetails(request, id):
    product_details = Product.objects.get(id=id)
    prod_photos = Photo.objects.filter(product=id)
    categories = Categories.objects.filter(parent_category=None)
    return render(request, "hoitymoppet/product-details.html", context={'product_details': product_details, 'child_categ': get_categ_and_subcateg(), 'photos':prod_photos})

def company(request):
    companies = Company.objects.all()
    context= {'companies':companies}
    return render(request, "hoitymoppet/company.html", context)

@login_required
def shop(request):
    products = Product.objects.all()
    colors = Color.objects.all()
    styles = Styles.objects.all()
    categories = Categories.objects.all()
    context = {'products':products, 'colors':colors, 'styles':styles, 'categories':categories}
    return render(request, "hoitymoppet/shop.html", context)

def quickview(request, id):
    product_details = Product.objects.get(id=id)
    return render(request, "hoitymoppet/quickview.html", context={'product_details': product_details})

def productcompare(request):
    return render(request, "hoitymoppet/product-compare.html")

@login_required
def productwishlist(request):
    items = UserWishList.objects.filter(user=request.user)
    count = items.count()
    return render(request, "hoitymoppet/product-wishlist.html",{'child_categ': get_categ_and_subcateg(), 'items': items, 'count': count})

@login_required
def addWishList(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    if not UserWishList.objects.filter(product_id=product).exists():
        cart = UserWishList(user=user, product_id=product)
        cart.save()
    return redirect('productdetails', product.id)

@login_required
def deleteWishList(request, id):
    item = UserWishList.objects.get(id=id)
    if item:
        item.delete()
        wishlist_items = UserWishList.objects.filter(user=request.user).count()
        request.session['wishlist_count'] = wishlist_items
    return redirect('productwishlist')

def checkout(request):
    return render(request, "hoitymoppet/checkout.html")

def tracker(request):
    return render(request, "hoitymoppet/tracker.html")

def hoitymoppetlookbook(request):
    lookbooks = Lookbook.objects.all()
    lookbookcategories = Lookbookcategories.objects.all()

    context = {'lookbooks':lookbooks, 'lookbookcategories':lookbookcategories, 'child_categ': get_categ_and_subcateg()}
    return render(request, "hoitymoppet/hoitymoppet-look-book.html", context)

def hoitymoppetlookbookdetails(request, id):
    lookbookdetails = Lookbook.objects.get(id=id)
    categories = Categories.objects.filter(parent_category=None)

    return render(request, "hoitymoppet/hoitymoppet-look-book-details.html", context={'lookbookdetails': lookbookdetails, 'categories':categories})

def hoitymoppetblog(request):
    return render(request, "hoitymoppet/hoitymoppet-blog.html")

def hoitymoppetblogdetails(request):
    return render(request, "hoitymoppet/hoitymoppet-blog-details.html")

def contactus(request):
    return render(request, "hoitymoppet/contact-us.html")

def faq(request):
    return render(request, "hoitymoppet/faq.html")

def careinstructions(request):
    cares = Careinstructions.objects.all()
    context= {'cares':cares}
    return render(request, "hoitymoppet/care-instructions.html", context)

def privacypolicy(request):
    privacypolicies = Privacypolicy.objects.all()
    context= {'privacypolicies':privacypolicies}
    return render(request, "hoitymoppet/privacy-policy.html", context)

def disclaimer(request):
    disclaimers = Disclaimer.objects.all()
    context= {'disclaimers':disclaimers}
    return render(request, "hoitymoppet/disclaimer.html", context)

def termsconditions(request):
    terms = Terms.objects.all()
    context= {'terms':terms}
    return render(request, "hoitymoppet/terms-conditions.html", context)