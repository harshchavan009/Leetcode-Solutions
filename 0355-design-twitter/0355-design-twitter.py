import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> list of (time, tweetId)
        self.following = {}   # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        users = set(self.following.get(userId, set()))
        users.add(userId)

        heap = []

        # Add the most recent tweet of each relevant user
        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))

        result = []

        # Get at most 10 most recent tweets
        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)

            # Add the next older tweet from the same user
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[uid][index]
                heapq.heappush(heap, (-time, tweetId, uid, index))

        return result

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)