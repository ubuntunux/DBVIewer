from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def add_question(request):
    q = Question(question_text="ok new question", pub_date=timezone.now())
    q.save()
    # back to index page
    return HttpResponseRedirect(reverse('polls:index'))


def view_image(request):
    with open("images/a.jpg", "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # if no have choice then add choice
        if question.choice_set.count() == 0:
            question.choice_set.create(choice_text='ok', votes=0)
            question.choice_set.create(choice_text='no', votes=0)

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
