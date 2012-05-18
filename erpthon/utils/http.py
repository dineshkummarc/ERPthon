

def quote_etag(etag, weak=False):
    """Quote etag.

    :param etag: etag to quote
    :param weak: boolean, `True` to set it "weak".
    inspired by werkzeug.
    """

    if '"' in etag:
        raise ValueError("Invalid Etag or Etag is already quoted")
    etag = '"%s"' % etag
    if weak:
        etag = 'w' + etag
    return etag
