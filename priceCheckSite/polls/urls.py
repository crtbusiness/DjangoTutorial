from django.urls import path

from . import views

# urlpatterns = [
#     #ex: /polls/
#     path("", views.index, name="index"),
#     #ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("specifics/<int:question_id>/", views.detail, name="detail"),
#     #ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     #ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

#I'm just gonna copy the next big block of text because it is all pretty useful
#Take a look in your browser, at “/polls/34/”. It’ll run the detail() method and display whatever ID you provide in the URL. Try “/polls/34/results/” and “/polls/34/vote/” too – these will display the placeholder results and voting pages.

#When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so:
#detail(request=<HttpRequest object>, question_id=34)

#The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The question_id part of the string defines the name that will be used to identify the matched pattern, and the int part is a converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
#since this is in polls, it's taking the number of the question or poll,
#and matching it to the primary key for that question, and that's how you get the url





# app_name = "polls"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]
#Better way to do the above, this groups the urls under a Namespace, or category for the polls app
#to keep things better organized