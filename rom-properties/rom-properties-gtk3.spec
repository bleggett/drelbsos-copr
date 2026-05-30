%global upstream_name rom-properties

Name:           rom-properties-gtk3
Version:        2.3
Release:        1%{?dist}
Summary:        GTK3/4 file browser plugin for managing video game ROM and disc images
License:        GPLv2
URL:            https://github.com/GerbilSoft/%{upstream_name}

Source:         https://github.com/GerbilSoft/%{upstream_name}/archive/refs/tags/v%{version}.tar.gz
Patch0:         no_tests.patch
Patch1:         no_zlibng.patch
Patch2:         defaults.patch

Requires:       curl
Requires:       zlib
Requires:       libpng
Requires:       libjpeg-turbo
Requires:       nettle
Requires:       tinyxml2
Requires:       libseccomp
Recommends:     lz4
Recommends:     lzo

BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  pkgconf
BuildRequires:  gettext-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libcurl-devel
BuildRequires:  nettle-devel
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  libzstd-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  gsound-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  nautilus-devel
BuildRequires:  gtk3-devel
BuildRequires:  cairo-devel
BuildRequires:  Thunar-devel

%global debug_package %{nil}

%description
GTK3/4 shell extension for Nautilus, Caja, Nemo, and Thunar that adds
property pages and thumbnailing for video game ROM and disc images.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%cmake \
    -DBUILD_KF6=OFF \
    -DBUILD_KF5=OFF \
    -DBUILD_KDE4=OFF \
    -DBUILD_XFCE=OFF \
    -DBUILD_GTK3=ON \
    -DBUILD_GTK4=ON
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_sysconfdir}/apparmor.d
rm -rf %{buildroot}%{_prefix}/lib/debug

%files
%license %{_defaultdocdir}/%{upstream_name}/LICENSE
%doc %{_defaultdocdir}/%{upstream_name}/NETWORK.md
%doc %{_defaultdocdir}/%{upstream_name}/COMPILING.md
%doc %{_defaultdocdir}/%{upstream_name}/README.md
%doc %{_defaultdocdir}/%{upstream_name}/NEWS.md
%doc %{_defaultdocdir}/%{upstream_name}/keys.conf.example
%doc %{_defaultdocdir}/%{upstream_name}/rom-properties.conf.example
%{_libdir}/libromdata.*
%{_bindir}/rpcli
%{_bindir}/rp-stub
%{_bindir}/rp-config
%{_libexecdir}/rp-download
%{_libexecdir}/rp-thumbnail
%{_datadir}/%{upstream_name}/amiibo-data.bin
%{_datadir}/applications/com.gerbilsoft.rom-properties.rp-config.desktop
%{_datadir}/metainfo/com.gerbilsoft.rom-properties.metainfo.xml
%{_datadir}/mime/packages/rom-properties.xml
%{_datarootdir}/locale/*/LC_MESSAGES/rom-properties.mo
%{_datadir}/thumbnailers/rom-properties.thumbnailer
%{_datadir}/thumbnailers/com.gerbilsoft.rom-properties.SpecializedThumbnailer1.service
%{_datadir}/dbus-1/services/com.gerbilsoft.rom-properties.SpecializedThumbnailer1.service
%{_bindir}/rp-thumbnailer-dbus
%{_libdir}/nautilus/extensions-3.0/rom-properties-gtk3.so
%{_libdir}/nautilus/extensions-4/rom-properties-gtk4.so
%{_libdir}/caja/extensions-2.0/rom-properties-gtk3.so
%{_libdir}/nemo/extensions-3.0/rom-properties-gtk3.so
%{_libdir}/thunarx-3/rom-properties-gtk3.so

%changelog
* Sat May 30 2026 drelbszoomer <algosystem@gmail.com> - 2.3-1
- Initial package, GTK3/4 only build based on bazzite-org/rom-properties COPR
