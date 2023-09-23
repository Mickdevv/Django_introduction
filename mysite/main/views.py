from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

verbosity = 1

def index(response, id):
    if verbosity == 1 :
        print("Index method")

    ls = ToDoList.objects.get(id=id)

    #{"save":["save"], "c1":["clicked"]}
    if response.method == "POST":
        print(response.POST)
        print("\n")

        # Delete selected items
        if response.POST.get("delete"):
            print("Delete method")
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.delete()

        # Save changes to items
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else: 
                    item.complete = False
                item.save()
        
        # Add new item 
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            print(len(txt))
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")
        
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    print("HOME")
    return render(response, "main/home.html", {})

def create(response):
    if verbosity == 1 :
        print()
        print("START - Create method views.py")
    if response.method == "POST":
        print("Response method POST")
        form = CreateNewList(response.POST)
        if form.is_valid():
            print("Form is valid")
            n = form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            if verbosity == 1 :
                print("END - Create method views.py - Form is valid")
            return HttpResponseRedirect("/%i" %t.id)
    
    else :
        if verbosity == 1 :
            print("END - Create method views.py - Method != POST")
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})

def view(response):
    if verbosity == 1 :
        print("START - View method")
    return render(response, "main/view.html")

def members(request):
    return HttpResponse("Hello world!")