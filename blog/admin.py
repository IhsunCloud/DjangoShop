from django.contrib import admin

from blog.models import Category, Comment, Post


# class CommentInline(admin.TabularInline):
# 	""" Tabular Inline View for Comments. """

# 	model = Comment
# 	min_num = 3
# 	max_num = 20
# 	extra = 3


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category', 'status', 'created_at')
	search_fields = ('title', 'description')
	list_editable = ('status',)
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'created_at'
	ordering = ('status', 'created_at')
	# fieldsets = (
	# 	('Standard info', {
	# 		'fields': ('title', 'slug', 'author',)
	# 		}),
	# 		('Address info', {
	# 			'fields': ('category', 'image', 'cropping', 'cropping_free',)
	# 			}),
	# 			)

	
	# inlines = [CommentInline]

	def get_changeform_initial_data(self, request):
		get_data = super(PostAdmin, self).get_changeform_initial_data(request)
		get_data['author'] = request.user.pk
		return get_data


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','slug', 'parent','status')
	list_filter = (['status'])
	search_fields = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment)