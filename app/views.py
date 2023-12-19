from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    #defaultly my data will be order in the form of Insertion Order, Bcz which way we will insert data like that only dispaly the all data
    QLTO=Topic.objects.all()
    #Now I Want My data in the form of ascending order so,
    QLTO=Topic.objects.all().order_by('topic_name')
    # or
    #QLTO=Topic.objects.order_by('topic_name')
    #Now I Want My data in the form of descending order so,
    QLTO=Topic.objects.all().order_by('-topic_name')

    #Now i dont want data numbers, ascii values in the form of asc or desc order of with the help of length function so, import length fun
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    #Now i dont want data numbers, ascii values in the form of asc or desc order of with the help of length function so, import length fun
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    #it will remove the specific data from the col
    #QLTO=Topic.objects.exclude(topic_name='FootBall')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    #defaultly my data will be order in the form of Insertion Order, Bcz which way we will insert data like that only dispaly the all data
    QLWO=Webpage.objects.all()
    #Now I Want My data in the form of ascending order so,
    QLWO=Webpage.objects.order_by('name')
    #Now I Want My data in the form of Descending order so,
    QLWO=Webpage.objects.order_by('-name')
    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)