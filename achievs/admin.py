from django.contrib import admin
from achievs.models import Achievement
from achievs.models import Gold
from achievs.models import Silver
from achievs.models import Bronze

class GoldInline(admin.StackedInline):
	model=Gold
	
class SilverInline(admin.StackedInline):
	model=Silver

class BronzeInline(admin.StackedInline):
	model=Bronze

class AchievementAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
	]
	inlines=[GoldInline, SilverInline, BronzeInline]
	list_display = ('name', 'pub_date')
	list_filter=['pub_date']
	search_fields=['name']
	date_hierarchy='pub_date'

admin.site.register(Gold)
admin.site.register(Silver)
admin.site.register(Bronze)
admin.site.register(Achievement, AchievementAdmin)