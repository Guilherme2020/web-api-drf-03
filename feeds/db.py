import json

from django.contrib.auth.models import User

from feeds.models import Post,Address,Profile, Comment

file = open('../db.json')

dados = json.load(file)

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

profile = Profile()
profile.user = user
profile.address = address
profile.save()