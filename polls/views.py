from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse


from .models import Choice, Question, Vote
from .forms import PollAddForm, EditPollForm, ChoiceAddForm


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
@login_required()
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    question_list = Question.objects.all()
    search_term = ''
    if 'name' in request.GET:
        question_list = question_list.order_by('question_text')

    if 'date' in request.GET:
        question_list = question_list.order_by('pub_date')

    if 'vote' in request.GET:
        question_list = question_list.annotate(Count('vote')).order_by('vote__count')

    if 'search' in request.GET:
        search_term = request.GET['search']
        question_list = question_list.filter(question_text__icontains=search_term)

    # https://docs.djangoproject.com/en/3.1/topics/pagination/
    paginator = Paginator(question_list, 5)  # Show 5 polls per page
    page = request.GET.get('page')
    question = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    print(params)

    context = {
        'questions': question,
        'params': params,
        'search_term': search_term,
    }
    return render(request, 'polls/index.html', context)

@login_required()
def list_by_user(request):
    all_polls = Question.objects.filter(owner=request.user)
    paginator = Paginator(all_polls, 7)  # Show 7 contacts per page

    page = request.GET.get('page')
    polls = paginator.get_page(page)

    context = {
        'questions': polls,
    }
    return render(request, 'polls/index.html', context)

@login_required()
def polls_add(request):
    if request.user.has_perm('polls.add_choice'):
        if request.method == 'POST':
            form = PollAddForm(request.POST)
            if form.is_valid:
                question = form.save(commit=False)
                question.save()
                new_choice1 = Choice(
                    question=question, choice_text=form.cleaned_data['choice1']).save()
                new_choice2 = Choice(
                    question=question, choice_text=form.cleaned_data['choice2']).save()
                new_choice3 = Choice(
                    question=question, choice_text=form.cleaned_data['choice3']).save()
                messages.success(
                    request, "Poll & Choices added successfully", extra_tags='alert alert-success alert-dismissible fade show')

                return redirect('polls:index')
        else:
            form = PollAddForm()
        context = {
            'form': form,
        }
        return render(request, 'polls/add_poll.html', context)
    else: 
        return HttpResponse("Sorry but you don't have permission to do that!")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not question.active:
        return render(request, 'polls/poll_result.html', {'question': question})
    loop_count = question.choice_set.count()
    context = {
        'question': question,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def editq(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=question)
        if form.is_valid:
            form.save()
            messages.success(request, "Poll Updated successfully",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("polls:index")

    else:
        form = EditPollForm(instance=question)

    return render(request, "polls/poll_edit.html", {'form': form, 'question': question})


@login_required
def polls_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.owner:
        return redirect('home')
    question.delete()
    messages.success(request, "Poll Deleted successfully",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return redirect("polls:index")

@login_required
def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.owner:
        return redirect('home')

    if request.method == 'POST':
        form = ChoiceAddForm(request.POST)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.question = question
            new_choice.save()
            messages.success(
                request, "Choice added successfully", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polls:editq', question.id)
    else:
        form = ChoiceAddForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/add_choice.html', context)

@login_required
def choice_edit(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    question = get_object_or_404(Question, pk=choice.question.id)

    if request.user != question.owner:
        return redirect('home')

    if request.method == 'POST':
        form = ChoiceAddForm(request.POST, instance=choice)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.question = question
            new_choice.save()
            messages.success(
                request, "Choice Updated successfully", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polls:editq', question.id)
    else:
        form = ChoiceAddForm(instance=choice)
    context = {
        'form': form,
        'edit_choice': True,
        'choice': choice,
    }
    return render(request, 'polls/add_choice.html', context)

@login_required
def choice_delete(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    question = get_object_or_404(Question, pk=choice.question.id)

    if request.user != question.owner:
        return redirect('home')

    choice.delete()
    messages.success(
        request, "Choice Deleted successfully", extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('polls:editq', question.id)

@login_required
def endpoll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != poll.owner:
        return redirect('home')

    if poll.active is True:
        poll.active = False
        poll.save()
        return render(request, 'polls/poll_result.html', {'question': question})
    else:
        return render(request, 'polls/poll_result.html', {'question': question})

@login_required
def poll_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get('choice')
    if not question.user_can_vote(request.user):
        messages.error(
            request, "You already voted this poll", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("polls:index")

    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        vote = Vote(user=request.user, question=question, choice=choice)
        vote.save()
        print(vote)
        return render(request, 'polls/poll_result.html', {'poll': question})
    else:
        messages.error(
            request, "No choice selected", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("polls:detail", question_id)
    return render(request, 'polls/poll_result.html', {'poll': question})