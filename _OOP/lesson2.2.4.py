class SoccerPlayer:

    def __init__(self, name='None', surname='None'):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"