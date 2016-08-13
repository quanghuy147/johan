from django.shortcuts import render
from .forms import ProcessForm


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = ProcessForm()
        form.input1 = "TEST"
    else:
        form = ProcessForm(request.POST)
        input1 = request.POST['input1']
        # newstring = input1.rstrip('\r\n') WHy this not work
        newstring = input1.replace('\r\n', ' ')
        print(newstring)

        data = form.data.copy()
        data['output1'] = newstring
        form.data = data

    context = {'form': form}
    return render(request, 'concatenate/index.html', context)

