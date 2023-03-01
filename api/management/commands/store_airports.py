from .models import 


from api.base import Processor


class Command(Processor):

    def add_arguments(self, parser):
        parser.add_argument('Competition', type=str,
                            help='Requires competition name: LIGA')

    def handle(self, *args, **kwargs):

        try:

            competition = kwargs['Competition']

            league = League.objects.filter(friendly_name=competition).first()

            teams = Team.objects.filter(league=league)

            # get list of injured players in that league
            injury_data = self.get_data(
                param=kwargs['Competition'], url_="projections/", url='InjuredPlayers/')

            injury_list = []

            for data in injury_data:
                injury_list.append(data['PlayerId'])

            for team in teams:

                response = self.get_data(
                    param=str(f'{team.teamid}'), url_="scores/", url='PlayersByTeam/')

                for player in response:

                    if player['PlayerId'] in injury_list:
                        injured = True

                    else:
                        injured = False

                    Player.objects.update_or_create(
                        playerid=player['PlayerId'], defaults=dict(
                            updated_at=timezone.now(),
                            league=league,
                            team=team,
                            teamid=team.teamid,
                            team_name=team.fullname,
                            player_image=player['PhotoUrl'],
                            team_key=team.key,
                            playerid=player["PlayerId"],
                            firstname=player["FirstName"],
                            lastname=player["LastName"],
                            injury_status=injured,
                            common_name=player["CommonName"],
                            shortname=player["ShortName"],
                            position=player["Position"],
                            position_category=player["PositionCategory"],
                            jersey=player["Jersey"],
                            foot=player["Foot"],
                            height=player["Height"],
                            weight=player["Weight"],
                            gender=player["Gender"],
                            birthdate=player["BirthDate"],
                            birth_city=player["BirthCity"],
                            birth_country=player["BirthCountry"],
                            nationality=player["Nationality"]
                        ))

            return competition

        except Exception as e:
            print(e)