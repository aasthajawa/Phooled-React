import logging
import multiprocessing
import os
import random
import subprocess

#from account.models import Avatar
#from phish.models import PhishingSample

from . import utils

from .models import (
    GameState,
    PhishGameSession,
    #PhishGameSessionCards,
    #PhishGameSessionPlayer,
    #PhishGameSessionScores,
)


# TODO: refactor class to be an instance
class GameEngine:
    
    def run_relay_script(self, room_id):
        self.logger.info("Starting process for room_id: %s", room_id)
        cmd = [
            utils.get_instance_python_path(),
            os.path.join("scripts", "relay.py"),
            room_id,
        ]
        subprocess.run(cmd)


    def __init__(self):
        self.logger = logging.getLogger("game.game_engine")

    def create_new_session(self, session_id):
        s = PhishGameSession(id=session_id)
        s.save()

        self.init_game_state(s)
        # setup_relay.delay(session_id)
        self.setup_relay(session_id)

        return s

    def init_game_state(self, session):
        self.logger.info("Setting game state for %s", session)
        game_state_obj = GameState(session=session)
        game_state_obj.save()

    def setup_relay(self, room_id):
        self.logger.info("Starting task: setup_relay")
        process = multiprocessing.Process(
            target=self.run_relay_script, args=(room_id,)
        )
        process.start()
        return process
    
    """def get_session(self, session_id):
        return PhishGameSession.objects.filter(id=session_id).first()

    def get_user(self, user_id):
        return Account.objects.filter(user_id=user_id).first()

    def add_player_to_session(self, session_id, player_id, channel_name):
        self.logger.info("Adding %s to %s", player_id, session_id)
        player_session_obj = PhishGameSessionPlayer(
            session=session_id, user=player_id, channel_name=channel_name
        )
        player_session_obj.save()

        return player_session_obj

    def disconnect_player_from_session(self, session_id, channel_name):
        self.logger.info("Disconnecting channel: %s", channel_name)
        pgs = PhishGameSessionPlayer.objects.filter(
            session=session_id, channel_name=channel_name
        ).first()

        if pgs == None:
            return False

        pgs.connect = False
        pgs.save()

        return True

    def get_count_connected_players(self, session_id):
        return PhishGameSessionPlayer.objects.filter(
            session_id=session_id, connect=True
        ).count()

    def check_user_in_session(self, session, player):
        return PhishGameSessionPlayer.objects.filter(
            session=session, user=player
        ).first()

    def get_relay_client(self):
        return Account.objects.filter(is_relay=True).first()

    def get_players_list(self, session):
        return PhishGameSessionPlayer.objects.filter(
            session=session, user__is_relay=False
        )

    def get_available_avatars(self, count=5):
        return Avatar.objects.all()[:count]

    def increment_game_turn(self, session):
        s = self.get_session(session)
        s.turn += 1
        s.save()

    def get_game_turn(self, session):
        s = self.get_session(session)
        return s.turn

    def draw_from_database(self, session):
        all_samples = list(PhishingSample.objects.all())

        random_samples = random.sample(all_samples, len(all_samples))

        for sample in random_samples:
            c = PhishGameSessionCards(session=session, card=sample)
            c.save()

    def distribute_cards(self, session, numCards, extra_cards=0):
        # cards_to_assign = PhishGameSessionCards.objects.filter(
        #     session=session, owner=0
        # )
        session_players = PhishGameSessionPlayer.objects.filter(
            session=session, user__is_relay=False
        )
        self.logger.info(
            "The players in this session are: %s", session_players
        )
        session_players_count = session_players.count()

        self.logger.info("The number of players is %s", session_players_count)

        # Check if there are players in the game
        if session_players_count == 0:
            self.logger.info("No players found for this session.")
            return

        # check if the total number of cards to be distributed is  more than the actual number of cards in database
        # if (numCards * (session_players_count - 1)) > cards_to_assign.count():
        #     self.logger.info("Not enough cards available for distribution.")
        #     return

        for player in session_players:
            if (
                player.user_id
                == Account.objects.filter(is_relay=True).first().user_id
            ):  # id 4 being the id of the relay
                continue

            # Check if player already has cards in their array
            if PhishGameSessionCards.objects.filter(
                session=session, owner=player.user_id
            ).exists():
                self.logger.info(
                    "Player %s already has cards in their hands.",
                    player.user_id,
                )
                continue
            self.draw_to_player_hand(session, player, numCards)
            self.draw_to_player_hand(session, player, extra_cards, True)
            # player_cards = cards_to_assign[:numCards]
            # for card in player_cards:
            #     card.owner = player.user_id
            #     card.save()
            # cards_to_assign = cards_to_assign[numCards:]

    def draw_to_player_hand(self, session, player, num_cards, extra=False):
        
        
        already_drawn_cards = PhishGameSessionCards.objects.filter(
            session=session
        ).values_list("card__phishing_sample_id", flat=True)

        self.logger.info(
            "Already drawn cards: %s (%s)",
            already_drawn_cards,
            len(already_drawn_cards),
        )

        remaining_cards = PhishingSample.objects.exclude(
            phishing_sample_id__in=already_drawn_cards
        ).values_list("phishing_sample_id", flat=True)

        self.logger.info(
            "Remaining cards: %s (%s)", remaining_cards, len(remaining_cards)
        )

        random_ids = random.sample(list(remaining_cards), num_cards)

        random_samples = PhishingSample.objects.filter(
            phishing_sample_id__in=random_ids
        )

        cards_to_draw = [
            PhishGameSessionCards(
                session=session,
                owner=player.user_id,
                card=sample,
                selected=not extra,
            )
            for sample in random_samples
        ]
        PhishGameSessionCards.objects.bulk_create(cards_to_draw)

        return random_samples

    def get_player_channel(self, session, user):
        return PhishGameSessionPlayer.objects.filter(
            session=session, user=user
        ).first()

    def get_cards_for_session(self, session):
        session_cards = PhishGameSessionCards.objects.filter(session=session)

        player_card_data = {}
        for session_card in session_cards:
            if session_card.owner in player_card_data.keys():
                player_card_data[session_card.owner].append(session_card)
            else:
                player_card_data[session_card.owner] = [session_card]

        return player_card_data

    def update_card_classification(
        self, session, user, card_id, classification
    ):
        this_card = PhishingSample.objects.filter(identifier=card_id).first()

        card_to_update = PhishGameSessionCards.objects.filter(
            session=session, owner=user.user_id, card=this_card
        ).first()
        # This part is hit when the card doesn't exist in the user's hand
        # already but we want to store a classification. This happens when
        # the user is not the attacker.
        if card_to_update == None:
            print("Creating session card to store classification")
            card_to_update = PhishGameSessionCards(
                session=session, owner=user.user_id, card=this_card, selected=0
            )

        card_to_update.classification = classification
        card_to_update.save()

    def update_card_flip(self, session, user, card_id, flip):
        this_card = PhishingSample.objects.filter(identifier=card_id).first()
        card_to_update = PhishGameSessionCards.objects.filter(
            session=session, owner=user.user_id, card=this_card
        ).first()
        card_to_update.flip = flip
        card_to_update.save()

    def modify_life_points(self, session, user, lifepoints):
        this_player = PhishGameSessionPlayer.objects.filter(
            session=session, user=user
        ).first()
        self.logger.info("prev: %s", this_player.lifePoints)
        this_player.lifePoints = (
            this_player.lifePoints + lifepoints
        )  # TODO calculate life points
        self.logger.info("new: %s", this_player.lifePoints)
        this_player.save()

    def modify_coins(self, session, user, coins):
        this_player = PhishGameSessionPlayer.objects.filter(
            session=session, user=user
        ).first()
        this_player.coins = this_player.coins + coins  # TODO calculate coins
        this_player.save()

    def set_game_settings(
        self,
        session_id,
        num_cards,
        qf_time_limit,
        ar_time_limit,
        fr_time_limit,
    ):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        this_session.num_cards = num_cards
        this_session.qf_time_limit = qf_time_limit
        this_session.ar_time_limit = ar_time_limit
        this_session.fr_time_limit = fr_time_limit
        this_session.save()

    def get_num_cards(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.num_cards

    def get_qf_time_limit(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.qf_time_limit

    def get_ar_time_limit(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.ar_time_limit

    def get_fr_time_limit(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.fr_time_limit

    def get_start_time(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.start_time

    def get_cards_in_hand(self, session):
        cards_in_hand = PhishGameSessionCards.objects.filter(
            session=session, selected=1, played=0
        )

        player_card_data = {}
        for session_card in cards_in_hand:
            if session_card.owner in player_card_data.keys():
                if session_card.selected == 1:
                    player_card_data[session_card.owner].append(
                        session_card.card
                    )
            else:
                player_card_data[session_card.owner] = [session_card.card]

        return player_card_data

    def update_card_selected(self, session, user, card_id, selected):
        this_card = PhishingSample.objects.filter(identifier=card_id).first()

        card_to_update = PhishGameSessionCards.objects.filter(
            session=session, owner=user.user_id, card=this_card
        ).first()
        card_to_update.selected = selected
        card_to_update.save()

    def update_card_played(self, session, user, card_id):
        this_card = PhishingSample.objects.filter(identifier=card_id).first()

        card_to_update = PhishGameSessionCards.objects.filter(
            session=session, owner=user.user_id, card=this_card
        ).first()
        card_to_update.played = 1
        card_to_update.save()

    def set_owner(self, session_id, user_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        this_session.owner = user_id
        this_session.save()

    def get_owner(self, session_id):
        this_session = PhishGameSession.objects.filter(id=session_id).first()
        return this_session.owner

    def update_ready_status(self, session, user, ready):
        this_player = PhishGameSessionPlayer.objects.filter(
            session=session, user=user
        ).first()
        this_player.ready = ready
        this_player.save()

    def get_all_players_ready(self, session):
        session_players = PhishGameSessionPlayer.objects.filter(
            session=session
        )

        for player in session_players:
            if (
                player.user_id
                == Account.objects.filter(is_relay=True).first().user_id
            ):  # id 4 being the id of the relay
                continue
            # verify if all players are ready
            if player.ready != 1:
                return False
        return True

    def reset_ready_status(self, session):
        session_players = PhishGameSessionPlayer.objects.filter(
            session=session
        )

        for player in session_players:
            if (
                player.user_id
                == Account.objects.filter(is_relay=True).first().user_id
            ):  # id 4 being the id of the relay
                continue
            # verify if all players are ready
            player.ready = 0

    def get_player_card_list(self, session, owner_id):
        return PhishGameSessionCards.objects.filter(
            session=session, owner=owner_id
        )

    def get_card_sample_type(self, card_id):
        this_card = PhishingSample.objects.filter(identifier=card_id).first()
        return this_card.sample_type

    def update_player_lifePoints(self, session, user, lifePoints):
        player_session_obj = PhishGameSessionScores(
            session=session, user=user, lifePoints=lifePoints
        )
        player_session_obj.save()

    def get_life_points(self, session, user):
        this_player = PhishGameSessionPlayer.objects.filter(
            session=session, user=user
        ).first()
        return this_player.lifePoints

    

    def _get_session_state(self, session):
        return GameState.objects.filter(session=session).first()

    def get_current_state(self, session):
        return self._get_session_state(session=session).current_state()

    def change_state(self, session, next_state):
        current_state = self.get_current_state(session)
        self.logger.info(
            "Switching states from %s to %s", current_state, next_state
        )

        return self._get_session_state(session=session).change_state(
            next_state=next_state
        )

    def update_player_avatar(self, user, avatar_id):
        selected_avatar = Avatar.objects.filter(id=avatar_id).first()
        user.avatar = selected_avatar
        user.save()"""
 