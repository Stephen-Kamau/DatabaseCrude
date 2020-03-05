from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp/show/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'./employee/index.html',{'form':form})



def show(request):
    employees = Employee.objects.all()
    return render(request,"./employee/show.html",{'employees':employees})



def edit(request, id):
    employee = Employee.objects.get(Emp_id = id)
    return render(request,'./employee/edit.html', {'employee':employee})



def update(request, id):
    employee = Employee.objects.get(Emp_id = id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/emp/show/")

    else:
        return render(request, './employee/edit.html', {'employee': employee})



def destroy(request, id):
    employee = Employee.objects.get(Emp_id = id)
    employee.delete()
    return redirect("/emp/show/")
