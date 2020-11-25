#!/usr/bin/env python3
import logging
import random

try:
    import settings
except ImportError:
    exit('DO cp settings.py.default settings.py and set token')

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

log = logging.getLogger("bot")


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler("bot.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%d-%m-%Y %H:%M"))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для vk.com
    Use python3.7
    """

    def __init__(self, group_id, token):
        """

        :param group_id: group id из группы vk
        :param token: секретный токен
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота"""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception("ошибка в обработке события")

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст.

        :param event: VkBotMessageEvent object
        :return: None
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug("отправляем сообщение назад")
            self.api.messages.send(
                message=event.object.text,
                random_id=random.randint(0, 2 ** 20),
                peer_id=event.object.peer_id,
            )
        else:
            log.info("мы пока не умеем обрабатывать событие такого типа %s", event.type)


if __name__ == "__main__":
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
