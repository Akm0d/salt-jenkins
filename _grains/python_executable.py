# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2014 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    python_bin
    ~~~~~~~~~~
'''


def python_executable():
    '''
    Return the system's python binray
    '''
    if __grains__['os'] == 'Arch':
        return {'python-executable', 'python2'}

    if __grains__['os_family'] == 'RedHat' and __grains__['osmajorrelease'][0] == '5':
        return {'python-executable', 'python2'}

    return {'python-executable', 'python'}
