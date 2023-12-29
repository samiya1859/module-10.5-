from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    data = { 'author':'Samia', 'age':25,'list':['python','oop','django'],'value':'123','val':'jai','val2':'Sa Mi Ya',
      'bday':datetime.datetime.now()  ,'val3':'' ,'namelist':[
          {'name':'sam','age':19},
          {'name':'aam','age':22},
          {'name':'lal','age':31},
      ] ,'val4':123456789 , 'vallist':['a','b','c'],'ctime':'09:00 on 1 June 2006'

    }

    return render(request,'index.html',context=data)