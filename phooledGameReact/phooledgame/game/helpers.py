"""
This file contains all model like classes that do
not add data to the database. Each of these classes
and methods are helper functions for the views.

An example would be the generator of a quiz session.
"""
import random
import json

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property

from gamification.choices import QuestionCategory, QuestionType
from gamification.models.question import GamificationQuestionTemplate
from phish.models import PhishingSample, PhishingAttribute
from gamification.models.session import QuizSession

class Question:

    def __init__(
        self,
        sample=None,
        question_template=None,
        characteristics={},
        answers=[],
        answer_key= None
    ):
        """
        This class handles the characteristics of a question before
        storing within the database
        """
        self.question_template = question_template
        self.sample = sample
        self.characteristics = characteristics
        self.answers = answers
        self.answer_key = answer_key

    @property
    def sample_id(self):
        if isinstance(self.sample, PhishingSample):
            return self.sample.pk
        return None

    @property
    def question_template_id(self):
        if isinstance(self.question_template, GamificationQuestionTemplate):
            return self.question_template.pk
        return None

    @property
    def category_code(self):
        if self.question_template is not None:
            return self.question_template.category_code
        return ""

    @property
    def question_statement(self):
        if self.question_template is not None:
            return self.question_template.complete_question_statement(**self.characteristics)
        return ""

    @property
    def characteristic_ids(self):
        characteristics = {}
        if 'attribute' in self.characteristics:
            attribute = self.characteristics['attribute']
            characteristics['attribute_id'] = attribute.pk
        return characteristics

    def to_json(self):

        data = {
            'sample_id': self.sample_id
            ,'answers': self.answers
            ,'question_template_id': self.question_template_id
            ,'characteristics': self.characteristic_ids
        }

        return json.dumps(data)

    def _check_answer_key(self, guesses):

        if not self.sample.is_phishing and 'NONPHISH' in guesses:
            return True

        for guess in guesses:
            if guess not in self.answer_key:
                return False
        return True

    def _check_bool_answer_key(self, guess):

        if guess == self.answer_key:
                return True

        return False

    def is_correct(self, guess):

        # if self.category_code == QuestionCategory.essay_code:
        #     is_correct = True

        if self.category_code == QuestionCategory.true_false_code:
            guess_bool = None
            if guess == 'true':
                guess_bool = True
            elif guess == 'false':
                guess_bool = False

            is_correct = self._check_bool_answer_key(guess_bool)

        else:
            if not isinstance(guess, (list, set)):
                guess = [guess]

            is_correct = self._check_answer_key(guess)

        return is_correct
