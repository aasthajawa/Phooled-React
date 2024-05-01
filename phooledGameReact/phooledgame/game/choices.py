"""
This file contains all the choice fields that are used throughout
the phishing app. All choices are a class.
"""


class PhishingSampleType:
    """
    The type of phishing sample that can be selected for a question.
    """

    # List all codes below
    phishing_code = "PHISH"
    non_phishing_code = "NONPHISH"

    # List all descriptions below
    phishing_description = "Phishing"
    non_phishing_description = "Non-Phishing"

    @classmethod
    def get_choice_list(cls):
        """ 
		Return a list 
		"""
        return [
            (cls.phishing_code, cls.phishing_description),
            (cls.non_phishing_code, cls.non_phishing_description),
        ]

    @classmethod
    def phishing(cls):
        """ 
		Return a dictonary 
		"""
        return {"code": cls.phishing_code, "description": cls.phishing_description}

    @classmethod
    def nonPhishing(cls):
        """ 
		Return a dictonary 
		"""
        return {
            "code": cls.non_phishing_code,
            "description": cls.non_phishing_description,
        }


class SampleFileType:
    """
    The type of file types that a sample can be.
    """

    # List all codes below
    image_code = "IMG"
    html_with_image_code = "HTML-IMG"

    # List all descriptions below
    image_description = "Image"
    html_with_image_description = "HTML with Embedded Image"

    @classmethod
    def get_choice_list(cls):
        """ 
		Return a list 
		"""
        return [
            (cls.image_code, cls.image_description),
            (cls.html_with_image_code, cls.html_with_image_description),
        ]

    @classmethod
    def image(cls):
        """ 
		Return a dictonary 
		
		Dictonary contains all attributes for a quiz session
		"""
        return {"code": cls.image_code, "description": cls.image_description}

    @classmethod
    def image(cls):
        """ 
		Return a dictonary 
		
		Dictonary contains all attributes for a quiz session
		"""
        return {
            "code": cls.html_with_image_code,
            "description": cls.html_with_image_description,
        }

class PhishingFeedbackType:
    """
    The type of feedbacks that can go for phishing attributes
    """

    # List all codes below
    attribute_tip_code = "ATTRIBUTE-TIP"
    sample_answer_code = "SAMPLE-ANSWER"

    # List all descriptions below
    attribute_tip_description = "Attribute Tip"
    sample_answer_description = "Sample Answer"

    @classmethod
    def get_choice_list(cls):
        """ 
		Return a list 
		"""
        return [
            (cls.attribute_tip_code, cls.attribute_tip_description),
            (cls.sample_answer_code, cls.sample_answer_description),
        ]

    @classmethod
    def attributeTip(cls):
        """ 
		Return a dictonary 
		
		Dictonary contains all attributes for a quiz session
		"""
        return {"code": cls.attribute_tip_code, "description": cls.attribute_tip_description}

    @classmethod
    def sampleAnser(cls):
        """ 
		Return a dictonary 
		
		Dictonary contains all attributes for a quiz session
		"""
        return {
            "code": cls.sample_answer_image_code,
            "description": cls.sample_answer_description,
        }
