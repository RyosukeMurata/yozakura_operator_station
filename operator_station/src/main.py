#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (C) 2015  Kyoto University Mechatronics Laboratory
# Released under the GNU General Public License, version 3


import logging
import rospy

from common.networking import get_ip_address
from src.operator_station.src.bk.server import Server, Handler


def main():
    rospy.init_node('operator_station', anonymous=True)

    try:
        ip_address = get_ip_address("eth0")
    except OSError:
        # ip_address = get_ip_address("enp2s0")
        ip_address = get_ip_address("wlan0")
    server = Server((ip_address, 9999), Handler)

    logging.debug("Initializing controllers")

    try:
        logging.debug("Starting server")
        server.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        raise
    finally:
        logging.info("Shutting down...")
    logging.info("All done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
