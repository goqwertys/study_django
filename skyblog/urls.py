from django.urls import path
from skyblog.apps import SkyblogConfig

from skyblog.views import HomePostListView

app_name = SkyblogConfig.name

urlpatterns = [
    path('', HomePostListView.as_view(), name='home'),
]
