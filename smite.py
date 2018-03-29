import requests
import json
import datetime
import time

prev_val = ''
for x in range(0, 10000):
    print 'go'
    history = requests.get(url="https://mixer.com/api/v1/chats/19088261/history")

    content = json.loads(history.content)
    #print content
    #print content
    for element in content:

        data = element['message']['message'][0]['data']

        if any(x in data.lower() for x in ['poll started', 'most recent code', 'poll results']) :
            val = "{} {}".format(element['user_name'], data)

            if prev_val == val:
                continue

            prev_val = "{} {}".format(element['user_name'], data)

            channelID = "428596424515649536" # enable dev mode on discord, right-click on the channel, copy ID
            botToken = "NDI4NTk5Mjg1MTk4ODgwNzcw.DZ1b-Q.5D5yYV2HvNRK8U3KLXGmj4eKcfo"    # get from the bot page. must be a bot, not a discord app

            baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
            headers = { "Authorization":"Bot {}".format(botToken),
                        "User-Agent":"myBotThing)",
                        "Content-Type":"application/json", }

            POSTedJSON = json.dumps ({"content":val})
            time.sleep(1)
            r = requests.post(baseURL, headers=headers, data=POSTedJSON)
            print r.content

    time.sleep(10)