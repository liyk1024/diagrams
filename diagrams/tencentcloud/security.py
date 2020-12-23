# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _TencentCloud

class _Security(_TencentCloud):
    _type = "security"
    _icon_dir = "resources/tencentcloud/security"


class CloudFireWall(_Security):
    _icon = "cloud-fire-wall.png"
class CloudWP(_Security):
    _icon = "cloud-w-p.png"
class DataSecurityAudit(_Security):
    _icon = "data-security-audit.png"
class DataSecurityGateway(_Security):
    _icon = "data-security-gateway.png"
class WebApplicationFirewall(_Security):
    _icon = "web-application-firewall.png"

# Aliases

DSG = DataSecurityGateway
CWP = CloudWP
CFW = CloudFireWall
DSAudit = DataSecurityAudit
WAF = WebApplicationFirewall