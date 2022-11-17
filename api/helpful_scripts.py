import hashlib
from models import task


def encript(str):
    return hashlib.sha256(str.encode()).hexdigest()


def serializable_task(task_):
    return {
        "id": task_.id,
        "title": task_.title,
        "text": task_.text,
        "start": task_.created,
        "finish": task_.closed
    }
