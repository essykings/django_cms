from django.urls import path
from .views import add_stories,stories,StoryUpdateView,StoryDetailView

urlpatterns = [
    path('add',add_stories, name = "add_story"),
    # path('stories', stories, name = "stories"),
    # path('stories/<pk>', StoryUpdateView.as_view(),name = "story"),
    # path('story_detail/<pk>', StoryDetailView.as_view(),name = "story_detail")
]


