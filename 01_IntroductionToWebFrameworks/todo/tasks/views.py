import random
import re
from django.http import HttpResponse

from django.views import View


class ToDoView(View):
    tasks = ''
    use_task = []

    def get(self, request, *args, **kwargs):
        return HttpResponse(f'<ul>{ToDoView.task_list(self)}</ul>')

    def task_list(self):
        if ToDoView.use_task == []:
            count = 0
            while count < 5:
                s = random.randint(1, 10)
                if s not in ToDoView.use_task:
                    ToDoView.tasks += (f'<li>Task {s}</li>')
                    ToDoView.use_task.append(s)
                    count += 1
                else:
                    continue
        return ToDoView.tasks