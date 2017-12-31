from typing import List, Dict  # NOQA

from n0core.processor import Processor
from n0core.processor import IncompatibleMessage
from n0core.message import Message
from n0core.message.notification import Notification
from n0core.target import Target  # NOQA
from n0core.gateway import Gateway  # NOQA


class Agent(Processor):
    """
    Example:
        >>> agent = Agent(notification)
        >>> agent.add_target("resource/network/flat", flat_network_target)
    """

    def __init__(self,
                 notification,  # type: Gateway
                 targets={}      # type: Dict[str, Target]
                 ):
        # type: (...) -> None
        self.__notification = notification
        self.__targets = targets

    def add_target(self, type, target):
        # type: (str, Target) -> None
        self.__targets[type] = target

    def proccess(self, message):
        # type: (Notification) -> None
        if message.type is not Message.TYPES.NOTIFICATION:
            raise IncompatibleMessage
        if message.model.type not in self.__targets.keys():
            raise IncompatibleMessage
        if not message.is_succeeded:
            raise IncompatibleMessage

        model, is_succeeded, description = self.__targets[message.model.type].apply(message.model)
        notification = Notification(spec_id=message.spec_id,
                                    model=model,
                                    event=Notification.EVENTS.APPLIED,
                                    is_succeeded=is_succeeded,
                                    description=description)

        self.__notification.send(notification)