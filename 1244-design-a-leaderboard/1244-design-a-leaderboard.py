import heapq

class Leaderboard(object):

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId, score):
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    def top(self, K):
        min_heap = []

        for score in self.scores.values():

            if len(min_heap) < K:
                heapq.heappush(min_heap, score)

            elif score > min_heap[0]:
                heapq.heapreplace(min_heap, score)

        return sum(min_heap)

    def reset(self, playerId):
        if playerId in self.scores:
            del self.scores[playerId]