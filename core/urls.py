from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.ProblemList.as_view(), name='problemList'),
    path('problem_details/<slug>', views.problemDetails.as_view(), name='problem_details'),
    path('post_comment/<int:pk>', views.post_comments, name='post_comment'),
    path('predict/', views.predict_chances, name='predict')
]

