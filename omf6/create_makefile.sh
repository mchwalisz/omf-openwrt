#!/bin/bash

rm -Rf src
ruby gem-fetch-dependencies.rb fetch --dependencies omf_rc
gem unpack --target=src *.gem
rm -Rf *.gem

python build_ruby_openwrt_makefile.py
