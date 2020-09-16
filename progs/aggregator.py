#from progs.customenter import send_message,send_call,ricktwo
from progs.customenter import send_message,send_call,ricktwo,send_message_two
from datetime import datetime
#from datetime import timezone not used anmore
import pytz


#print('OUT')
def choice_help(num,msg,choi):
    #print('IN')
    print(choi)
    choi = int(choi)
    if choi == 0:
        #print('CALL SENT')
        send_call(num,msg)
    if choi == 1:
        #print('MSG SENT')
        send_message_two(num,msg)
    elif choi == 2:
        #print('RICK SENT')
        ricktwo(num)


def curr_time():
    eastern = pytz.timezone('US/Eastern')
    now = datetime.now()
    now = now.astimezone(eastern)
    #now = now.replace(tzinfo=timezone.utc)
    return now.strftime("%Y-%m-%d %H:%M:%S")

def choice_pass(ch):
    choice = int(ch)
    if choice == 0:
        return 'call'
    elif choice == 1:
        return 'text'
    else: 
        return 'rick roll'

#the comments in this were used for testing, the lesson learned is that
#test if a variable is a string or an int before passing it along!!!


