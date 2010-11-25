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

class SavedAnswer(models.Model):
    answer_set = models.ForeignKey(AnswerSet)
    question = models.ForeignKey(Question)
    answer = models.TextField()

#class AnswerSet(db.Model):
#    date = db.DateTimeProperty(auto_now_add=True)
#    author = db.UserProperty()
#    count  = db.IntegerProperty()
#
#class SavedAnswer(db.Model):
#  answer_set = db.ReferenceProperty(AnswerSet,
#                                   collection_name='saved_answers')
#  question = db.ReferenceProperty(reference_class=Question)
#  answer = db.StringProperty()
#

#
#
#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.URLField()
#    def __unicode__(self):
#        return self.name
#
#class Author(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=40)
#    email = models.EmailField(blank=True,verbose_name='e-mail')
#    def __unicode__(self):
#        return u'%s %s' % (self.first_name, self.last_name)
#
#class Book(models.Model):
#    title = models.CharField(max_length=100)
#    authors = models.ManyToManyField(Author)
#    publisher = models.ForeignKey(Publisher)
#    publication_date = models.DateField(blank=True, null=True)
#    def __unicode__(self):
#        return self.title
