from django.contrib import admin
from .models import*

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Coment)

admin.site.site_title='Jeans blog administration'
admin.site.site_header='Jeans blog administration'