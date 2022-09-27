# import os
#
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oshop.settings')
# app = Celery('oshop')
#
# app.conf.beat_schedule = {
#     "Notify_every_times": {
#         "task": 'api.v1.tasks.ad.ads_notifications',
#         "schedule": crontab(minute='0', hour='9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22')
#     },
#     "Send_unsent_ads_for_moderation": {
#         "task": 'api.v1.tasks.ad.unsent_ads_to_send_for_moderation',
#         "schedule": crontab(minute='*/10')
#     }
# }
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
