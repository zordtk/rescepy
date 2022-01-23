# Author: Joseph Wiseman <joswiseman@cock.li>
# URL: https://github.com/dryes/rescepy/
#
# This file is part of rescepy.
#

import os,subprocess

class CFV(object):
    def __init__(self, binary=None):
        if binary == None:
            if os.name == 'posix':
                self.binary = 'cksfv'
            elif os.name == 'nt':
                self.binary = 'cfv'
        else:
            self.binary = binary

    def verify(self, opts=''):
        sp = subprocess.Popen('%s %s' % (self.binary, opts), shell=True, stdin=subprocess.PIPE)
        sp.communicate()

        return True if sp.returncode == 0 else False
