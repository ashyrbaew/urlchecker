# urlchecker
Simple app to check url statuses

[comment]: <> (  celery:)

[comment]: <> (    build:)

[comment]: <> (      context: .)

[comment]: <> (      dockerfile: Dockerfile-alternate)

[comment]: <> (    command: celery -A oshop worker --beat -l INFO)

[comment]: <> (    volumes:)

[comment]: <> (      - .:/source/)

[comment]: <> (      - static_vol:/source/static)

[comment]: <> (    environment:)

[comment]: <> (      - DEBUG=True)

[comment]: <> (      - PYTHONUNBUFFERED=1)

[comment]: <> (      - DB_URL=172.27.129.177:1521/sd)

[comment]: <> (      - DB_USER=ADS_BOARD_STAGING)

[comment]: <> (      - DB_PASS=AbS2!6Dv)

[comment]: <> (      - LD_LIBRARY_PATH=/oracle_cli)

[comment]: <> (      - MINIO_HOST=devminio.o.kg)

[comment]: <> (      - MINIO_HOST_PROTOCOL=https://)

[comment]: <> (      - MINIO_BUCKET=ads)

[comment]: <> (      - MINIO_BUCKET_DOCS=ads-docs)

[comment]: <> (      - MINIO_BUCKET_MINIFY=ads-minify)

[comment]: <> (      - MINIO_BUCKET_ICONS=icons)

[comment]: <> (      - MINIO_BUCKET_AVATAR=ads-avatar)

[comment]: <> (      - MINIO_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE)

[comment]: <> (      - MINIO_SECRET_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY)

[comment]: <> (      - REDIS_HOST=redis)

[comment]: <> (      - REDIS_PORT=6379)

[comment]: <> (      - RABBIT_MQ_HOST=172.27.129.105)

[comment]: <> (      - RABBIT_MQ_PORT=5672)

[comment]: <> (      - RABBIT_MQ_USERNAME=admin)

[comment]: <> (      - RABBIT_MQ_PASSWORD=admin)

[comment]: <> (      - RABBIT_MQ_ERRORS_EXCHANGE=users_exchange)

[comment]: <> (      - ELASTICSEARCH_URL=172.27.128.240:9200)

[comment]: <> (      - MWALLET_USER_STATUS_URL=http://172.27.128.215:8080/user-profile/get-status/)

[comment]: <> (      - LK_LOGIN_BY_STRONG_PASS_URL=https://devproxy.o.kg/api/lk/wa/login_by_strong_pass)

[comment]: <> (      - MEDIA_SERVICE_URL=https://staging-api-media.o.kg/media-trusted/avatar-storage/)

[comment]: <> (      - TZ=Asia/Bishkek)

[comment]: <> (      - RABBIT_MQ_BOT_HOST=172.27.129.105)

[comment]: <> (      - RABBIT_MQ_BOT_PORT=5672)

[comment]: <> (      - RABBIT_MQ_BOT_USERNAME=admin)

[comment]: <> (      - RABBIT_MQ_BOT_PASSWORD=admin)

[comment]: <> (      - ALLOWED_IP=172.27.113, 172.27.128, 172.19.0, 192.168.0)

[comment]: <> (      - API_KEY=SKufX0aq9aCRaiS9NnOe)

[comment]: <> (      - UUID-LIFECYCLE=30)

[comment]: <> (    links:)

[comment]: <> (      - redis)