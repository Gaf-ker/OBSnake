# More information on OBS scripting https://obsproject.com/docs/
import obspython as obs
import os

# Trying importing requests library, install it via pip if unavailable.
try:
    import requests
except ImportError:
    os.system('python -m pip install requests')
    import requests

# Global variables, should have just used Class for it.
stream_link = ""
description = ""
ds_token = ""
ds_channel = ""
tg_token = ""
tg_channel = ""


# Send message using telegram API
def send_msg(token, msg, channel):
    """
    Sends a message to telegram channel

    :param token: str, telegram bot API token
    :param msg: str, Text of the message
    :param channel: str, Channel name or id
    :return: json, returns json reply
    """
    get_url = "https://api.telegram.org/bot{}/sendMessage".format(token)
    if token != '':
        a = requests.get(get_url, {
            'chat_id': channel,
            'text': msg,
            'disable_notification': True
        }).json()
        return a
    else:
        pass


# Send message using discord webhook
def send_msg_dis(token, msg):
    """
       Sends a message to Discord channel

       :param token: str, discord webhook
       :param msg: str, Text of the message
       :return: json, returns json reply
       """
    get_url = token
    if token != '':
        requests.post(get_url, {
            "content": msg
            })
    else:
        pass


# Description for OBS script
def script_description():
    return "OBSnake \n\n" \
           "OBSnake is a simple discord/telegram notification script" \



# Default OBS script settings
def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "stream_link", "")
    obs.obs_data_set_default_string(settings, "description", "Hey, I'm live :): ")
    obs.obs_data_set_default_string(settings, "ds_token", "")
    obs.obs_data_set_default_string(settings, "tg_token", "")
    obs.obs_data_set_default_string(settings, "tg_channel", "")


# GUI elements for the scripts
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "stream_link", "Stream link", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "description", "Description", obs.OBS_TEXT_MULTILINE)
    obs.obs_properties_add_text(props, "ds_token", "Discord webhook", obs.OBS_TEXT_PASSWORD)
    obs.obs_properties_add_text(props, "tg_token", "Telegram bot token", obs.OBS_TEXT_PASSWORD)
    obs.obs_properties_add_text(props, "tg_channel", "Telegram channel", obs.OBS_TEXT_DEFAULT)

    return props


# Handling data import from GUI
def script_update(settings):
    global stream_link, description, ds_token, tg_token, tg_channel, ds_channel
    stream_link = obs.obs_data_get_string(settings, "stream_link")
    description = obs.obs_data_get_string(settings, "description")
    ds_token = obs.obs_data_get_string(settings, "ds_token")
    tg_token = obs.obs_data_get_string(settings, "tg_token")
    tg_channel = "@{}".format(obs.obs_data_get_string(settings, "tg_channel"))


# Callback function for when an event occurs
def call_back(event):
    if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTED:
        msg = "{}, {}".format(stream_link, description)
        print("{}, {}".format(stream_link, description))
        print(send_msg(tg_token, msg, tg_channel))
        send_msg_dis(ds_token, msg)


obs.obs_frontend_add_event_callback(call_back)
