class Logger(object):

    def __init__(self):
        # Store last printed timestamp for each message
        self.last_seen = {}

    def shouldPrintMessage(self, timestamp, message):
        # STEP 1: If message not seen before
        if message not in self.last_seen:
            self.last_seen[message] = timestamp
            return True

        # STEP 2: Check time difference
        if timestamp - self.last_seen[message] >= 10:
            self.last_seen[message] = timestamp
            return True

        # STEP 3: Otherwise, do not print
        return False