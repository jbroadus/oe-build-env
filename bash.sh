#!/bin/sh
set -x

BUILD_USER=builder

# SSH key directory
KEYS=ssh
if [ -e "$(realpath $KEYS)" ]; then
   SSH_VOL="-v $(realpath $KEYS):/home/$BUILD_USER/.ssh/:Z"
fi
   
VOL_ARGS="\
-v $PWD:$PWD:rw,exec,nosuid,nodev $SSH_VOL \
--tmpfs /tmp \
--tmpfs /home/$BUILD_USER:rw,exec,nosuid,nodev \
-w $PWD"
#DEBUG_ARGS="--log-level=debug"
NET_ARGS="--cap-add=NET_ADMIN --device=/dev/net/tun"
#SEC_ARGS="--security-opt label=type:builder-policy.process"
TAG=oe-builder

podman run $VOL_ARGS $DEBUG_ARGS $NET_ARGS $SEC_ARGS -u $BUILD_USER -it $TAG /bin/bash
