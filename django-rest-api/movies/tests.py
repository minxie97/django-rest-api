from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Movie

class MovieTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Movie.objects.create(title='inception', director='christopher nolan', description='dream in a dream', watcher = testuser1)
        test_thing.save()

    def test_movie_model(self):
        movie = Movie.objects.get(id=1)
        actual_title = str(movie.title)
        actual_director = str(movie.director)
        actual_description = str(movie.description)
        actual_watcher = str(movie.watcher)
        self.assertEqual(actual_title,'inception')
        self.assertEqual(actual_director, 'christopher nolan')
        self.assertEqual(actual_description,'dream in a dream')
        self.assertEqual(actual_watcher, 'testuser')