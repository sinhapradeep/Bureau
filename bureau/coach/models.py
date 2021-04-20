from django.db import models


class Coach(models.Model):
    subject = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    stand = models.CharField(max_length=10)

class Computer(models.Model):
    coursec = models.CharField(max_length=30)




class Teacher(models.Model):
    name = models.CharField(max_length=30, default=' ')
    qual = models.CharField(max_length=30, default=' ')
    exp = models.CharField(max_length=30, default=' ')
    mob = models.CharField(max_length=30, default=' ')
    email = models.CharField(max_length=30, default=' ')
    stand = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    board = models.CharField(max_length=30)
    locat = models.CharField(max_length=30)



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    Details = models.CharField(max_length=100, default = ' ')

class Prof(models.Model):
    sname = models.CharField(max_length=50)
    amoun = models.CharField(max_length=10, default='')
    cours1 = models.CharField(max_length=30, default='xx')
    cours2 = models.CharField(max_length=30, default='xx')








