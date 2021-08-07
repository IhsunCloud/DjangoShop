from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from shop.models import Category, Color, Comment, Image, Product


class ImageInline(admin.TabularInline):
	""" Tabular Inline View for Images. """
	
	model = Image
	min_num = 3
	max_num = 20
	extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'status', 'color', 'created_at')
	search_fields = ('title', 'description')
	list_editable = ('status',)
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'created_at'
	ordering = ('status', 'created_at')
	
	inlines = [ImageInline]

	def get_changeform_initial_data(self, request):
		get_data = super(ProductAdmin, self).get_changeform_initial_data(request)
		get_data['author'] = request.user.pk
		return get_data


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','slug', 'parent','status')
	list_filter = (['status'])
	search_fields = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment),
admin.site.register(Image),
admin.site.register(Color),