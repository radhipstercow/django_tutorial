from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.

# Sona_ID Model
class studyUser(models.Model):
    sonaID = models.CharField(max_length=255,primary_key=True, unique=True)

# Session ID
class Session(models.Model):
    sessionID = models.CharField(max_length=255, primary_key=True,unique=True, default=uuid.uuid4)
    sonaID = models.ForeignKey(studyUser, max_length=255, on_delete=models.CASCADE)

# Part 1
class part_1(models.Model):
    sessionID = models.ForeignKey(Session, max_length=255, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0,validators=[MaxValueValidator(100)])
    major = models.CharField(max_length=255)

# Part 2
class part_2(models.Model):
    sessionID = models.ForeignKey(Session, max_length=255, on_delete = models.CASCADE)
    advanced_degree = models.IntegerField(default=0,validators=[MaxValueValidator(1)])
    dream_Job = models.TextField()

# Part 3
class part_3(models.Model):
    sessionID = models.ForeignKey(Session, max_length=255, on_delete = models.CASCADE)
    user_os = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255)
    phone_sat = models.IntegerField(default=0,validators=[MaxValueValidator(5)])