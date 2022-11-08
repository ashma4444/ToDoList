from django.shortcuts import redirect, render
from .forms import ToDoForm
from .models import ToDoLists

# Create your views here.
def home(req):
    if req.method == 'POST':
        myform = ToDoForm(req.POST)

        # if the form is valid then pass the data into the database
        if myform.is_valid():
            myform.save()
            # myform = ToDoForm()
            return redirect('/')
    else: 
        myform = ToDoForm()
    
    # retriving data from the database
    todolists = ToDoLists.objects.all()

    return render(req, 'base/index.html', {'form': myform, 'mytodo':todolists})


# Delete function
def delete(req, id):
    task = ToDoLists.objects.get(id=id)
    task.delete()
    return redirect('/')


# Update function
def update(req, id):
    task = ToDoLists.objects.get(id=id)
    myform = ToDoForm(instance=task) #yo form ma jun edit garnu parne tyo id vako task ko previous information/ i.e. agadi ko table bata aako information aaucha

    if req.method == 'POST':
        taskform = ToDoForm(req.POST, instance=task) #yo form ma hamile naya kei enter garyo vani store huncha
        
        if taskform.is_valid():
            task = taskform.save(commit=False)
            task.save()
            return redirect('home')
    return render(req, 'base/update.html',{'form': myform})



# Update function - For begineers
# def update(req, id):
#     currenttask = ToDoLists.objects.get(id=id)
#     myform = ToDoForm(instance = currenttask)

#     if req.method == 'POST':
#         newtask = req.POST['task']
#         currenttask.task = newtask
#         # .task is from the models.py
#         currenttask.save()
#         return redirect('home')
#     return render(req, 'base/update.html',{'form': myform})