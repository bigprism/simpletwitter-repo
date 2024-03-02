from django.test import TestCase
from django.urls import reverse

class PostCreateTestCase(TestCase):
    def test_can_create_post(self):
        data = {'content': 'This is a test post.'}
        response = self.client.post(reverse('create_post'), data)
        self.assertEqual(response.status_code, 201)

from django.test import TestCase
from django.urls import reverse

class PostLikeTestCase(TestCase):
    def test_can_like_post(self):
        post = Post.objects.create(content='This is a test post.')
        response = self.client.post(reverse('like_post', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse

class PostCommentTestCase(TestCase):
    def test_can_comment_on_post(self):
        post = Post.objects.create(content='This is a test post.')
        data = {'content': 'This is a test comment.'}
        response = self.client.post(reverse('comment_on_post', kwargs={'pk': post.pk}), data)
        self.assertEqual(response.status_code, 201)

from django.test import TestCase
from django.urls import reverse

class PostDetailTestCase(TestCase):
    def test_can_view_post_detail(self):
        post = Post.objects.create(content='This is a test post.')
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse

class HomePageTestCase(TestCase):
    def test_can_view_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)