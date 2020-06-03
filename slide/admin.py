from django.contrib import admin

from .models import Achievement, Profile


# class AchievementAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'start_date', 'end_date', 'visible', 'highlight', 'tag_list']
#     list_display_links = ['title']
#     list_editable = ['visible', 'highlight']
#     list_filter = ['category', 'visible', 'highlight', 'tags']

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')

#     def tag_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['name', 'birth', 'sex',]

# admin.site.register(Achievement, AchievementAdmin) # model class add to admin

# admin.site.register(Profile, ProfileAdmin)




@admin.register(Profile, Achievement)
class DefaultAdmin(admin.ModelAdmin):
    # list_display = 
    pass