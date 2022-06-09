from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from news_blog.models import Issue, Comment


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
    template_name = 'news_blog/detail.html'


class ResultsView(generic.DetailView):
    model = Issue
    template_name = 'news_blog/results.html'


def vote(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    try:
        selected_issue = issue.comment_set.get(pk=request.POST['issue'])
    except(KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'news_blog/detail.html', {
            'issue': issue,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_issue.comment_text = request.POST['issue']
        selected_issue.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('news_blog:detail', args=(issue.id,)))
