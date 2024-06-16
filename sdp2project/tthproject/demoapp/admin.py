from django.contrib import admin
from .models import Customer, LoginInfo, Admin, Book, FeedBack

admin.site.register(Customer)
admin.site.register(LoginInfo)
admin.site.register(Admin)
admin.site.register(FeedBack)
admin.site.register(Book)

