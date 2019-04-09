import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone
from boards.models import Board,Topic,Post
import random

def create_user(n):
    for _ in range(n):
        fake = Faker()
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()

        User.objects.create_user(username=username, password="abcd1234",
                                 email=email, first_name=first_name, last_name=last_name)
    print(f"{n} users created successfully...")


def create_board(n):
    for _ in range(n):
        fake = Faker()
        name = fake.sentence()
        details = fake.paragraph()

        Board.objects.create(name=name, description=details)
        
    print(f"{n} Boards created successfully...")


def create_topic(n):
    boards = Board.objects.all()
    users = User.objects.all()
    for _ in range(n):
        fake = Faker()
        board = random.choice(boards)
        user = random.choice(users)
        subj = fake.sentence()
        details = fake.paragraph()

        new_topic = Topic.objects.create(subject=subj, board=board, starter=user)
        Post.objects.create(message=details, topic=new_topic, created_by=user)

    print(f"{n} Topics created successfully...")


def create_post(n):
    boards = Board.objects.all()
    users = User.objects.all()
    topics = Topic.objects.all()

    for _ in range(n):
        fake = Faker()
        board = random.choice(boards)
        user = random.choice(users)
        topic = random.choice(topics)
        msg = fake.sentence()
        
        Post.objects.create(message=msg, topic=topic, created_by=user)
        
    print(f"{n} Posts created successfully...")
