from django.urls import path

from .views import * 

app_name = 'site'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact'),
    path('faq/', QuestionsView.as_view(), name='faq'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('terms-conditions/', TermsConditionsView.as_view(), name='terms-conditions'),
]