from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        
        self.stdout.write(self.style.SUCCESS('Connected to MongoDB'))
        
        # Drop existing collections to start fresh
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        
        self.stdout.write(self.style.SUCCESS('Dropped existing collections'))
        
        # Create unique index on email field
        db.users.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Created unique index on email field'))
        
        # Marvel Team Superheroes
        marvel_users = [
            {
                'username': 'ironman',
                'email': 'tony.stark@marvel.com',
                'full_name': 'Tony Stark',
                'team': 'Team Marvel',
                'created_at': datetime.now(),
                'fitness_level': 'advanced',
                'goals': ['strength', 'endurance']
            },
            {
                'username': 'captainamerica',
                'email': 'steve.rogers@marvel.com',
                'full_name': 'Steve Rogers',
                'team': 'Team Marvel',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'cardio']
            },
            {
                'username': 'blackwidow',
                'email': 'natasha.romanoff@marvel.com',
                'full_name': 'Natasha Romanoff',
                'team': 'Team Marvel',
                'created_at': datetime.now(),
                'fitness_level': 'advanced',
                'goals': ['flexibility', 'endurance']
            },
            {
                'username': 'thor',
                'email': 'thor.odinson@marvel.com',
                'full_name': 'Thor Odinson',
                'team': 'Team Marvel',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'power']
            },
            {
                'username': 'hulk',
                'email': 'bruce.banner@marvel.com',
                'full_name': 'Bruce Banner',
                'team': 'Team Marvel',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'mass']
            }
        ]
        
        # DC Team Superheroes
        dc_users = [
            {
                'username': 'batman',
                'email': 'bruce.wayne@dc.com',
                'full_name': 'Bruce Wayne',
                'team': 'Team DC',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'agility']
            },
            {
                'username': 'superman',
                'email': 'clark.kent@dc.com',
                'full_name': 'Clark Kent',
                'team': 'Team DC',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'endurance']
            },
            {
                'username': 'wonderwoman',
                'email': 'diana.prince@dc.com',
                'full_name': 'Diana Prince',
                'team': 'Team DC',
                'created_at': datetime.now(),
                'fitness_level': 'expert',
                'goals': ['strength', 'combat']
            },
            {
                'username': 'flash',
                'email': 'barry.allen@dc.com',
                'full_name': 'Barry Allen',
                'team': 'Team DC',
                'created_at': datetime.now(),
                'fitness_level': 'advanced',
                'goals': ['speed', 'cardio']
            },
            {
                'username': 'aquaman',
                'email': 'arthur.curry@dc.com',
                'full_name': 'Arthur Curry',
                'team': 'Team DC',
                'created_at': datetime.now(),
                'fitness_level': 'advanced',
                'goals': ['swimming', 'endurance']
            }
        ]
        
        all_users = marvel_users + dc_users
        result = db.users.insert_many(all_users)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} users'))
        
        # Create teams
        teams = [
            {
                'name': 'Team Marvel',
                'description': 'Avengers Assemble! The mightiest heroes on Earth',
                'created_at': datetime.now(),
                'captain': 'captainamerica',
                'members': ['ironman', 'captainamerica', 'blackwidow', 'thor', 'hulk'],
                'total_points': 0
            },
            {
                'name': 'Team DC',
                'description': 'Justice League - Protecting the world from threats',
                'created_at': datetime.now(),
                'captain': 'superman',
                'members': ['batman', 'superman', 'wonderwoman', 'flash', 'aquaman'],
                'total_points': 0
            }
        ]
        
        result = db.teams.insert_many(teams)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} teams'))
        
        # Create activities
        activities = []
        activity_types = ['running', 'cycling', 'swimming', 'weightlifting', 'yoga', 'boxing', 'crossfit']
        
        for user in all_users:
            # Generate 5-10 activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                activity_type = random.choice(activity_types)
                
                activity = {
                    'username': user['username'],
                    'activity_type': activity_type,
                    'duration_minutes': random.randint(20, 120),
                    'calories_burned': random.randint(100, 800),
                    'distance_km': round(random.uniform(1, 20), 2) if activity_type in ['running', 'cycling', 'swimming'] else 0,
                    'date': activity_date,
                    'notes': f'{activity_type.capitalize()} session',
                    'points': random.randint(10, 50)
                }
                activities.append(activity)
        
        result = db.activities.insert_many(activities)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} activities'))
        
        # Calculate leaderboard based on activities
        leaderboard_data = []
        for user in all_users:
            user_activities = [a for a in activities if a['username'] == user['username']]
            total_points = sum(a['points'] for a in user_activities)
            total_calories = sum(a['calories_burned'] for a in user_activities)
            total_duration = sum(a['duration_minutes'] for a in user_activities)
            
            leaderboard_entry = {
                'username': user['username'],
                'full_name': user['full_name'],
                'team': user['team'],
                'total_points': total_points,
                'total_calories': total_calories,
                'total_duration_minutes': total_duration,
                'total_activities': len(user_activities),
                'rank': 0,  # Will be calculated after sorting
                'updated_at': datetime.now()
            }
            leaderboard_data.append(leaderboard_entry)
        
        # Sort by points and assign ranks
        leaderboard_data.sort(key=lambda x: x['total_points'], reverse=True)
        for idx, entry in enumerate(leaderboard_data):
            entry['rank'] = idx + 1
        
        result = db.leaderboard.insert_many(leaderboard_data)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} leaderboard entries'))
        
        # Update team total points
        for team in teams:
            team_members = team['members']
            team_total = sum(l['total_points'] for l in leaderboard_data if l['username'] in team_members)
            db.teams.update_one(
                {'name': team['name']},
                {'$set': {'total_points': team_total}}
            )
        
        self.stdout.write(self.style.SUCCESS('Updated team total points'))
        
        # Create sample workouts
        workouts = [
            {
                'name': 'Super Soldier Strength',
                'description': 'Captain America inspired strength training',
                'difficulty': 'advanced',
                'duration_minutes': 60,
                'exercises': [
                    {'name': 'Push-ups', 'sets': 4, 'reps': 20},
                    {'name': 'Pull-ups', 'sets': 4, 'reps': 15},
                    {'name': 'Squats', 'sets': 4, 'reps': 25},
                    {'name': 'Deadlifts', 'sets': 4, 'reps': 12}
                ],
                'target_muscles': ['chest', 'back', 'legs'],
                'created_at': datetime.now()
            },
            {
                'name': 'Speedster Cardio',
                'description': 'Flash inspired high-intensity cardio',
                'difficulty': 'intermediate',
                'duration_minutes': 45,
                'exercises': [
                    {'name': 'Sprint Intervals', 'duration': '10 minutes'},
                    {'name': 'Jump Rope', 'duration': '5 minutes'},
                    {'name': 'Burpees', 'sets': 3, 'reps': 15},
                    {'name': 'Mountain Climbers', 'sets': 3, 'reps': 30}
                ],
                'target_muscles': ['cardio', 'full-body'],
                'created_at': datetime.now()
            },
            {
                'name': 'Amazonian Warrior',
                'description': 'Wonder Woman inspired combat training',
                'difficulty': 'advanced',
                'duration_minutes': 75,
                'exercises': [
                    {'name': 'Battle Ropes', 'sets': 4, 'duration': '1 minute'},
                    {'name': 'Kettlebell Swings', 'sets': 4, 'reps': 20},
                    {'name': 'Box Jumps', 'sets': 4, 'reps': 15},
                    {'name': 'Medicine Ball Slams', 'sets': 4, 'reps': 20}
                ],
                'target_muscles': ['full-body', 'power'],
                'created_at': datetime.now()
            },
            {
                'name': 'Dark Knight Agility',
                'description': 'Batman inspired agility and flexibility',
                'difficulty': 'intermediate',
                'duration_minutes': 50,
                'exercises': [
                    {'name': 'Ladder Drills', 'sets': 5, 'duration': '2 minutes'},
                    {'name': 'Yoga Flow', 'duration': '15 minutes'},
                    {'name': 'Plyometric Jumps', 'sets': 3, 'reps': 12},
                    {'name': 'Core Holds', 'sets': 3, 'duration': '1 minute'}
                ],
                'target_muscles': ['agility', 'flexibility', 'core'],
                'created_at': datetime.now()
            },
            {
                'name': 'Asgardian Power',
                'description': 'Thor inspired power lifting',
                'difficulty': 'expert',
                'duration_minutes': 90,
                'exercises': [
                    {'name': 'Heavy Deadlifts', 'sets': 5, 'reps': 5},
                    {'name': 'Bench Press', 'sets': 5, 'reps': 5},
                    {'name': 'Overhead Press', 'sets': 4, 'reps': 8},
                    {'name': 'Barbell Rows', 'sets': 4, 'reps': 10}
                ],
                'target_muscles': ['full-body', 'strength'],
                'created_at': datetime.now()
            }
        ]
        
        result = db.workouts.insert_many(workouts)
        self.stdout.write(self.style.SUCCESS(f'Inserted {len(result.inserted_ids)} workouts'))
        
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Total Users: {len(all_users)}'))
        self.stdout.write(self.style.SUCCESS(f'Total Teams: {len(teams)}'))
        self.stdout.write(self.style.SUCCESS(f'Total Activities: {len(activities)}'))
        self.stdout.write(self.style.SUCCESS(f'Total Leaderboard Entries: {len(leaderboard_data)}'))
        self.stdout.write(self.style.SUCCESS(f'Total Workouts: {len(workouts)}'))
        
        client.close()
