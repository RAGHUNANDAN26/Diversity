from django.shortcuts import render
from rest_framework.response import Response
from .models import Students
from App1.serializers import StudentSerializers
from django.db.models import Avg, Min, Max, Sum, Count
import djqscsv
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from App1.models import Files_upload




# Create your views here.
from rest_framework.decorators import api_view
@api_view(['GET','POST','DELETE'])
def students_list(request):
    if request.method == 'GET':
        qs=Students.objects.all()
        q = qs.values('id' , 'name' , 'score')
        df = pd.DataFrame.from_records(q)
        mean_df=df['score'].mean()
        min_df=df['score'].min() 
        max_df=df['score'].max()         # Students_csv = djqscsv.render_to_csv_response(students)
        # hi = pandas.read_csv(Students_csv)
        print(mean_df)
        context ={ 
            "mean":mean_df, 
            "min":min_df,
            "max":max_df
               }       # serializers = StudentSerializers(students,many=True)
        return Response(context)

    

    if request.method == 'POST':
        name = request.data.get("name")
        print(name)
        students = Students.objects.create( name= name, score= request.data.get("score"))
        # serializers = StudentSerializers(students,many=True)
        return Response("success")

    if request.method == 'DELETE':
        students = Students.objects.get(id=100)
        students.delete()
        students.save()
        # serializers = StudentSerializers(students,many=True)
        return Response("success")

# def students_list(request):
# try:
#     p=Project(name=request.POST.get('project1'))
#     p.save()
#     return redirect('http://www.google.com/')
# except:
#     return redirect('http://www.google.com/')

@api_view(['POST'])
def project_upload(request):
    if request.method == 'POST' :
    #  and request.FILES['myfile']:
        # # myfile = request.FILES['myfile'].name
        for myfile, file in request.FILES.items():
            name = request.FILES[myfile]
            sqs= Files_upload.objects.create(document = name)
            print(name)
        
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        return Response('Hello')






