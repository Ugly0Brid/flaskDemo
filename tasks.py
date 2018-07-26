from app import celery


@celery.task
def send_msg(a, b):
    return a + b
