from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from datetime import date


from .models import Idea,Category

class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30

admin.site.register(Category, CustomMPTTModelAdmin)

class YearIdeaFilter(admin.SimpleListFilter):
    # name of the filter to display
    title = "Year created"
    # name for what we a filtering 
    parameter_name = "year"
    def lookups(self, request, modeladmin):
        """create a clickable link on the right side"""
        # one goes to the url,another appears in the sidebar
        # url = parameter_name + [0] from the lookups
        return (
            (2019,2019),
            (2018,2018)
        )
    def queryset(self,request,queryset):
        if self.value() == '2019':
            return queryset.filter(created_at__gte=date(2019,1,1),
                                    created_at__lte = date(2019,12,31)
            )   
        if self.value() == '2018':
            return queryset.filter(created_at__gte=date(2018,1,1),
                                    created_at__lte = date(2018,12,31)
            )   

def make_published(modeladmin,request,queryset):
    """make possbile to mark idea as published in admin bar checkbox"""
    queryset.update(status=2)

make_published.short_description = 'Mark idea as published'    



# group fields in fieldsets
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ('title','lead_text','main_text')
    list_filter = ('created_at','is_public',YearIdeaFilter,'tags')
    list_display = ['id','title','author','status','is_public','created_at']
    list_editable = ['status']
    list_display_links = ['title']
    fieldsets = (
        # I don't need it
        (None,{'fields':('author','title','categ',
        'lead_text','main_text','status')}),
        # should be present for clearity
        ('Not required Fields',
        {
            'fields':('featured','view_count','likes','dislikes','is_public','thumbnail','tags'),
            'classes':('collapse',)
        },
        )
    )
    radio_fields = {'categ':admin.HORIZONTAL}
    actions = [make_published]

admin.site.register(Idea,IdeaAdmin)


# check it (below) out
# @admin.register(Comment)
# class IdeaAdmin(admin.ModelAdmin):
#     list_display = ('title', 'id', 'status', 'slug', 'author')
#     prepopulated_fields = {'slug': ('title',), }

