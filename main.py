import asyncio
import datetime
import json
from datetime import date
import time
import pandas as pd

import requests

import notifyEngine
import reader

PINCODE = reader.PINCODE
AGE = reader.AGE
EMAIL = reader.EMAIL



async def main():
     await checkAvailability()


async def checkAvailability():
    datelist = await fetchNext10Days()
    for date_item in datelist:
        #print(date_item)
        await getSlotsForDate(date_item)


async def getSlotsForDate(date):
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + PINCODE + '&date='+date
    headers = {
        'User-Agent': 'Chrome/39.0.2171.95',
        'accept': 'application/json',
        'Accept-Language': 'hi_IN'
    }
    run_flag = True
    while run_flag:
        try:
            response = requests.get(url, headers = headers)
            #print(response.text)
            response_session = json.loads(response.text)
            filter_slot = []

            for session in response_session['sessions']:
                if (session['min_age_limit'] == 18) and session['available_capacity'] > 0:
                    filter_slot.append(session)

            #    df = pd.DataFrame.from_dict(filter_slot)
            #    pd.set_option("display.max_rows", None, "display.max_columns", None)
            #    df.to_html('df.html')
            #    print(df)

            if len(filter_slot) > 0:
                for slots in filter_slot:
                    print(slots)
#               await sendnotification(filter_slot)
                run_flag = False

            else:
                print('No slots found for: ' + date)
                run_flag = True

        except:
            print("Unable to fetch data at the moment.")

        finally:
            print('sleeping for 5 secs......')
            time.sleep(5)

async def sendnotification(slots):
    message = json.dumps(slots)
    #print('message :::' + message)
    notifyEngine.notifyviamail('VACCINE AVAILABLE', message)


async def fetchNext10Days():
    datelist = []
    start_date = date.today()
    datelist.insert(0, start_date.strftime("%d/%m/%Y"))
    # print(start_date)
    delta = datetime.timedelta(days=1)
    for i in range(1, 7):
        start_date += delta
        #print(start_date)
        datelist.insert(i, start_date.strftime("%d/%m/%Y"))

    return datelist


asyncio.run(main())

