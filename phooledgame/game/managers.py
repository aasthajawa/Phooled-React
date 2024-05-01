from django.db.models import Manager, Exists
from django.conf import settings

from game.choices import SampleFileType, PhishingFeedbackType
from game.querysets import PhishingSampleQuerySet, PhishingAttributeQuerySet, PhishingFeedbackQuerySet

from safedelete.managers import DELETED_VISIBLE, DELETED_ONLY_VISIBLE

from game.managers1 import RandomizationManager

class PhishingAttributeManager(RandomizationManager):
    _queryset_class = PhishingAttributeQuerySet

class PhishingAttributeAllManager(PhishingAttributeManager):
    _safedelete_visibility = DELETED_VISIBLE

class PhishingAttributeDeletedManager(PhishingAttributeManager):
    _safedelete_visibility = DELETED_ONLY_VISIBLE

class PhishingSampleManager(RandomizationManager):
    _queryset_class = PhishingSampleQuerySet

    def phishing(self):
        return self.get_queryset().phishing()

    def non_phishing(self):
        return self.get_queryset().non_phishing()

    def image_file(self):
        return self.get_queryset().image_file()

    def html_with_image_file(self):
        return self.get_queryset().html_with_image_file()

class PhishingSampleAllManager(PhishingSampleManager):
    _safedelete_visibility = DELETED_VISIBLE

class PhishingSampleDeletedManager(PhishingSampleManager):
    _safedelete_visibility = DELETED_ONLY_VISIBLE
class ImageSampleManager(PhishingSampleManager):

    def get_queryset(self):
        return super().image_file()

    def create(self, **kwargs):
        kwargs.update({"file_type": SampleFileType.image_code})
        return super().create(**kwargs)

class HtmlWithEmbeddedImageManager(PhishingSampleManager):
    
    def get_queryset(self):
        return super().html_with_image_file()

    def create(self, **kwargs):
        kwargs.update({"file_type": SampleFileType.html_with_image_code})
        return super().create(**kwargs)

class PhishingFeedbackManager(RandomizationManager):
    _queryset_class = PhishingFeedbackQuerySet
    
    def sample_answer(self):
        return self.get_queryset().sample_answer()

    def attribute_tip(self):
        return self.get_queryset().attribute_tip()

class PhishingFeedbackAllManager(PhishingFeedbackManager):
    _safedelete_visibility = DELETED_VISIBLE

class PhishingFeedbackDeletedManager(PhishingFeedbackManager):
    _safedelete_visibility = DELETED_ONLY_VISIBLE
class SampleAnswerManager(PhishingFeedbackManager):

    def get_queryset(self):
        return super().sample_answer()

    def create(self, **kwargs):
        kwargs.update({"feedback_type": PhishingFeedbackType.sample_answer_code})
        return super().create(**kwargs)

class AttributeTipManager(PhishingFeedbackManager):

    def get_queryset(self):
        return super().attribute_tip()

    def create(self, **kwargs):
        kwargs.update({"feedback_type": PhishingFeedbackType.attribute_tip_code})
        return super().create(**kwargs)