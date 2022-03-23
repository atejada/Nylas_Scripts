from dotenv import load_dotenv
load_dotenv()

import os
from datetime import date
import datetime
from nylas import APIClient

nylas = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN")
)

today = date.today()
file_name = today.strftime('%d %b %Y') + ".md"

AFTER = int(datetime.datetime(today.year, today.month, 
today.day, 0, 0, 0).strftime('%s'))
BEFORE = int(datetime.datetime(today.year, today.month,
 today.day, 23, 59, 59).strftime('%s'))

events = nylas.events.where(calendar_id = os.environ.get("CALENDAR_ID"), 
                            starts_after=AFTER, ends_before=BEFORE)

with open(file_name, 'w') as f:
	f.write("# {}\n\n".format(today.strftime('%d %b %Y')))
	f.write("--------\n\n")
	f.write("## Events:\n\n")
	for event in events:
		start_time = datetime.datetime. \
		fromtimestamp(event.when["start_time"]).strftime('%H:%M:%S')
		end_time = datetime.datetime. \
		fromtimestamp(event.when["end_time"]).strftime('%H:%M:%S')
		f.write("{} {} {} \n\n".format(start_time, end_time, event.title))
	f.write("--------")
