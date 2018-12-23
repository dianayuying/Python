class Pong:
    def __init__(self, max_score):
        self.max_score = max_score;
        self.score = [0,0]
        self.player = 0
        self.gameover = False

    def check_score(self):
        if not self.gameover:
            for i in self.score:
                if i==self.max_score:
                    self.gameover = True
                    return "Player "+ str((self.player+1)%2+1)+" has won the game!"
                else:
                    return "-"
        else:
            return "Game Over!"

    def play(self, ball_pos, player_pos):
        if abs(ball_pos-player_pos)>3:
            text = "Player "+ str(self.player+1)+" has missed the ball!"
            self.score[self.player] += 1
            ck_text = self.check_score()
            if ck_text!="-":
                text = ck_text
        else:
            ck_text = self.check_score()
            if ck_text!="-":
                text = ck_text
            else:
                text = "Player "+ str(self.player+1)+" has hit the ball!"
        self.player = (self.player+1)%2
        return text
        
# Other Best Practices:
from itertools import cycle

class Pong:
    def __init__(self, max_score):
        self.max_score = max_score;
        self.scores = {1: 0, 2: 0}
        self.players = cycle((1, 2))

    def game_over(self):
        return any(score >= self.max_score for score in self.scores.values())

    def play(self, ball_pos, player_pos):
        if self.game_over():
            return "Game Over!"
 
        player = next(self.players)
        if abs(ball_pos - player_pos) <= 3:
            return "Player {} has hit the ball!".format(player)
        else:
            self.scores[player] += 1
            if self.scores[player] == self.max_score:
                return "Player {} has won the game!".format(next(self.players))
            else:
                return "Player {} has missed the ball!".format(player)
'''-----------
Test:'''
@test.describe('Sample Tests')
def example_tests():
    @test.it('Should pass sample tests')
    def example_test_case():
        game = Pong(2)
        test.assert_equals(game.play(50, 53), "Player 1 has hit the ball!")
        test.assert_equals(game.play(100, 97), "Player 2 has hit the ball!")
        test.assert_equals(game.play(0, 4), "Player 1 has missed the ball!")
        test.assert_equals(game.play(25, 25), "Player 2 has hit the ball!")
        test.assert_equals(game.play(75, 25), "Player 2 has won the game!")
        test.assert_equals(game.play(50, 50), "Game Over!")