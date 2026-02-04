from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'team', 'fitness_level', 'created_at')
    list_filter = ('team', 'fitness_level', 'created_at')
    search_fields = ('username', 'email', 'full_name')
    ordering = ('username',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'total_points', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'captain')
    ordering = ('-total_points',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('username', 'activity_type', 'duration_minutes', 'calories_burned', 'points', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('username', 'activity_type')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'username', 'full_name', 'team', 'total_points', 'total_activities', 'updated_at')
    list_filter = ('team', 'updated_at')
    search_fields = ('username', 'full_name')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'duration_minutes', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
