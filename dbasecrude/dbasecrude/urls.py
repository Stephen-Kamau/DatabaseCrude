from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include

urlpatterns = [
    url('admin/', admin.site.urls),
    # url('', views.emp),
    url('^emp/', include('employee.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('emp', views.emp),
#     path('show',views.show),
#     path('edit/<int:id>', views.edit),
#     path('update/<int:id>', views.update),
#     path('delete/<int:id>', views.destroy),
# ]
