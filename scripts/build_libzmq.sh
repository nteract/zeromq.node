#!/bin/sh
set -e

if [ "$1" != "" ]; then
  ZMQ=$1
else
  echo "No ZMQ version given"
  exit 1
fi

export ZMQ_PREFIX="$(dirname $0)/../zmq"
export ZMQ_SRC_DIR=zeromq-$ZMQ
cd $ZMQ_PREFIX

export CFLAGS=-fPIC
export CXXFLAGS=-fPIC
export PKG_CONFIG_PATH=$ZMQ_PREFIX/lib/pkgconfig

test -d $ZMQ_SRC_DIR || tar xzf zeromq-$ZMQ.tar.gz
cd $ZMQ_SRC_DIR

test -f configure || ./autogen.sh
./configure --prefix=$ZMQ_PREFIX --disable-pedantic --enable-static --disable-shared
make -j 2
make install

cd $ZMQ_PREFIX
rm -rf $ZMQ_SRC_DIR
rm -f zeromq-$ZMQ.tar.gz
