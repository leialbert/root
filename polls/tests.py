from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question,Choice

class QuestionModelTests(TestCase):
    def test_was_published_recently_future_question(self):
        """
        to test if the was_published_recently function
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recently_question = Question(pub_date=time)
        self.assertIs(recently_question.was_published_recently(), True)
    

