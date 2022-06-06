import datetime
from django.db import models
from django.utils import timezone


class Issue(models.Model):
    issue_topic = models.CharField(max_length=100)
    issue_text = models.CharField(max_length=400)
    issue_image = models.ImageField()
    issue_author = models.CharField(max_length=100)
    issue_class = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.issue_topic


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=400)
    comment_author = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_text


# DEBUG
# if __name__ == '__main__':
    # q = Question()

