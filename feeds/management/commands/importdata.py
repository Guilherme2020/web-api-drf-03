import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings
from os.path import join
from feeds.models import Post,Address,Profile, Comment

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        print(join(settings.BASE_DIR,options['file']))
        
        json_file = open(join(settings.BASE_DIR,options['file']))

        dados = json.load(json_file)

        users = dados['users']

        for u in users:
            u['address'].pop('geo')
            address = Address(**u['address'])
            address.save()

            user = User()
            user.username = u['username']
            user.email = u['email']
            user.password = 'abcd@1234'
            user.address = address
            user.save()

            profile = Profile()
            profile.user = user
            profile.address = address
            profile.save()

        posts = dados['posts']

        for p in posts:
            post = Post()
            post.user = User.objects.get(pk=p['userId'])
            post.body = p.get('body') or 'sem corpo'
            post.title = p.get('title') or 'sem title'
            post.save()

        comments  = dados['comments']
        for c in comments:
            com = Comment()
            com.name = c['name']
            com.email = c['email']
            com.body = c['body']
            com.post = Post.objects.get(pk=c['postId'])
            com.save()
