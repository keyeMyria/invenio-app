# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Celery application for Invenio flavours."""

from __future__ import absolute_import, print_function

from flask_celeryext import create_celery_app

from .factory import create_ui

celery = create_celery_app(create_ui(
    SENTRY_TRANSPORT='raven.transport.http.HTTPTransport'
))
"""Celery application for Invenio.

Overrides SENTRY_TRANSPORT wih synchronous HTTP transport since Celery does not
deal nicely with the default threaded transport.
"""

# Trigger an app log message upon import. This makes Sentry logging
# work with `get_task_logger(__name__)`.
celery.flask_app.logger.info('Created Celery app')
