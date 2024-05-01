from game.choices import PhishingSampleType, SampleFileType, PhishingFeedbackType
from game.queryset import RandomizationQuery

class PhishingAttributeQuerySet(RandomizationQuery):
    pass

class PhishingSampleQuerySet(RandomizationQuery):

    def phishing(self):
        return self.filter(sample_type=PhishingSampleType.phishing_code)

    def non_phishing(self):
        return self.filter(sample_type=PhishingSampleType.non_phishing_code)

    def image_file(self):
        return self.filter(file_type=SampleFileType.image_code)

    def html_with_image_file(self):
        return self.filter(file_type=SampleFileType.html_with_image_code)

class PhishingFeedbackQuerySet(RandomizationQuery):

    def sample_answer(self):
        return self.filter(feeback_type=PhishingFeedbackType.sample_answer_code)

    def attribute_tip(self):
        return self.filter(feeback_type=PhishingFeedbackType.attribute_tip_code)
