#!/usr/bin/env python
"""


Usage:
  russian-tor-exit-node [<tor>] [--color] [--geoipfile=</path/to/file>]
  russian-tor-exit-node -h | --help
  russion-tor-exit-node --version


"""

import sys
from contextlib import closing
from lxml.cssselect import CSSSelector
import colorama  # $ pip install colorama
import docopt  # $ pip install docopt
import socks  # $ pip install PySocks
import stem.process  # $ pip install stem
from sockshandler import SocksiPyHandler  # see pysocks repository
from stem.util import term
import random
import string
import socket
import os, random
from bs4 import BeautifulSoup

try:
    import urllib2
except ImportError: # Python 3
    import urllib.request as urllib2

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class randomLink():
    args = docopt.docopt(__doc__, version='0.2')
    colorama.init(strip=not (sys.stdout.isatty() or args['--color']))

    tor_cmd = args['<tor>'] or 'tor'
    socks_port = 7000
    config = dict(SocksPort=str(socks_port), ExitNodes='{ru}')
    if args['--geoipfile']:
        config.update(GeoIPFile=args['--geoipfile'], GeoIPv6File=args['--geoipfile']+'6')


    def query(url, opener=urllib2.build_opener(
            SocksiPyHandler(socks.PROXY_TYPE_SOCKS5, "localhost", socks_port))):
        try:
            with closing(opener.open(url)) as r:


                return r.read().decode('ascii')
        except EnvironmentError as e:

            return "Unable to reach %s: %s" % (url, e)

    # Start an instance of Tor configured to only exit through Russia. This prints
    # Tor's bootstrap information as it starts. Note that this likely will not
    # work if you have another Tor instance running.
    def print_bootstrap_lines(line):
      if "Bootstrapped " in line:
        print(term.format(line, term.Color.BLUE))
      else:
        print(line)

    print(term.format("Starting Tor:\n", term.Attr.BOLD))
    tor_process = stem.process.launch_tor_with_config(
        tor_cmd=tor_cmd,
        config=config,
        init_msg_handler=print_bootstrap_lines,
    )
    while True:
        try:
            x = str("http://" + id_generator() + ".onion/")
            #TESTCONNECTION
            # x = str('HTTP://PLATZGN27WKRKF4T.ONION/')
            #
            website = (term.format(query(x), term.Color.BLUE))
            soup = BeautifulSoup(website, "html.parser")
            ##TODO GRAB SPECIFIC PARTS OF A WEBSITE
            #print soup.prettify()[0:20000]
            try:
                tit = soup.title
                if tit == None:
                    pass

                elif soup.title != None:
                    print(term.format("\nTryingrandom website:  \n" + x))
                    print soup.prettify()[0:20000]
                    for link in soup.find_all('a'):
                        print(link.get('href'))
            except Exception as e:
                print str(e)


        finally:
            if tor_process.poll() is None: # still running
                #tor_process.terminate()  # stops tor
                #tor_process.wait()
                pass