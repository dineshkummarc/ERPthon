"""    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012  Cresto Miseroglio Alessandro <alex179ohm@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program."""
from werkzeug.wrappers import (BaseResponse, BaseRequest)


class Response(BaseResponse):
    def __init__(self, descriptors=False, www_authentication=False, etag=False,
                 stream=False):
        if descriptors:
            from werkzeug.wrappers import CommonResponseDescriptorsMixin as \
                common
            self.age = common.age
            self.mimetype = common.mimetype
            self.mimetype_params = common.mimetype_params
            self.location = common.location
            self.content_type = common.content_type
            self.content_length = common.content_length
            self.content_location = common.content_location
            self.content_encoding = common.content_encoding
            self.content_md5 = common.content_md5
            self.date = common.date
            self.expires = common.expires
            self.last_modified = common.last_modified
            self.retry_after = common.retry_after
            self.vary = common.vary
            self.content_language = common.content_language
            self.allow = common.allow
        if www_authentication:
            from werkzeug.wrappers import WWWAuthenticateMixin as \
                authenticate
            self.www_authenticate = authenticate.www_authenticate
        if etag:
            from werkzeug.wrappers import ETagResponseMixin as resp_etag
            self.cache_control = resp_etag.cache._control
            self.make_conditional = resp_etag.make_conditional
            self.add_etag = resp_etag.add_etag
            self.set_etag = resp_etag.set_etag
            self.get_etag = resp_etag.get_etag
            self.freeze = resp_etag.freeze
            self.content_range = resp_etag.content_range
        if stream:
            from werkzeug.wrappers import ResponseStreamMixin as resp_stream
            self.stream = resp_stream.stream


class Request(BaseRequest):
    pass
