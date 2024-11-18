# from django.contrib import admin
# from .models import Stock, StockData

# class StockAdmin(admin.ModelAdmin):
#     search_fields = ('id', 'name', 'symbol')

# admin.site.register(Stock, StockAdmin)
# admin.site.register(StockData)

from django.contrib import admin
from .models import Stock, StockData

# Inline for StockData to be displayed on the Stock admin page
class StockDataInline(admin.TabularInline):
    model = StockData
    extra = 1  # Allows adding one extra StockData in the inline form
    fields = ('current_price', 'price_changed', 'percentage_changed', 'previous_close', 'week_52_high', 'week_52_low', 'market_cap', 'pe_ratio', 'dividend_yield')
    readonly_fields = ('current_price', 'price_changed', 'percentage_changed')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'sector', 'exchange', 'country')
    search_fields = ('name', 'symbol', 'sector', 'exchange', 'country')
    list_filter = ('sector', 'exchange', 'country')
    inlines = [StockDataInline]

@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ('stock', 'current_price', 'price_changed', 'percentage_changed', 'previous_close', 'week_52_high', 'week_52_low', 'market_cap', 'pe_ratio', 'dividend_yield')
    search_fields = ('stock__name', 'stock__symbol')
    list_filter = ('stock__sector', 'stock__exchange')
    readonly_fields = ('current_price', 'price_changed', 'percentage_changed')  # Mark these fields as readonly
