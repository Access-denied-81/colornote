# drawing_app/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DrawingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join a group when a WebSocket connection is established
        self.group_name = 'drawing_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group when a WebSocket connection is closed
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Handle incoming drawing data
        data = json.loads(text_data)
        # Process the data as needed (e.g., save to the database)
        # Broadcast the drawing data to all other users in the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'drawing_message',
                'data': data,
            }
        )

    async def drawing_message(self, event):
        # Send drawing data to the WebSocket
        data = event['data']
        # Send the received drawing data to the WebSocket
        await self.send(text_data=json.dumps(data))
