"""
Config functions
"""

import os


def get_port(varname: str = "PORT") -> int:
    """Gets port from env, default 9000"""

    port_env = os.getenv(varname)
    if port_env is None:
        return 9000
    return int(port_env)
