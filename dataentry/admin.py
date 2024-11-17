from django.contrib import admin
from .models import Student, Customer, Employee


# Custom Admin for Student Model
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'age')  # Columns to display in the list view
    search_fields = ('name', 'roll_no')  # Add a search bar to search by name or roll_no
    list_filter = ('age',)  # Filter by age
    ordering = ('age',)  # Order students by age


# Custom Admin for Customer Model
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'country')  # Columns to display in the list view
    search_fields = ('customer_name', 'country')  # Add a search bar to search by name or country
    list_filter = ('country',)  # Filter by country
    ordering = ('customer_name',)  # Order by customer_name


# Custom Admin for Employee Model
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'designation', 'salary', 'retirement', 'other_benefits', 'total_benefits', 'total_compensation')  # Include 'other_benefits' and 'total_benefits' here
    search_fields = ('employee_name', 'employee_id')  # Search by employee name or ID
    list_filter = ('designation',)  # Filter by designation
    ordering = ('employee_name',)  # Order employees by employee_name
    list_editable = ('salary', 'other_benefits', 'total_benefits', 'total_compensation')  # Make these fields editable in the list view


# Register the models with their custom admin classes
admin.site.register(Student, StudentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
