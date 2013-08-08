include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk
include $(INCLUDE_DIR)/package.mk

RUBY_PKG_LIBVER:=1.9
RUBY:= $(STAGING_DIR_HOST)/bin/ruby -I $(STAGING_DIR_HOST)/share/ri \

PKG_NAME:=omf-rc
PKG_RELEASE:=1
PKG_VERSION:=6.0.3

define Package/omf-rc/Default
  SUBMENU:=Ruby
  SECTION:=lang
  CATEGORY:=Languages
  DEPENDS:=ruby
  TITLE:=Ruby OMF
endef

define Package/omf-rc/description
  This package contains the OMF RC implementation in Ruby and all the necessary gems.
endef

define Package/omf-rc
  $(call Package/omf-rc/Default)
  TITLE += (RC)
  DEPENDS += omf-common
endef

define Package/omf-common
  $(call Package/omf-rc/Default)
  TITLE += (Common)
endef

# necessary ruby gems

define Package/ruby-eventmachine
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (eventmachine)
endef

# build process

define Build/Prepare
  $(call Build/Prepare/Default)
  $(CP) ./src/* $(PKG_BUILD_DIR)
endef

define Build/Configure/eventmachine
	(cd $(PKG_BUILD_DIR)/ext; \
		$(RUBY) extconf.rb; \
	);
endef

define Build/Compile/eventmachine
	$(MAKE_VARS) \
	$(MAKE) -C $(PKG_BUILD_DIR)/ext \
		$(MAKE_FLAGS) \
		$(1);
	$(CP) $(PKG_BUILD_DIR)/ext/*.so $(PKG_BUILD_DIR)/lib/
endef

define Build/Configure/fastfilereader
	(cd $(PKG_BUILD_DIR)/ext/fastfilereader; \
		$(RUBY) extconf.rb; \
	);
endef

define Build/Compile/fastfilereader
	$(MAKE_VARS) \
	$(MAKE) -C $(PKG_BUILD_DIR)/ext/fastfilereader \
		$(MAKE_FLAGS) \
		$(1);
	$(CP) $(PKG_BUILD_DIR)/ext/fastfilereader/*.so $(PKG_BUILD_DIR)/lib/
endef

define Build/Configure
	$(call Build/Configure/eventmachine)
	$(call Build/Configure/fastfilereader)
endef

define Build/Compile
	$(call Build/Compile/fastfilereader)
	$(call Build/Compile/eventmachine)
endef

define Package/ruby-eventmachine/install
	$(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/mips-linux
	$(CP) $(PKG_BUILD_DIR)/lib/eventmachine.rb $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/em $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/*.so $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/mips-linux
endef

$(eval $(call BuildPackage,ruby-eventmachine))
