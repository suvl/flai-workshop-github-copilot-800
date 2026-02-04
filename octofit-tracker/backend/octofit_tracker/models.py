from djongo import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    fitness_level = models.CharField(max_length=50)
    goals = models.JSONField(default=list)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    captain = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    total_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    username = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    distance_km = models.FloatField(default=0)
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    points = models.IntegerField(default=0)

    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.username} - {self.activity_type}"


class Leaderboard(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    total_calories = models.IntegerField(default=0)
    total_duration_minutes = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        return f"{self.rank}. {self.full_name}"


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    exercises = models.JSONField(default=list)
    target_muscles = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
