from . import hooks
from .websocket.consumer import IdomWebsocket
from .websocket.paths import IDOM_WEBSOCKET_PATH


__version__ = "1.0.0"
__all__ = ["IDOM_WEBSOCKET_PATH", "IdomWebsocket", "hooks"]
