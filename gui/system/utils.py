# Copyright 2014 iXsystems, Inc.
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#####################################################################
import json
import logging
import os

from django.utils.translation import ugettext as _
from lockfile import LockFile

from freenasUI.common.pipesubr import pipeopen

log = logging.getLogger('system.utils')


class BootEnv(object):

    def __init__(
            self, id=None, active=None, on_reboot=None, mountpoint=None, space=None, created=None, **kwargs
    ):
        self._id = id
        self.active = active
        self.on_reboot = on_reboot
        self.created = created
        self.mountpoint = mountpoint
        self.name = id
        self.space = space

    @property
    def id(self):
        return self._id


def task_running(request):
    from freenasUI.middleware.connector import connection as dispatcher
    tid = request.session.get('update', {}).get('task')
    if tid is None:
        return False, None
    task = dispatcher.call_sync('task.status', int(tid))
    if task is None:
        return False, None
    if task['state'] in ('FINISHED', 'FAILED'):
        return False, task
    return True, task


def debug_get_settings():
    from freenasUI.middleware.notifier import notifier
    direc = "/var/tmp/ixdiagnose"
    mntpt = '/var/tmp'
    dump = os.path.join(direc, 'ixdiagnose.tgz')

    return (mntpt, direc, dump)


def debug_run(direc):
    # Be extra safe in case we have left over from previous run
    if os.path.exists(direc):
        opts = ["/bin/rm", "-r", "-f", direc]
        p1 = pipeopen(' '.join(opts), allowfork=True)
        p1.wait()

    opts = ["/usr/local/bin/ixdiagnose", "-d", direc, "-s", "-F"]
    p1 = pipeopen(' '.join(opts), allowfork=True)
    p1.communicate()
