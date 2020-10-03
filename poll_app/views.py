from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll

# Create your views here.
def poll(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/polls.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    print(poll.options)
    if poll.options == {}:
        poll.options = poll.example2(poll.example)
        poll.save()
    else:
        options_dict = poll.options

        if request.method == 'POST':
            selected_option = request.POST['poll']

            if selected_option in options_dict.keys():
                options_dict[selected_option] += 1
            else:
                return HttpResponse(400, 'Invalid Form')
            poll.save()
            return redirect('result', poll.id)

    context = {
        'poll' : poll,
        'options' : poll.options.keys(),
    }
    return render(request, 'poll/vote.html', context)

def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    items = poll.options.items()
    context = {
        'poll' : poll,
        'items' : items,
    }
    return render(request, 'poll/results.html', context)

def create(request):

    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll')
    else:
        form = CreatePollForm()
    context = { 
        'form' : form
    }
    return render(request, 'poll/create.html', context)




