from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Feedback)



header_title = "PTI SERVICOM Admin"
admin.site.site_header = header_title
admin.site.index_title = "PTI SERVICOM Admin"
admin.site.site_title = "PTI SERVICOM Admin"