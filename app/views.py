from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q #1st import Q-objects from models

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


    ### Here, Field lookup ####
    #here, except cricket remaining we want to check with the help of lookup greater
    QLTO=Topic.objects.filter(topic_name__gt='Cricket')
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

    
def display_webpages(request):
    #defaultly my data will be order in the form of Insertion Order, Bcz which way we will insert data like that only dispaly the all data
    QLWO=Webpage.objects.all()
    #Now I Want My data in the form of ascending order so,
    QLWO=Webpage.objects.order_by('name')
    #Now I Want My data in the form of Descending order so,
    QLWO=Webpage.objects.order_by('-name')

    #Here we r checking >pk value 1
    QLWO=Webpage.objects.filter(id__gt='0')
    #Here we r checking pk (or)id value >=3
    QLWO=Webpage.objects.filter(id__gte='3')
    QLWO=Webpage.objects.filter(id__lt='1')
    QLWO=Webpage.objects.filter(id__lte='2')

    #By using Q-objects checking multiple conditions like ename='smith',sal=100,deptno in(10,30)-----
    #1st import Q-objects from models---->from django.db.models import Q
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='Dhoni'))
    #for and opertor in django by using symbol & or comma(,)
    QLWO=Webpage.objects.filter(topic_name='Cricket',name='Dhoni')
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Dhoni'))
    QLWO=Webpage.objects.filter(Q(name__startswith='r') | Q(name__endswith='T'))
    QLWO=Webpage.objects.filter(Q(name__startswith='r') & Q(name__endswith='T'))
    QLWO=Webpage.objects.filter(Q(url__endswith='in') & Q(name__endswith='T') | Q(email__startswith='INDIA'))

    d={'webpages':QLWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.order_by('author')

    #month lookup
    QLAO=AccessRecord.objects.filter(date__month='12')
    QLAO=AccessRecord.objects.filter(date__day='17')
    QLAO=AccessRecord.objects.filter(date__year='2023')
    QLAO=AccessRecord.objects.filter(date__year='2022')
    QLAO=AccessRecord.objects.filter(author__startswith='B')
    QLAO=AccessRecord.objects.filter(author__endswith='i')
    #there is no changes for i and I , result both r same
    QLAO=AccessRecord.objects.filter(author__endswith='I')
    QLAO=AccessRecord.objects.filter(author__in=('sai2','BCCI','sai'))
    QLAO=AccessRecord.objects.filter(author__contains='BCCI')
    #there is no pk value 1 and 2 so check more than 3
    QLAO=AccessRecord.objects.filter(pk__startswith='3')

    d={'access':QLAO}
    return render(request,'display_access.html',d)
  