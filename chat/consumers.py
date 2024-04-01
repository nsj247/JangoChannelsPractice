from channels.generic.websocket import JsonWebsocketConsumer

class ChatConsumer(JsonWebsocketConsumer):
    SQUARE_GROUP_NAME = "square"
    groups = [SQUARE_GROUP_NAME]

    def receive_json(self, content, **kwargs):
        _type = content["type"]

        if _type == "chat.message":
            message = content["message"]
            async_to_sync(self.channel_layer.group_send)(
                SQUARE_GROUP_NAME,
                {
                    "type": "chat.message",
                    "message": message
                }
            )
        else:
            print(f"Invaild message type : $(_type)")

    def chat_message(self, message_dict):
        self.send_json({
            "type": "chat.message",
            "message": message_dict["message"]            
        })