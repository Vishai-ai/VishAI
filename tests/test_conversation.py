from app.conversation.conversation_manager import ConversationManager

chat = ConversationManager()

chat.add_user_message("Hello")

chat.add_assistant_message("Hi!")

chat.add_user_message("My name is Vishal")

print(chat.get_messages())