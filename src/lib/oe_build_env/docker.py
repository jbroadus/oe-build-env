import os
import subprocess
from typing import Union

class Docker:
    docker_exec = 'podman'
    pwd = os.getcwd()

    def __init__(self, tag: str, build_user: str = 'builder'):
        self._tag = tag
        self._build_user = build_user

    def volume_args(self) -> list[str]:
        return ['-v', '{}:{}:rw,exec,nosuid,nodev'.format(self.pwd, self.pwd),
                '--tmpfs', '/tmp',
                '--tmpfs', '/home/{}:rw,exec,nosuid,nodev'.format(self._build_user)]

    def net_args(self) -> list[str]:
        return ['--cap-add=NET_ADMIN',
                '--device=/dev/net/tun',
                '--publish', '1234:1234']

    def run(self, cmd: Union[str, list[str]]):
        args = [self.docker_exec, 'run']
        args.extend(['-w', self.pwd])
        args.extend(self.volume_args())
        args.extend(self.net_args())
        args.extend(['-it', self._tag])
        args.extend(cmd if isinstance(cmd, list) else [cmd])
        print(args)
        subprocess.run(args)
