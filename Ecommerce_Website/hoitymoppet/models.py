from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Color(models.Model):
    color         = models.CharField(max_length=30)
    parent_color  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='pcolor')

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.__str__()

class Age(models.Model):
    age = models.CharField(max_length=20)

    def __str__(self):
        return str(self.age) +' year'

    def __repr__(self):
        return self.__str__()

class Stockdetails(models.Model):
    stock = models.CharField(max_length=255)

    def __str__(self):
        return self.stock

    def __repr__(self):
        return self.__str__()

class Styles(models.Model):
    style_name    = models.CharField(max_length=255)
    parent_style  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='pstyle')

    def __str__(self):
        return self.style_name

    def __repr__(self):
        return self.__str__()

class Fabric(models.Model):
    fabric = models.CharField(max_length=255)
    fabric_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fabric

    def __repr__(self):
        return self.__str__()

class Categories(models.Model):
    category         = models.CharField(max_length=255)
    parent_category  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='pcategory')

    def __str__(self):
        return self.category

    def __repr__(self):
        return self.__str__()

class Product(models.Model):
    product_name        = models.CharField(max_length=255)
    categories          = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_fabric      = models.ForeignKey(Fabric, on_delete=models.CASCADE, null=True, blank=True)
    age                 = models.ManyToManyField(Age)
    style               = models.ForeignKey(Styles, on_delete=models.CASCADE, null=True,blank=True)
    color               = models.ManyToManyField(Color, null=True, blank=True)
    item_detail         = models.TextField(default="")
    style_code          = models.CharField(max_length=255, default="")
    care_instructions   = models.TextField(null=True, blank=True, default="")
    price               = models.FloatField()
    stock               = models.ForeignKey(Stockdetails, on_delete=models.CASCADE, default=1)
    # custom_size         = models.ForeignKey(UserCustomSize, on_delete=models.CASCADE, null=True, blank=True)
    productimage        = models.ImageField(upload_to="hoitymoppet/productimages", default="")
    def __str__(self):
        return self.product_name

    def __repr__(self):
        return self.__str__()

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='product')
    image = models.ImageField(upload_to='hoitymoppet/productimages')

class Lookbookcategories(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def __repr__(self):
        return self.__str__()

class Lookbook(models.Model):
    lookbook_name = models.CharField(max_length=255)
    lookbook_summary = models.TextField(max_length=255, default="")
    # lookbook_details = models.TextField(default="")
    lookbook_details = RichTextUploadingField()
    lookbook_image = models.ImageField(upload_to="hoitymoppet/lookbookimages", default="")

    def __str__(self):
        return self.lookbook_name

    def __repr__(self):
        return self.__str__()

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_summary = models.TextField(max_length=255, default="")
    # company_details = models.TextField(default="")
    company_details = RichTextUploadingField()
    company_image = models.ImageField(upload_to="hoitymoppet/companyimages", default="")

class Slider(models.Model):
    parent_category = [('shop', 'Shop'), ('girls', 'Girls'), ('baby', 'Baby'),('accessories', 'Accessories'),('sale', 'Sale'),('offers', 'Offers')]
    slider_name = models.CharField(max_length=255)
    slider_summary = models.TextField(max_length=255, default="")
    slider_details = models.TextField(default="")
    slider_image = models.ImageField(upload_to="hoitymoppet/sliderimages", default="")
    slider_category = models.CharField(max_length=20, choices=parent_category)

    def __str__(self):
        return self.slider_name

    def __repr__(self):
        return self.__str__()

class Careinstructions(models.Model):
    cares_name = models.CharField(max_length=255)
    # cares_details = models.TextField(default="")
    cares_details = RichTextUploadingField()

class Privacypolicy(models.Model):
    privacypolicy_name = models.CharField(max_length=255)
    # privacypolicy_details = models.TextField(default="")
    privacypolicy_details = RichTextUploadingField()

class Disclaimer(models.Model):
    disclaimer_name = models.CharField(max_length=255)
    # disclaimer_details = models.TextField(default="")
    disclaimer_details = RichTextUploadingField()

class Terms(models.Model):
    terms_name = models.CharField(max_length=255)
    # terms_details = models.TextField(default="")
    terms_details = RichTextUploadingField()

class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=20)
    quantity = models.IntegerField('Quantity', default = 1)
    total_price = models.FloatField("Total Price", blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class UserWishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class UserCustomSize(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    soulder_to_apex = models.CharField(max_length=255, null=True, blank=True)
    cap_sleeve_length = models.CharField(max_length=255, null=True, blank=True)
    short_sleeve_length = models.CharField(max_length=255, null=True, blank=True)
    three_fourth_to_apex = models.CharField(max_length=255, null=True, blank=True)
    full_sleeve_length = models.CharField(max_length=255, null=True, blank=True)
    knee_round = models.CharField(max_length=255, null=True, blank=True)
    calf = models.CharField(max_length=255, null=True, blank=True)
    ankle_round = models.CharField(max_length=255, null=True, blank=True)
    waist_length = models.CharField(max_length=255, null=True, blank=True)
    neck_round = models.CharField(max_length=255, null=True, blank=True)
    front_neck_depth = models.CharField(max_length=255, null=True, blank=True)
    cross_front = models.CharField(max_length=255, null=True, blank=True)
    bust = models.CharField(max_length=255, null=True, blank=True)
    under_bust = models.CharField(max_length=255, null=True, blank=True)
    waist = models.CharField(max_length=255, null=True, blank=True)
    lower_waist = models.CharField(max_length=255, null=True, blank=True)
    wrist = models.CharField(max_length=255, null=True, blank=True)
    thigh_round = models.CharField(max_length=255, null=True, blank=True)
    lower_thigh = models.CharField(max_length=255, null=True, blank=True)
    arm_hole = models.CharField(max_length=255, null=True, blank=True)
    knee_length = models.CharField(max_length=255, null=True, blank=True)
    full_length = models.CharField(max_length=255, null=True, blank=True)
    shoulder = models.CharField(max_length=255, null=True, blank=True)
    back_neck_depth = models.CharField(max_length=255, null=True, blank=True)
    biceps = models.CharField(max_length=255, null=True, blank=True)
    elbow_round = models.CharField(max_length=255, null=True, blank=True)
    hips = models.CharField(max_length=255, null=True, blank=True)
    bottom_length = models.CharField(max_length=255, null=True, blank=True)




