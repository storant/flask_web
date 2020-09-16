
from datetime import datetime
from datetime import timezone
import pytz

def curr_time():
    eastern = pytz.timezone('US/Eastern')
    now = datetime.now()
    now = now.astimezone(eastern)
    #now = now.replace(tzinfo=timezone.utc)
    return now.strftime("%Y-%m-%d %H:%M:%S")
