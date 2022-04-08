import csv, datetime
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import get_user_model 
from .models import Post, User, Category, Tag , Comments

class UserAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"
    list_filter = ('mobile_number', 'mail','company','designation','state','image',)


class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_date', 'title','category','tag',)
    filter_horizontal = ('tag',) # this works but obviously shows all entries


    def view_on_site(self,obj):
        url = reverse('blogs:post_detail', kwargs={'slug': obj.slug})
        return url


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_filter = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('mail', 'posts',)   

admin.site.register(Post , PostAdmin)
admin.site.register(User , UserAdmin )
admin.site.register(Category , CategoryAdmin)
admin.site.register(Tag , TagAdmin)
admin.site.register(Comments, CommentAdmin)    