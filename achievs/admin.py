from django.contrib import admin
from achievs.models import Achievement
# from achievs.models import Gold
# from achievs.models import Silver
# from achievs.models import Bronze
# from achievs.models import Platinum
from achievs.models import Level

# class PlatinumInline(admin.StackedInline):
	# model=Platinum
	
# class GoldInline(admin.StackedInline):
	# model=Gold
	
# class SilverInline(admin.StackedInline):
	# model=Silver

# class BronzeInline(admin.StackedInline):
	# model=Bronze

class LevelInline(admin.StackedInline):
	model=Level

class AchievementAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date']}),
	]
	#inlines=[GoldInline, SilverInline, BronzeInline, PlatinumInline]
	inlines=[LevelInline]
	list_display = ('name', 'pub_date')
	list_filter=['pub_date']
	search_fields=['name']
	date_hierarchy='pub_date'

# admin.site.register(Gold)
# admin.site.register(Silver)
# admin.site.register(Bronze)
# admin.site.register(Platinum)
admin.site.register(Level)
admin.site.register(Achievement, AchievementAdmin)