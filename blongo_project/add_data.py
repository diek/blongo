from blongo.models import Post
import datetime
Post(title='just a test', content='again, just a test', date_published=datetime.datetime.now).save()
for post in Post.objects:
    print(post.title)
