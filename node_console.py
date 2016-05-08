# _*_ coding:utf-8 _*_

import sys
import signal
import urwid
from common import ConfigTab, TabNetwork
from node_console import TabHostedEngine

def handler(signum, frame):
    sys.exit()

signal.signal(signal.SIGINT, handler)

palette = [
    ('buttn','black','dark cyan'),
    ('buttnf','white','dark blue','bold'),
]
loop = urwid.MainLoop(None, palette, pop_ups=True)
config_tab_list = [
    TabNetwork(loop),
    TabHostedEngine(loop),
]
loop.widget = ConfigTab(config_tab_list)

if __name__ == '__main__':
   loop.run()