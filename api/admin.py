from django.contrib import admin
from .models import NewsletterSubscription, Contact, Portfolio, PortfolioImage

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('email',)
    date_hierarchy = 'created_at'

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'include_user_email')
    list_filter = ('include_user_email',)
    search_fields = ('name', 'email', 'subject')

admin.site.register(Contact, ContactAdmin)

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]
    list_display = ('title', 'category', 'link')
    list_filter = ('category',)
    search_fields = ('title', 'description')

admin.site.register(Portfolio, PortfolioAdmin)