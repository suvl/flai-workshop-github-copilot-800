from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model."""
    
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            full_name='Test User',
            team='Test Team',
            fitness_level='intermediate',
            goals=['strength', 'endurance']
        )

    def test_user_creation(self):
        """Test that a user can be created."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(str(self.user), 'testuser')


class TeamModelTest(TestCase):
    """Test cases for Team model."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            captain='testuser',
            members=['testuser', 'testuser2'],
            total_points=100
        )

    def test_team_creation(self):
        """Test that a team can be created."""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.total_points, 100)
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            username='testuser',
            activity_type='running',
            duration_minutes=30,
            calories_burned=300,
            distance_km=5.0,
            notes='Morning run',
            points=25
        )

    def test_activity_creation(self):
        """Test that an activity can be created."""
        self.assertEqual(self.activity.username, 'testuser')
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.calories_burned, 300)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model."""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            username='testuser',
            full_name='Test User',
            team='Test Team',
            total_points=100,
            total_calories=500,
            total_duration_minutes=60,
            total_activities=5,
            rank=1
        )

    def test_leaderboard_entry_creation(self):
        """Test that a leaderboard entry can be created."""
        self.assertEqual(self.entry.username, 'testuser')
        self.assertEqual(self.entry.rank, 1)
        self.assertEqual(self.entry.total_points, 100)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model."""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty='intermediate',
            duration_minutes=45,
            exercises=[{'name': 'Push-ups', 'sets': 3, 'reps': 10}],
            target_muscles=['chest', 'arms']
        )

    def test_workout_creation(self):
        """Test that a workout can be created."""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'intermediate')
        self.assertEqual(str(self.workout), 'Test Workout')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'apiuser',
            'email': 'api@example.com',
            'full_name': 'API User',
            'team': 'API Team',
            'fitness_level': 'beginner',
            'goals': ['fitness']
        }

    def test_create_user(self):
        """Test creating a user via API."""
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        """Test retrieving users via API."""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'API Team',
            'description': 'A team created via API',
            'captain': 'apiuser',
            'members': ['apiuser'],
            'total_points': 0
        }

    def test_create_team(self):
        """Test creating a team via API."""
        response = self.client.post('/api/teams/', self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teams(self):
        """Test retrieving teams via API."""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.activity_data = {
            'username': 'apiuser',
            'activity_type': 'cycling',
            'duration_minutes': 45,
            'calories_burned': 400,
            'distance_km': 10.0,
            'notes': 'Evening ride',
            'points': 30
        }

    def test_create_activity(self):
        """Test creating an activity via API."""
        response = self.client.post('/api/activities/', self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_activities(self):
        """Test retrieving activities via API."""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints."""
    
    def setUp(self):
        self.client = APIClient()

    def test_get_leaderboard(self):
        """Test retrieving leaderboard via API."""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints."""
    
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'name': 'API Workout',
            'description': 'A workout created via API',
            'difficulty': 'advanced',
            'duration_minutes': 60,
            'exercises': [{'name': 'Squats', 'sets': 4, 'reps': 15}],
            'target_muscles': ['legs']
        }

    def test_create_workout(self):
        """Test creating a workout via API."""
        response = self.client.post('/api/workouts/', self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_workouts(self):
        """Test retrieving workouts via API."""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
