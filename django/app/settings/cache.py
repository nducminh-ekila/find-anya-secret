import os


REDIS_URL = os.getenv("REDIS_URL")
master_redis = REDIS_URL.split(',')[0]  if REDIS_URL else ''

if master_redis:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': REDIS_URL.split(','),
            'OPTIONS': {
                'DB': 0,
                'MASTER_CACHE': master_redis,
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
