LANGUAGE_CODE = 'zh-hans'
# 自己应用ID
TENCENT_SMS_APP_ID = 1400496023
# 自己应用Key
TENCENT_SMS_APP_KEY = "d38902f2574dc825933cec4faf66cf1e"
# 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
TENCENT_SMS_SIGN = "django爬虫"

TENCENT_SMS_TEMPLATE = {
    'register': 894421,
    'login': 894419
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1",  # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": ""
        }
    }
}
