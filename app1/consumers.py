# C:\Users\yuvraj\Desktop\Career-Guidance-System - Copy\loginform\app1\consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
import google.generativeai as genai # Import the Gemini API library # Import the Gemini API library# Import the Gemini API library
from django.conf import settings # Import settings to access GEMINI_API_KEY
from asgiref.sync import sync_to_async
import asyncio

class LiveChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'global_live_chat_room'
        self.room_group_name = f'chat_{self.room_name}'

        # Add this consumer's channel to the group for this room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept() # Accept the WebSocket connection

    async def disconnect(self, close_code):
        # Remove this consumer's channel from the group when disconnected
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket (from the client browser)
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json.get('sender', 'Anonymous')

        # First, send the user's message to the entire room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
            }
        )

        # --- AI Response Logic (This is the NEW part you need to add/ensure is there!) ---
        # Configure Gemini API with your key from settings.py
        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            # Use 'gemini-1.5-pro-latest' for text-only responses
            model = genai.GenerativeModel('gemini-1.5-pro-latest')
            
            # Generate content from Gemini based on the user's message
            # Use sync_to_async to run synchronous generate_content in async context
            response_ai = await sync_to_async(model.generate_content)(message)
            ai_message = response_ai.text # Extract the text content from the AI's response
            ai_sender = "Gemini AI" # Or "Assistant", "Bot", etc.

            # Send the AI's response back to the entire room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': ai_message,
                    'sender': ai_sender,
                }
            )
        except Exception as e:
            # Handle potential errors during API call or response processing
            error_message = f"AI Error: {str(e)}"
            print(f"Error calling Gemini API: {e}") # Print to Daphne console for debugging
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': error_message,
                    'sender': "System Error",
                }
            )


    # Receive message from room group (sent by another consumer via channel layer)
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send the message back to the WebSocket (to the client browser)
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))