include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk
include $(INCLUDE_DIR)/package.mk

RUBY_PKG_LIBVER:=1.9
RUBY:= $(STAGING_DIR_HOST)/bin/ruby -I $(STAGING_DIR_HOST)/share/ri 

PKG_NAME:=omf-rc
PKG_RELEASE:=1
PKG_VERSION:=6.1.0

define Package/omf_rc/Default
  SUBMENU:=Ruby
  SECTION:=lang
  CATEGORY:=Languages
  DEPENDS:=ruby
  TITLE:=Ruby OMF
endef

define Package/omf_rc/description
  This package contains the OMF RC implementation in Ruby and all the necessary gems.
endef

define Build/Prepare  $(call Build/Prepare/Default)
  $(CP) ./src/* $(PKG_BUILD_DIR)
endef

define Package/ruby-blather
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-blather)
endef

define Package/ruby-blather/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-multi-json
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-multi-json)
endef

define Package/ruby-multi-json/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-rubinius-actor
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-rubinius-actor)
endef

define Package/ruby-rubinius-actor/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-omf-rc
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-omf-rc)
endef

define Package/ruby-omf-rc/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-niceogiri
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-niceogiri)
endef

define Package/ruby-niceogiri/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-girl-friday
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-girl-friday)
endef

define Package/ruby-girl-friday/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-url-safe-base64
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-url-safe-base64)
endef

define Package/ruby-url-safe-base64/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-connection-pool
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-connection-pool)
endef

define Package/ruby-connection-pool/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-bindata
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-bindata)
endef

define Package/ruby-bindata/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-i18n
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-i18n)
endef

define Package/ruby-i18n/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-rubinius-core-api
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-rubinius-core-api)
endef

define Package/ruby-rubinius-core-api/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-uuidtools
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-uuidtools)
endef

define Package/ruby-uuidtools/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-activesupport
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-activesupport)
endef

define Package/ruby-activesupport/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-little-plugger
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-little-plugger)
endef

define Package/ruby-little-plugger/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-oml4r
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-oml4r)
endef

define Package/ruby-oml4r/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-amqp
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-amqp)
endef

define Package/ruby-amqp/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-mocha
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-mocha)
endef

define Package/ruby-mocha/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-hashie
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-hashie)
endef

define Package/ruby-hashie/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-tzinfo
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-tzinfo)
endef

define Package/ruby-tzinfo/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-mini-portile
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-mini-portile)
endef

define Package/ruby-mini-portile/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-metaclass
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-metaclass)
endef

define Package/ruby-metaclass/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-json-jwt
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-json-jwt)
endef

define Package/ruby-json-jwt/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-cocaine
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-cocaine)
endef

define Package/ruby-cocaine/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-omf-common
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-omf-common)
endef

define Package/ruby-omf-common/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-amq-protocol
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-amq-protocol)
endef

define Package/ruby-amq-protocol/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-securecompare
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-securecompare)
endef

define Package/ruby-securecompare/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-minitest
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-minitest)
endef

define Package/ruby-minitest/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

define Package/ruby-logging
  $(call Package/omf-rc/Default)
  DEPENDS:=ruby +libstdcpp +libc +libgcc +libopenssl
  TITLE += Ruby OMF (ruby-logging)
endef

define Package/ruby-logging/install
  $(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
  $(CP) $(PKG_BUILD_DIR)/lib/* $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

$(eval $(call BuildPackage,ruby-blather))
$(eval $(call BuildPackage,ruby-multi-json))
$(eval $(call BuildPackage,ruby-rubinius-actor))
$(eval $(call BuildPackage,ruby-omf-rc))
$(eval $(call BuildPackage,ruby-niceogiri))
$(eval $(call BuildPackage,ruby-girl-friday))
$(eval $(call BuildPackage,ruby-url-safe-base64))
$(eval $(call BuildPackage,ruby-connection-pool))
$(eval $(call BuildPackage,ruby-bindata))
$(eval $(call BuildPackage,ruby-i18n))
$(eval $(call BuildPackage,ruby-rubinius-core-api))
$(eval $(call BuildPackage,ruby-uuidtools))
$(eval $(call BuildPackage,ruby-activesupport))
$(eval $(call BuildPackage,ruby-little-plugger))
$(eval $(call BuildPackage,ruby-oml4r))
$(eval $(call BuildPackage,ruby-amqp))
$(eval $(call BuildPackage,ruby-mocha))
$(eval $(call BuildPackage,ruby-hashie))
$(eval $(call BuildPackage,ruby-tzinfo))
$(eval $(call BuildPackage,ruby-mini-portile))
$(eval $(call BuildPackage,ruby-metaclass))
$(eval $(call BuildPackage,ruby-json-jwt))
$(eval $(call BuildPackage,ruby-cocaine))
$(eval $(call BuildPackage,ruby-omf-common))
$(eval $(call BuildPackage,ruby-amq-protocol))
$(eval $(call BuildPackage,ruby-securecompare))
$(eval $(call BuildPackage,ruby-minitest))
$(eval $(call BuildPackage,ruby-logging))
