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

define Package/ruby-activesupport
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (activesupport)
endef

define Package/ruby-atomic
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (atomic)
endef

define Package/ruby-blather
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (blather)
endef

define Package/ruby-cocaine
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (cocaine)
endef

define Package/ruby-connection_pool
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (connection_pool)
endef

define Package/ruby-eventmachine
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (eventmachine)
endef

define Package/ruby-girl_friday
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (girl_friday)
endef

define Package/ruby-hashie
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (hashie)
endef

define Package/ruby-i18n
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (i18n)
endef

define Package/ruby-little_plugger
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (little_plugger)
endef

define Package/ruby-logging
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (logging)
endef

define Package/ruby-metaclass
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (metaclass)
endef

define Package/ruby-mini_portile
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (mini_portile)
endef

define Package/ruby-minitest
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (minitest)
endef

define Package/ruby-mocha
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (mocha)
endef

define Package/ruby-multi_json
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (multi_json)
endef

define Package/ruby-niceogiri
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (niceogiri)
endef

define Package/ruby-nokogiri
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (nokogiri)
endef

define Package/ruby-oml4r
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (oml4r)
endef

define Package/ruby-rubinius_actor
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (rubinius_actor)
endef

define Package/ruby-rubinius_core_api
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (rubinius_core_api)
endef

define Package/ruby-thread_safe
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (thread_safe)
endef

define Package/ruby-tzinfo
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE:=Ruby Gem (tzinfo)
endef

# prepare

define Build/Prepare
  $(call Build/Prepare/Default)
  $(CP) ./src/* $(PKG_BUILD_DIR)
endef

# configure

define Build/Configure/ruby-atomic
  (cd $(PKG_BUILD_DIR)/atomic-1.1.10/ext; $(RUBY) extconf.rb; );
endef

define Build/Configure/ruby-eventmachine
  (cd $(PKG_BUILD_DIR)/eventmachine-1.0.3/ext; $(RUBY) extconf.rb; );
endef

define Build/Configure/ruby-nokogiri
  (cd $(PKG_BUILD_DIR)/nokogiri-1.6.0/ext/nokogiri; $(RUBY) extconf.rb; );
endef

define Build/Configure/ruby-thread_safe
  # (cd $(PKG_BUILD_DIR)/thread_safe-0.1.0/ext; $(RUBY) extconf.rb; );
endef

# compile

define Build/Compile/ruby-atomic
  $(MAKE_VARS) $(MAKE) -C $(PKG_BUILD_DIR)/ext $(MAKE_FLAGS) $(1);
  $(CP) $(PKG_BUILD_DIR)/ext/*.so $(PKG_BUILD_DIR)/lib/
endef

define Build/Compile/ruby-eventmachine
  $(MAKE_VARS) $(MAKE) -C $(PKG_BUILD_DIR)/ext $(MAKE_FLAGS) $(1);
  $(CP) $(PKG_BUILD_DIR)/ext/*.so $(PKG_BUILD_DIR)/lib/
  $(MAKE_VARS) $(MAKE) -C $(PKG_BUILD_DIR)/ext/fastfilereader $(MAKE_FLAGS) $(1);
  $(CP) $(PKG_BUILD_DIR)/ext/fastfilereader/*.so $(PKG_BUILD_DIR)/lib/
endef

define Build/Compile/ruby-nokogiri
  $(MAKE_VARS) $(MAKE) -C $(PKG_BUILD_DIR)/ext/nokogiri $(MAKE_FLAGS) $(1);
  $(CP) $(PKG_BUILD_DIR)/ext/nokogiri/*.so $(PKG_BUILD_DIR)/lib/
endef

define Build/Compile/ruby-thread_safe
endef

# install

define Package/ruby-eventmachine/install
	$(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/mips-linux
	$(CP) $(PKG_BUILD_DIR)/lib/eventmachine.rb $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/em $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/*.so $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/mips-linux
endef

$(eval $(call BuildPackage,omf-rc))
$(eval $(call BuildPackage,ruby-atomic))
$(eval $(call BuildPackage,ruby-eventmachine))
$(eval $(call BuildPackage,ruby-nokogiri))
$(eval $(call BuildPackage,ruby-thread_safe))
