import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from chat.models import Room

log = logging.getLogger(__name__)

@channel_session
def ws_connect(message):
    prefix, label = message['path'].strip('/').split('/')
    room = Room.objects.get(label=label)
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = room.label
    message.reply_channel.send({'accept': True})

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    data = json.loads(message['text'])
    m = room.messages.create(handle=data['handle'], message=data['message'])
    Group('chat-'+label).send({'text': json.dumps(m.as_dict())})

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)						
