from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializer import Student_Serializer
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
def addStudent(request):
    serialized_data = Student_Serializer(data = request.data)
    msg = ''
    if serialized_data.is_valid() :
        serialized_data.save()
        msg = 'Data added successfully'
        return JsonResponse({'msg':msg})
    else :
        msg = 'Invalid Details'
        return JsonResponse({'msg':msg})
    

@api_view(['GET'])
def viewStudent(request):
    students = Student.objects.all()
    serialized_data = Student_Serializer(students,many = True)
    return JsonResponse(serialized_data.data,safe = False)

@api_view(['PUT'])
def updateStudent(request,student_id):
    student = Student.objects.get(id = student_id)
    serialized_data = Student_Serializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'msg':'updated successfully'})
    else:
        return JsonResponse({'msg':'invalid details'})
    
@api_view(['DELETE'])
def deleteStudent(request,student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    return JsonResponse({'msg':'Deleted Successfully'})

    


