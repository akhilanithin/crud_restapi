from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect  
from notes.forms import NoteForm  
from notes.models import Note  





# Create your views here. 

def home(request):
    return render(request,'home.html')
def emp(request):  
    if request.method == "POST":  
        form = NoteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = NoteForm()  
    return render(request,'index.html',{'form':form})
  
def show(request):  
    notes = Note.objects.all()  
    return render(request,"show.html",{'notes':notes}) 
 
def edit(request, id):  
    notes = Note.objects.get(id=id)  
    return render(request,'edit.html', {'notes':notes}) 
 
def update(request, id):  
    notes = Note.objects.get(id=id)  
    form = NoteForm(request.POST, instance = notes)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'notes': notes}) 
 
def destroy(request, id):  
    notes = Note.objects.get(id=id)  
    notes.delete()  
    return redirect("/show")  