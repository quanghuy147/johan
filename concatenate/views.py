from django.shortcuts import render
from .forms import ProcessForm


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = ProcessForm()
        form.input1 = "TEST"
    else:
        form = ProcessForm(request.POST)
        if form.is_valid():
            input1 = request.POST['input1']
            print(input1.rstrip('\n'))
            data = form.data.copy()
            data['output1'] = "processed"
            form.data = data

    context = {'form': form}
    return render(request, 'concatenate/index.html', context)
