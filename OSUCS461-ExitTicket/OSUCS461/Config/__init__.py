# this file is a template config file, the real configs are in __init__.py
from dataclasses import dataclass
import os

env = "prod"
API_VERSION = 'v1'
SERVER = 'osucapstone.com'
FRONTEND = 'osucapstone.com'

@dataclass(repr=False)
class BaseConfig:
    reload: bool = True
    use_colors: bool = True
    port: int = os.getenv("PORT", "80")

@dataclass
class LocalConfig(BaseConfig):
    host: str = os.getenv("HOST", "0.0.0.0")

@dataclass
class StagingConfig(BaseConfig):
    host: str = "staging.osucapstone.com"

@dataclass
class ProdConfig(BaseConfig):
    host: str = os.getenv("HOST", "0.0.0.0")

configs = {
    "local" : LocalConfig(),
    "sandbox" : StagingConfig(),
    "prod" : ProdConfig()
}

FASTAPI_CONFIG = configs[env]

MySQL = {
	'local' : {
		'host' : '127.0.0.1',
		'port' : 3306,
		"user": "root",
        "passwd": "",
 		'db' : 'osucs461'
	},
	'sandbox' : {
		'host' : 'xxxx',
		'port' : 3306,
		"user": "root",
        "passwd": "",
 		'db' : 'osucs461'
	},
	'prod' : {
		'host' : '10.44.192.2',
		'port' : 3306,
		"user": "root",
        "passwd": "",
 		'db' : 'osucs461'
	}
}[env]
