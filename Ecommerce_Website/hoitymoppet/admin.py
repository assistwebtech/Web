from django.contrib import admin
from .models import (Color,
                     Fabric,
                     Styles,
                     Categories,
                     Stockdetails,
                     Product,
                     Age,
                     Lookbookcategories,
                     Lookbook,
                     Slider,
                     Photo,
                     Company,
                     Careinstructions,
                     Privacypolicy,
                     Disclaimer,
                     Terms,
                     UserCart,
                     UserCustomSize
                     )

admin.site.site_header = 'Hoitymoppet Admin'

class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'parent_color')

class FabricAdmin(admin.ModelAdmin):
    list_display = ('id', 'fabric', )

class StylesAdmin(admin.ModelAdmin):
    list_display = ('id','style_name', 'parent_style')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'parent_category')

class AgeAdmin(admin.ModelAdmin):
    list_display = ('id','age', )

class StockdetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock')

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'categories','ages', 'style', 'item_detail', 'style_code', 'care_instructions', 'price', 'stock', 'productimage', 'color')
    inlines = [PhotoInline]

    def ages(self, obj):
        return "\n".join([str(p.age) for p in obj.age.all()])

    def color(self, obj):
        return "\n".join([p.color for p in obj.color.all()])

    def categories(self, obj):
        return "\n".join([p.categories for p in obj.categories.all()])

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(product=obj, image=afile)


class UserCustomSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_id', 'create_date', 'modified_date', 'soulder_to_apex', 'cap_sleeve_length', 'short_sleeve_length', 'three_fourth_to_apex', 'full_sleeve_length', 'knee_round')

class LookbookcategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

class LookbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'lookbook_name', 'lookbook_summary', 'lookbook_details')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'company_summary', 'company_details')

class CareinstructionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cares_name', 'cares_details')

class PrivacypolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'privacypolicy_name', 'privacypolicy_details')

class DisclaimerAdmin(admin.ModelAdmin):
    list_display = ('id', 'disclaimer_name', 'disclaimer_details')

class TermsAdmin(admin.ModelAdmin):
    list_display = ('id', 'terms_name', 'terms_details')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'slider_name', 'slider_summary', 'slider_details', 'slider_image')



admin.site.register(Color, ColorAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(Styles, StylesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Age, AgeAdmin)
admin.site.register(Stockdetails, StockdetailsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Lookbookcategories, LookbookcategoriesAdmin)
admin.site.register(Lookbook, LookbookAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Photo)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Careinstructions, CareinstructionsAdmin)
admin.site.register(Privacypolicy, PrivacypolicyAdmin)
admin.site.register(Disclaimer, DisclaimerAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(UserCart)
admin.site.register(UserCustomSize, UserCustomSizeAdmin)