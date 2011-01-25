from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionType(models.Model):
    type_name = models.CharField(max_length=25)
    def __unicode__(self):
        return self.type_name

class QuestionSet(models.Model):
    name = models.TextField(max_length=128)

    def __unicode__(self):
        return self.name

class  Question(models.Model):
    text = models.TextField(max_length=128)
    type = models.ForeignKey(QuestionType)
    question_set = models.ForeignKey(QuestionSet,)
    
    def __unicode__(self):
         return u'(%s) %s | %s' % (self.question_set.name,self.text, self.type)

    def field_id(self):
        return "ID_%s" % (self.id,)

class AnswerSet(models.Model):
    date = models.DateField(auto_now_add= True)
    author = models.ForeignKey(User)
    count  = models.IntegerField(null = True)
    def __unicode__(self):
        return "%s(%d) at %s" % (self.author.username,self.count,str(self.date))


class SavedAnswer(models.Model):
    answer_set = models.ForeignKey(AnswerSet)
    question = models.ForeignKey(Question)
    answer = models.TextField()
    def __unicode__(self):
        return "%s:%s " % (self.question.text,self.answer[:50])



class UserProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)

    email = models.EmailField(blank=False)

    clean_start_time = models.DateField()
    country = models.TextField(max_length=128)
    
