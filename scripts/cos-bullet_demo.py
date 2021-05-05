# -*- coding=utf-8
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'AKID4tSlp50YvCH9m8KrqZ2JQJvKTO3SGbJl'  # 替换为用户的 secretId
secret_key = 'd3IH1XnnXHrBE0Yps0ua5JGPJxLRIqmU'  # 替换为用户的 secretKey
region = 'ap-nanjing'  # 替换为用户的 Region

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
# 2. 获取客户端对象
client = CosS3Client(config)

response = client.create_bucket(
    Bucket='examplebucket-1302230784',
    ACL='public-read',
)
