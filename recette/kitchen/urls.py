from django.conf.urls import patterns, url
from kitchen import views

urlpatterns = patterns('',
    url(r'^$', views.userKitchen,name='index'),
    url(r'^createIngredient/',views.createIngredient,name='createIngredient'),
    url(r'^success/',views.success,name='success'),
    url(r'^addIngredientAmount/',views.addIngredientAmount,name='addIngredientAmount'),
    url(r'^addNewIngredient/',views.addNewIngredient,name='addNewIngredient')
)
