

from hashlib import md5


def generate_etag(data):
    """Generate a Etag for some data,
    inspired from werkzeug

    :param data: Some data
    """

    return md5(data).hexdigest()
