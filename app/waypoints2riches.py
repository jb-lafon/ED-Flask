# ==========
# File : waypoints2riches.py
# Author : Jb
# First created on : 2019-01-07
# Description: Main functions for W2R feature
# ==========

from .util.misc import urlify, http_request, req_value
from .alchemydb.systems_db import FindSystem


def api_call(sysName, minRadius, radius):
    result = {'data': '', 'length': ''}
    api_url = "https://www.edsm.net/api-v1/sphere-systems?systemName=" + urlify(sysName) + "&minRadius=" + str(
        minRadius) + "&radius=" + str(radius) + "&showId=1&showCoordinates=1"
    api_datas = http_request(api_url).json()
    result['data'] = api_datas
    result['length'] = int(len(api_datas))
    return result


# def coord_dif(coords_a, coords_b):
    # if coords_a[0] - coords_b[0] < 0:
        # return

def w2r(sys_a, sys_b='', jump_range='', value_limit=''):
    sys_a = FindSystem.by_name(sys_a)
    sys_b = FindSystem.by_name(sys_b)

    return 'done'
