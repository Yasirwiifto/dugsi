
from django.contrib import admin
from django.urls import path
from dugsi.views import arday

urlpatterns = [
    path('dugsi/', arday, name="arday"),
    path('admin/', admin.site.urls),
]
