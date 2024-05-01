""" Gameification Form Configuration

Forms are used for all aspects of the game system

"""
from django import forms

from phish.choices import SampleFileType
from gamification.choices import QuestionCategory

from gamification.models import Feedback

class QuestionMixin:
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value

    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, value):
        self._statement = statement

    @property
    def is_html_with_image(self):
        return self.file_type == SampleFileType.html_with_image_code

    @property
    def is_phishing(self):
        return self._is_phishing


class MultipleChoiceForm(forms.Form, QuestionMixin):
    def __init__(self, question=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        answers = question.answers
        if question.category_code is not QuestionCategory.true_false_code:
            answers = tuple(list(answers) + [('NONPHISH', 'Not a phishing mail')])
        self.fields["answers"] = forms.ChoiceField(
            choices=answers, widget=forms.RadioSelect
        )

        self._file_type = question.sample.file_type
        self._file_url = question.sample.phishing_sample_file.url
        self._statement = question.question_statement
        self._is_phishing = question.sample.is_phishing

class MultipleSelectionForm(forms.Form, QuestionMixin):
    def __init__(self, question=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        answers = tuple(list(question.answers) + [('NONPHISH', 'Not a phishing mail')])
        self.fields["answers"] = forms.MultipleChoiceField(
            choices=answers, widget=forms.CheckboxSelectMultiple
        )

        self._file_type = question.sample.file_type
        self._file_url = question.sample.phishing_sample_file.url
        self._statement = question.question_statement
        self._is_phishing = question.sample.is_phishing


# class EssayForm(forms.Form, QuestionMixin):
#     def __init__(self, question=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["answers"] = forms.CharField(
#             widget=forms.Textarea(attrs={"style": "width:100%", "rows": 5, "cols": 50})
#         )

#         self._file_type = question.sample.file_type
#         self._file_url = question.sample.phishing_sample_file.url
#         self._statement = question.question_statement


class FeedbackForm(forms.ModelForm): #This is how the text box is going to be created. This is a Django form, much more feature rich than basic HTML forms
    # feedback_type_choices= [
    #         ("Bug","Bug"),
    #         ("Feature","Feature Request"),
    #         ("Attribute Issue", "Wrong/Missing Attribute"),
    #     ],
    # feedback_message = forms.CharField(max_length=200, label="Feedback",) #This is the text box specifically, to edit the box you must edit this
    # feedback_type = forms.CharField(label= "What type of feedback would you like to submit?", widget=forms.Select(choices=feedback_type_choices))
    # feedback_sample_id = forms.IntegerField()
    class Meta: #This bounds the form with a specific model so that we can easily save to it
        model = Feedback
        fields = ('feedback_type','feedback','sample_id')
        widgets = {
            'feedback': forms.Textarea(attrs={'cols': 80, 'rows':12}),
        }
