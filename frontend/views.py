from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

from backend.models import Student, MarkList


def login(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        dob = request.POST.get('dob')

        if not roll_number or not dob:
            messages.error(request, "Enter a valid Roll Number and DOB")
            return render(request, "frontend/login.html")

        student = Student.objects.filter(Q(roll_number=roll_number) & Q(dob=dob)).first()

        context = {
            'student': student,
            'marklist': MarkList.objects.filter(student=student).all(),
            'total_mark': MarkList.objects.filter(student=student).aggregate(total_mark=Sum('mark')).get('total_mark')
        }

        if student:
            return render(request, "frontend/result.html", context)
        else:
            messages.error(request, "Enter a valid Roll Number and DOB")
            return render(request, "frontend/login.html")

    return render(request, "frontend/login.html")


def logout_view(request):
    logout(request)
    request.session.flush()  # Clear the session data
    return redirect('staff_login')  # Redirect to the index page



