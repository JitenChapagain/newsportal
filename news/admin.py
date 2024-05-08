from django.contrib import admin
from .models import Category, Tag, News, slugify

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['en_name', 'np_name', 'slug', 'status']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('en_name', )}

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.en_name)
        obj.save()

class TagAdmin(admin.ModelAdmin):
    list_display = ['en_tag', 'np_tag', 'slug']
    prepopulated_fields = {'slug': ('en_tag', )}
    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.en_tag)
        obj.save()

class NewsAdmin(admin.ModelAdmin):
    list_display = ['en_title', 'np_title', 'category', 'tag', 'published_date', 'status']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('en_title', )}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            # Filter to only include active categories
            kwargs['queryset'] = Category.objects.filter(status=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.en_title)
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(News, NewsAdmin)
