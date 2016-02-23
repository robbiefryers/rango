from django.conf.urls import patterns, url
from rango import views

#Notes to self $ and ^ are regular expression characters that have special meaning
#The caret means that the pattern must match the start of the string eg rango/hisabout would still load the about page without it
#The dollar means that the pattern must match the end of the string eg rango/aboutblahblah would still load the about page without it 

#The 'r' in front of each regular expression string is optional but recommended.
#It tells Python that a string is "raw" - that nothing in the string should be escaped.


#For the 4th entry in the list 
#the second parameter comes from the parenthesis inserted in urls.py (?P<category_name_slug>[\w\-]+)
#Parenthesis around anything will create new arguments that are passed to views.py

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)  # New!)