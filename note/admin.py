from django.contrib import admin

from .models import NotesModel

# class NotesAdmin(admin.ModelAdmin):
#     class Meta:
#         model = NotesModel
# class NotesAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['title']}),
#     ]
    
admin.site.register(NotesModel)

