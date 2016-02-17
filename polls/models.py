from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Sample(models.Model):
    policyid = models.TextField(db_column='policyID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    statecode = models.TextField(blank=True, null=True)  # This field type is a guess.
    county = models.TextField(blank=True, null=True)  # This field type is a guess.
    eq_site_limit = models.TextField(blank=True, null=True)  # This field type is a guess.
    hu_site_limit = models.TextField(blank=True, null=True)  # This field type is a guess.
    fl_site_limit = models.TextField(blank=True, null=True)  # This field type is a guess.
    fr_site_limit = models.TextField(blank=True, null=True)  # This field type is a guess.
    tiv_2011 = models.TextField(blank=True, null=True)  # This field type is a guess.
    tiv_2012 = models.TextField(blank=True, null=True)  # This field type is a guess.
    eq_site_deductible = models.TextField(blank=True, null=True)  # This field type is a guess.
    hu_site_deductible = models.TextField(blank=True, null=True)  # This field type is a guess.
    fl_site_deductible = models.TextField(blank=True, null=True)  # This field type is a guess.
    fr_site_deductible = models.TextField(blank=True, null=True)  # This field type is a guess.
    point_latitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    point_longitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    line = models.TextField(blank=True, null=True)  # This field type is a guess.
    construction = models.TextField(blank=True, null=True)  # This field type is a guess.
    point_granularity = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sample'
