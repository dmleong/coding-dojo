from time import strftime
import datetime
from system.core.controller import *

class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)

    def times(self):
        now = datetime.datetime.now().strftime("%B %-d, %Y %-I:%M %p")
        return self.load_view('time.html', now=now)
