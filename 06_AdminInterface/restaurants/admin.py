from django.contrib import admin
from restaurants.models import Restaurant, Waiter

class WaiterInlines(admin.StackedInline):
    model = Waiter

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_description', 'count_of_employers', 'serves_pizza']
    list_filter = ['count_of_employers']
    inlines = [WaiterInlines]
    actions = ['pizza_yes', 'pizza_no']

    def get_description(self, object):
        if len(object.description) > 15:
            try:
                return object.description[:15] + '...'
            except:
                return object.description
        else:
            try:
                return object.description[:15]
            except:
                return object.description


    def pizza_yes(self, request, queryset):
        queryset.update(serves_pizza=True)

    def pizza_no(self, request, queryset):
        queryset.update(serves_pizza=False)


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'restaurant', 'cources']
    list_filter = ['age']
    actions = ['has_cources']

    def has_cources(self, request, queryset):
        queryset.update(cources='Курсы не проходил')