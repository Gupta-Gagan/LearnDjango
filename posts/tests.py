from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create(
            username='testuser',
            password='1234',
        )
        
        test_user1.save()
        
        test_post = Post.objects.create(
                author=test_user1, title='Blog title', body='Body content...')
        test_post.save()
        
        
    def test_blog_case(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')