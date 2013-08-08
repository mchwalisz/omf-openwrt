include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk
include $(INCLUDE_DIR)/package.mk

RUBY_PKG_LIBVER:=1.9

PKG_NAME:=ruby-activesupport
PKG_RELEASE:=1
PKG_VERSION:=4.0.0

define Package/ruby-activesupport
  SUBMENU:=Ruby
  SECTION:=lang
  CATEGORY:=Languages
  DEPENDS:=ruby
  TITLE:=Ruby activesupport gem
endef

define Package/ruby-activesupport/description
 This package contains the ruby activesupport gem.
endef

define Build/Prepare
	$(call Build/Prepare/Default)
	$(CP) ./src/* $(PKG_BUILD_DIR)/
endef

define Package/ruby-activesupport/install
	$(INSTALL_DIR) $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/active_support.rb $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
	$(CP) $(PKG_BUILD_DIR)/lib/active_support $(1)/usr/lib/ruby/$(RUBY_PKG_LIBVER)/
endef

$(eval $(call BuildPackage,ruby-activesupport))
