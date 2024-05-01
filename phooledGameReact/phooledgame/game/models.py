from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from safedelete.models import SOFT_DELETE, SafeDeleteModel, SOFT_DELETE_CASCADE
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, Group, Permission
)
from shortuuid.django_fields import ShortUUIDField
from game.choices import (
    PhishingFeedbackType,
    PhishingSampleType,
    SampleFileType,
)
from game.managers import *
from django_fsm import FSMFieldMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from game.const import GameStates
from django.utils import timezone

def sample_upload_path(instance, filename):
    return "samples/type_{0}/{1}".format(instance.file_type, filename)

class PhishingAttribute(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    phishing_attribute_id = models.AutoField(primary_key=True)

    code = models.CharField(
        max_length=25,
        unique=True,
        help_text="Enter the code for the phishing attribute",
        verbose_name="Code",
    )

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name for the phishing attribute",
        verbose_name="Name",
    )

    description = models.CharField(
        max_length=255,
        help_text="Enter the description for the phishing attribute",
        verbose_name="Description",
    )

    objects = PhishingAttributeManager()
    all_objects = PhishingAttributeAllManager()
    deleted_objects = PhishingAttributeDeletedManager()

    class Meta:
        verbose_name = "Phishing Attribute"
        verbose_name_plural = "Phishing Attributes"
        db_table = "phishing_attribute"
        default_related_name = "phishing_attributes"

    def __str__(self):
        return self.name

class PhishingSample(SafeDeleteModel):
    safedelete_policy = SOFT_DELETE

    phishing_sample_id = models.AutoField(primary_key=True)

    identifier = models.CharField(
        ("identifier"),
        max_length=36,
        unique=True,
        help_text="Enter a unique identifier for the phishing sample.",
        editable=False,
    )

    file_type = models.CharField(
        max_length=10,
        choices=SampleFileType.get_choice_list(),
        default=SampleFileType.image_code,
        help_text="Choose a file type",
        verbose_name="File Type",
    )

    phishing_sample_file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=sample_upload_path,
        default="samples/default.html",
        help_text="Upload a phishing sample",
        verbose_name="Phishing Sample File",
    )

    thumbnail = models.ImageField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to=sample_upload_path,
        default="samples/default.png",
        help_text="Upload a thumbnail for the phishing sample",
        verbose_name="Thumbnail",
    )

    sample_type = models.CharField(
        max_length=25,
        choices=PhishingSampleType.get_choice_list(),
        help_text="Enter the sample type",
        verbose_name="Sample Type",
    )

    explanation = models.CharField(
        max_length=500,
        verbose_name="Explanation",
        help_text="Explain the attributes/sample type",
        blank=True,
        null=True,
        default=None,
    )

    phishing_attributes = models.ManyToManyField(PhishingAttribute, blank=True)

    test_sample = models.BooleanField(
        default=False,
        help_text="Select if this is a test sample",
        verbose_name="Test Sample",
    )

    objects = PhishingSampleManager()
    all_objects = PhishingSampleAllManager()
    deleted_objects = PhishingSampleDeletedManager()

    class Meta:
        db_table = "phishing_sample"
        default_related_name = "phishing_sample"
        verbose_name = "Phishing Sample"
        verbose_name_plural = "Phishing Samples"
        ordering = ["pk"]

    def get_display_attributes(self):
        return ",\n".join([str(a) for a in self.phishing_attributes.all()])

    @property
    def is_phishing(self):
        if self.sample_type == PhishingSampleType.phishing_code:
            return True
        else:
            return False

    def __str__(self):
        return str(self.pk) + " "
    
class PhishGameSession(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    id = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="id_",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    owner = models.IntegerField(default=0, null=False, blank=False)
    turn = models.IntegerField(default=0, null=False, blank=False)
    start_time = models.DateTimeField(default=timezone.now)
    num_cards = models.IntegerField(default=15, null=False, blank=False)
    qf_time_limit = models.IntegerField(default=60, null=False, blank=False)
    ar_time_limit = models.IntegerField(default=60, null=False, blank=False)
    fr_time_limit = models.IntegerField(default=30, null=False, blank=False)

    class Meta:
        verbose_name = "PhishGame Session"
        verbose_name_plural = "PhishGame Sessions"
        db_table = "phishgame_game_session"

    def __str__(self):
        return f"PhishGameSession: session_id=[{self.id}]"
    
class GameRoom(models.Model):
    """ room_name = models.CharField(max_length=255, default='Default Room Name')
    game_starter = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_rooms', null=True)
    players = models.ManyToManyField(User, related_name='joined_rooms')
    game_started = models.BooleanField(default=False)
    rules = models.TextField(null=True, blank=True)
    room_url = models.URLField(max_length=200, null=True, blank=True)  # Add the URL field """


class Image(models.Model):
    name = models.CharField(max_length=100, default='image')
    image = models.ImageField(upload_to='avatars/', null=True)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), username=username
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    
    user_id = models.AutoField(primary_key=True)

    email = models.EmailField(("email address"), unique=True)

    # TODO: Move from username system to just Full Name format?
    username = models.CharField(
        ("username"),
        max_length=150,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
    )

    date_joined = models.DateTimeField(("date joined"), auto_now_add=True)

    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=(
            "Designates whether the user can log into this data admin site."
        ),
    )

    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    # Specify custom related names for groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=("groups"), blank=True, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(Permission, verbose_name=("user permissions"), blank=True, related_name="custom_user_permissions_set")
    
    
    objects = MyAccountManager()


class GameState(SafeDeleteModel, FSMFieldMixin):
    CHOICES = (
        (GameStates.IDLE, GameStates.IDLE),
        (GameStates.GAME_PROPOSAL, GameStates.GAME_PROPOSAL),
        (GameStates.GAME_SETTINGS, GameStates.GAME_SETTINGS),
        (
            GameStates.SET_UP_QF_DISTRIBUTE_CARDS,
            GameStates.SET_UP_QF_DISTRIBUTE_CARDS,
        ),
        (GameStates.SET_UP_QF_READY_UP, GameStates.SET_UP_QF_READY_UP),
        (GameStates.QF_TEAR_DOWN, GameStates.QF_TEAR_DOWN),
        (GameStates.QUICK_FIRE, GameStates.QUICK_FIRE),
        (GameStates.SET_UP_AR, GameStates.SET_UP_AR),
        (GameStates.ARSENAL_ROUND, GameStates.ARSENAL_ROUND),
        (GameStates.SET_UP_FR, GameStates.SET_UP_FR),
        (GameStates.FR_INIT, GameStates.FR_INIT),
        (GameStates.FR_CLASSIFY_INIT, GameStates.FR_CLASSIFY_INIT),
        (GameStates.FR_CLASSIFY, GameStates.FR_CLASSIFY),
        (GameStates.FR_CLASSIFY_TEAR_DOWN, GameStates.FR_CLASSIFY_TEAR_DOWN),
        (GameStates.FR_CLASSIFY_RESULT, GameStates.FR_CLASSIFY_RESULT),
        (GameStates.FR_INIT_ATTR, GameStates.FR_INIT_ATTR),
        (GameStates.FR_ATTR_SOLO, GameStates.FR_ATTR_SOLO),
        (GameStates.FR_ATTR_GROUP, GameStates.FR_ATTR_GROUP),
        (GameStates.FR_ATTR_TEAR_DOWN, GameStates.FR_ATTR_TEAR_DOWN),
        (GameStates.FR_ATTR_RESULT, GameStates.FR_ATTR_RESULT),
        (GameStates.FR_RESULT, GameStates.FR_RESULT),
        (GameStates.FR_WILD, GameStates.FR_WILD),
        (GameStates.FINISH, GameStates.FINISH),
    )

    
    state = models.CharField(max_length=30, choices=CHOICES, default="idle")
    session = models.ForeignKey(PhishGameSession, on_delete=models.CASCADE)

    def on_change_state(self, previous_state, next_state, **kwargs):
        self.save()


class PhishGameSessionPlayer(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    session = models.ForeignKey(PhishGameSession, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE
    )
    channel_name = models.CharField(max_length=77)
    connect = models.BooleanField(default=True, null=False, blank=False)

    lifePoints = models.IntegerField(default=100, null=False, blank=False)
    coins = models.IntegerField(default=0, null=False, blank=False)

    ready = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"PhishGameSessionPlayer: user=[{self.user}]"

    class Meta:
        verbose_name = "Session Player"
        verbose_name_plural = "Session Players"
        db_table = "phishgame_game_session_player"


class PhishGameSessionCards(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    session = models.ForeignKey(PhishGameSession, on_delete=models.CASCADE)
    card = models.ForeignKey(PhishingSample, on_delete=models.CASCADE)
    # owner
    # 0 - server
    # other int - owner's player id
    # TODO: make this a foreign key to PhishGameSessionPlayer
    owner = models.IntegerField(default=0, null=False, blank=False)

    # classification values
    # 0 - no classification (default)
    # 1 - phish
    # 2 - nonphish
    # 3 - discard (NOTE: probably not used anymore)
    # 4 - on table (NOTE: probably not used anymore)
    classification = models.IntegerField(default=0, null=False, blank=False)

    # selected cards in arsenal round
    # 0 - card not selected (default)
    # 1 - card selected
    selected = models.IntegerField(default=0, null=False, blank=False)

    played = models.IntegerField(default=0, null=False, blank=False)

    # TODO: is this timestamp needed? If it was added only for tracking, could probably use the log instead... Would need to do this anyway for the attributes below.
    timestamp = models.DateTimeField(default=timezone.now)

    
    class Meta:
        verbose_name = "Session Card"
        verbose_name_plural = "Session Cards"
        db_table = "phishgame_game_session_card"
        ordering = ["timestamp"]



class PhishGameSessionAttribute(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    card = models.ForeignKey(PhishGameSessionCards, on_delete=models.CASCADE)
    attribute = models.ForeignKey(PhishingAttribute, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Session Attribute"
        verbose_name_plural = "Session Attributes"
        db_table = "phishgame_game_session_attribute"


