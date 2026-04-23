
# app1/urls.py
from django.urls import path
from .views import (
    SignupPage,
    login_view,
    HomePage,
    LogoutPage,
    assessment_view,
    profile_view,
    search_view,
    contact_view,
    about_view,
    thank_you,
    generate_test,
    resume_builder_view,
    career_form_view,
    career_recommendation,
    dashboard_view,
    live_chat_view,
    career_result_view,
    ai_career_assistant,
    IndustryTrendsAPIView,
    news_feed_page
)

# You can optionally add app_name for namespacing if you need it
# app_name = 'app1'

urlpatterns = [
    # --- Main Application URLs ---
    path('', SignupPage, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/', LogoutPage, name='logout'),
    path('assessment/', assessment_view, name='assessment'),
    path('profile/', profile_view, name='profile_view'),
    path('search/', search_view, name='search'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('thankyou/', thank_you, name='thankyou'),
    path('test/<str:test_type>/', generate_test, name='generate_test'),
    path('resume-builder/', resume_builder_view, name='resume_builder'),
    path('livechat/', live_chat_view, name='live_chat'),
    path('career_result/', career_result_view, name='career_result'),

    # --- Career Recommendation URLs ---
    path('career_form/', career_form_view, name='career_form'),
    path('recommend/', career_recommendation, name='career_recommend'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # --- AI Career Assistant URL ---
    path('startchat/', ai_career_assistant, name='start_chat'),

    # --- Industry Trends & Insights Feed URLs ---
    path('api/trends/', IndustryTrendsAPIView.as_view(), name='api_industry_trends'),
    path('trends/', news_feed_page, name='industry_trends_page'),

    path('startchat/',ai_career_assistant, name='start_chat'),

    

]