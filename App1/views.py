from django.shortcuts import render
from rest_framework.response import Response
from .models import Students
from App1.serializers import StudentSerializers
from django.db.models import Avg, Min, Max, Sum, Count




# Create your views here.
from rest_framework.decorators import api_view
@api_view(['GET','POST','DELETE'])
def students_list(request):
    if request.method == 'GET':
        students = Students.objects.filter(name="Surya")
        serializers = StudentSerializers(students,many=True)
        return Response(serializers.data)

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


