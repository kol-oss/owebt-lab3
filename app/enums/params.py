from enum import Enum, auto


class ContextParams(Enum):
    CHAT_ID = "chatId"
    MESSAGE_ID = "messageId"
    PROMPT_EXPECTED = "promptExpected"
