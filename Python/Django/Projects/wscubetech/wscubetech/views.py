from django.http import HttpResponse  # send message to browser
from django.shortcuts import render  # send the html file to browser
import random

def home(request):
    return HttpResponse("Welcome to Django.")

def aboutUs(request):
    return HttpResponse("Welcome to wscubetech.")

def course(request):
    result = """
    <b>
    <h2><font color="red">List of courses:</font></h2>
    <font color="blue">
    <ol>
        <li> BCA </li>
        <li> BBA </li>
        <li> B.Tech. </li>
        <li> B.Sc. </li>
        <li> B.A. </li>
        <li> B.Com. </li>
        <li> PHP </li>
        <li> Python </li>
        <li> Java </li>
        <li> Flutter </li>
    </ol>
    </font>
    </b>
    """
    return HttpResponse(result)

# dynamic routes
def courseDetails(request, courseId):
    if courseId == 1:
        result = "BCA Courses"
    elif courseId == 2:
        result = "BBA Course"
    elif courseId == 3:
        result = "B.Tech. Course"
    elif courseId == 4:
        result = "B.Sc. Course"
    elif courseId == 5:
        result = "B.A. Course"
    elif courseId == 6:
        result = "B.Com. Course"
    elif courseId == 7:
        result = "PHP Course"
    elif courseId == 8:
        result = "Python. Course"
    elif courseId == 9:
        result = "Java. Course"
    elif courseId == 10:
        result = "Flutter Course"
    else:
        result = f"courseDetails: {courseId}"
    return HttpResponse(result)


def teachers(request):
    result = """
    <b>
    <h2><font color="red">List of teachers:</font></h2>
    <font color="blue">
    <ol>
        <li> Mr.Ramesh Mishra </li>
        <li> Mr.Primal Tiwari </li>
        <li> Dr. Apoorve Shukla </li>
        <li> Ms.Shambhavi Mudra </li>
    </ol>
    </font>
    </b>
    """
    return HttpResponse(result)

# dynamic routes
def teachersNames(request, teachersName):
    result = f"teachers Name: {teachersName}"
    return HttpResponse(result)

def students(request):
    result = """
    <b>
    <h2><font color="red">List of students:</font></h2>
    <font color="blue">
    <ol>
        <li> Arjun Prajapati </li>
        <li> Sudhanshu Mishra </li>
        <li> Jyoti Sharma </li>
        <li> Vikas Prajapati </li>
    </ol>
    </font>
    </b>
    """
    return HttpResponse(result)

# dynamic routes
def studentsDescription(request, studentsDes):
    result = f"students Description: {studentsDes}"
    return HttpResponse(result)

def colleges(request):
    result = """
    <b>
    <h2><font color="red">List of colleges:</font></h2>
    <font color="blue">
    <ol>
        <li> Dr. Rammanohar Lohia Avadh University </li>
        <li> BBD University </li>
        <li> Swami Vivekanand University </li>
        <li> Galgotiya University </li>
    </ol>
    </font>
    </b>
    """
    return HttpResponse(result)

def collegesDetails(request, college_name):
    return HttpResponse(college_name)


# render template
def homePage(request):
    return render(request, "index.html")

# dynamic render template
def homeData(request):
    data = {
        'title': 'Home Data',
        'city': 'Ayodhya',
        'user': 'Arjun Prajapati',
        'courses': ['PHP', 'Python', 'Java', 'Cpp', 'C'],
        'numbers': [random.randint(10, 99) for _ in range(10)],
        'student_details': [
            {'name': 'Pradeep', 'phone': 8054674372},
            {'name': 'Suresh', 'phone': 6383548894},
            {'name': 'Jiya', 'phone': 6393549811},
            {'name': 'Arjun', 'phone': 9161589883}
        ], 
    }
    return render(request, "indexData.html", data)



def homeList(request):
    data = {
        'title': "Home List",
        'city': "Gurugram",
        'user': "Er. Arjun",
        'numbers': list(set([random.randint(10, 99) for _ in range(30)]))
        # 'numbers': [],
        }
    return render(request, "homeList.html", data)


