# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _TencentCloud

class _Application(_TencentCloud):
    _type = "application"
    _icon_dir = "resources/tencentcloud/application"


class CloudMessageQueue(_Application):
    _icon = "cloud-message-queue.png"
class LoadMaster(_Application):
    _icon = "load-master.png"
class LogService(_Application):
    _icon = "log-service.png"

# Aliases

CLS = LogService
CMQ = CloudMessageQueue
LM = LoadMaster