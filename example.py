# todo make example 
# - cli 
# - crontab
# - repl

import random
import datetime

from pushy_utils import send_message, get_templated_insult, make_message


import toml




def is_lucky(x=6):
    return random.randint(1,10) >= x


if __name__ == '__main__':
    dt = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
    print(f"[{dt}]: rolling 1d10...")

    if is_lucky():
        print("feeling lucky!")

        try:
            msg = get_templated_insult()
            payload = make_message(msg, 'somephonenumber') # sure thats a valid number
            send_message(payload)
        except:
            print("failed miserably")
        
    else:
        print('skipping this time')


