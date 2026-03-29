class Leaderboard(object):

    def __init__(self):
        # Store playerId -> score
        self.scores = {}

    def addScore(self, playerId, score):
        # If player exists, add to their score
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            # Otherwise create new player
            self.scores[playerId] = score

    def top(self, K):
        # Get all scores
        all_scores = self.scores.values()

        # Sort scores in descending order
        sorted_scores = sorted(all_scores, reverse=True)

        # Sum top K scores
        return sum(sorted_scores[:K])

    def reset(self, playerId):
        # Remove player from leaderboard
        if playerId in self.scores:
            del self.scores[playerId]