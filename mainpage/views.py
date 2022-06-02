from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Issue, Issue_comment


class IndexView(generic.ListView):
    template_name = 'mainpage/index.html'
    context_object_name = 'latest_issue_list'

    # queryset = Question.objects.order_by('-pub_date')[:5]
    # equivalent
    def get_queryset(self):
        """Return the last five published questions."""
        return Issue.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Issue
    template_name = 'mainpage/detail.html'


class ResultsView(generic.DetailView):
    model = Issue
    template_name = 'mainpage/results.html'


def vote(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    try:
        selected_issue = issue.issue_comment_set.get(pk=request.POST['issue'])
    except(KeyError, Issue_comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mainpage/detail.html', {
            'issue': issue,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_issue.comment_text = request.POST['issue']
        selected_issue.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mainpage:detail', args=(issue.id,)))
