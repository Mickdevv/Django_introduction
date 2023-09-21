from main.models import ToDoList

ls = ToDoList.objects.get(id=2)
ls.item_set.create(text="not showing", complete=True)
print(1)