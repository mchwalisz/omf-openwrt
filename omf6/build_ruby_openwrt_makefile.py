#!/bin/python

import os

path = os.path.join(os.getcwd(), "src/")
filename = "Makefile"
package = "omf_rc"
title = "Ruby OMF"
description = "This package contains the OMF RC implementation in Ruby and all the necessary gems."
version = "0.0"
gems = []
extgems = []
libgems = []

def build_gemname(input):
    return "ruby-" + input.rsplit("-", 1)[0].replace("_", "-")

for item in os.listdir(path):
	if os.path.isdir(os.path.join(path, item)):
		gems.append(item)
		if item.startswith(package):
			version = item.rsplit("-", 1)[1]

for gem in gems:
	for item in os.listdir(os.path.join(path, gem)):
		if os.path.isdir(os.path.join(path, gem, item)):
			if item == 'ext':
				extgems.append(gem)

for gem in gems:
    if gem not in extgems:
        libgems.append(gem)

f = open(filename, "wb")
f.write("include $(TOPDIR)/rules.mk\ninclude $(INCLUDE_DIR)/kernel.mk\ninclude $(INCLUDE_DIR)/package.mk\n\nRUBY_PKG_LIBVER:=1.9\nRUBY:= $(STAGING_DIR_HOST)/bin/ruby -I $(STAGING_DIR_HOST)/share/ri \n\n");
f.write("PKG_NAME:=%s\n" % package.replace("_","-"))
f.write("PKG_RELEASE:=1\n")
f.write("PKG_VERSION:=%s\n\n" % version)

f.write("define Package/%s/Default\n" % package)
f.write("  SUBMENU:=Ruby\n")
f.write("  SECTION:=lang\n")
f.write("  CATEGORY:=Languages\n")
f.write("  DEPENDS:=ruby\n")
f.write("  TITLE:=%s\n" % title)
f.write("endef\n\n")

f.write("define Package/%s/description\n" % package)
f.write("  %s\n" % description)
f.write("endef\n\n")

f.write("define Build/Prepare")
f.write("  $(call Build/Prepare/Default)\n")
f.write("  $(CP) ./src/* $(PKG_BUILD_DIR)\n")
f.write("endef\n\n")

for gem in libgems:
    gemname = build_gemname(gem)
    f.write("define Package/%s\n" % gemname)
    f.write("  $(call Package/omf-rc/Default)\n")
    f.write("  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl\n")
    f.write("  TITLE += %s (%s)\n" % (title, gemname))
    f.write("endef\n\n")

    f.write("define Package/%s/install\n" % gemname)
    f.write("  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/\n")
    f.write("  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/\n")
    f.write("endef\n\n")

for gem in libgems:
    gemname = build_gemname(gem)
    f.write("$(eval $(call BuildPackage,%s))\n" % gemname)

f.close()
