from django.test import TestCase, Client
from .models import News, Comment
from django.urls import reverse
from django.contrib.auth.models import User

class NewsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Создаем тестовую новость
        test_news = News.objects.create(title='Test News', text='This is a test news', author=test_user)
        test_news.save()

    def test_news_title(self):
        news = News.objects.get(id=1)
        expected_title = f'{news.title}'
        self.assertEqual(expected_title, 'Test News')

    def test_news_text(self):
        news = News.objects.get(id=1)
        expected_text = f'{news.text}'
        self.assertEqual(expected_text, 'This is a test news')

class NewsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()

        # Создаем тестовые новости
        number_of_news = 10
        for news_id in range(number_of_news):
            News.objects.create(title=f'Test News {news_id}', text=f'This is test news {news_id}', author=test_user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/news_list.html')