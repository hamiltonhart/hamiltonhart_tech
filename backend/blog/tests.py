from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='testemail@test.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title = "A good title",
            author = self.user,
            body_text = "Good content"
        )

    def test_str_representation(self):
        post = Post(title="A good title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', "A good title")
        self.assertEqual(f'{self.post.author}', "test_user")
        self.assertEqual(f'{self.post.body_text}', "Good content")

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body_text}'
        self.assertEqual(expected_author, 'test_user')
        self.assertEqual(expected_title, 'A good title')
        self.assertEqual(expected_body, 'Good content')
        

    # def test_post_list_view(self):
    #     response = self.client.get(reverse('post_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Good content")
    #     self.assertTemplateUsed(response, "blog/post_list.html")

    # def test_post_detail_view(self):
    #     response = self.client.get('/post/1/')
    #     no_response = self.client.get('/post/1000/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "A good title")
    #     self.assertTemplateUsed(response, "blog/post_detail.html")
