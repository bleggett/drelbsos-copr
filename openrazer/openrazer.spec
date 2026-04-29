Name: openrazer-meta
Version: 3.12.2
Release: 1%{?dist}
Summary: Open source driver and user-space daemon for managing Razer devices

License: GPL-2.0
URL: https://github.com/openrazer/openrazer
Source0: https://github.com/openrazer/openrazer/releases/download/v%{version}/openrazer-%{version}.tar.xz

BuildArch: noarch
BuildRequires: make
BuildRequires: systemd-rpm-macros

Requires: openrazer-daemon
Requires: python3-openrazer

%description
Meta package for installing all required openrazer packages.
Note: kernel module is expected to be provided by kmod-openrazer from ublue-os/akmods.


%package -n openrazer-daemon
Summary: OpenRazer Service package
Obsoletes: razer-daemon
Provides: razer-daemon
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-setproctitle
Requires: python3-pyudev
Requires: python3-daemonize
Requires: xautomation

%description -n openrazer-daemon
Userspace daemon that abstracts access to the kernel driver. Provides a DBus service for applications to use.


%package -n python3-openrazer
Summary: OpenRazer Python library
Obsoletes: python3-razer
Provides: python3-razer
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: openrazer-daemon
Requires: python3
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-numpy

%description -n python3-openrazer
Python library for accessing the daemon from Python.


%prep
%autosetup -n openrazer-%{version}

%build
# noop

%install
make DESTDIR=%{buildroot} udev_install daemon_install python_library_install

%files
# meta package is empty

%files -n openrazer-daemon
%{_udevrulesdir}/99-razer.rules
%{_udevdir}/razer_mount
%{_bindir}/openrazer-daemon
%{python3_sitelib}/openrazer_daemon/
%{python3_sitelib}/openrazer_daemon-*.egg-info/
%{_datadir}/openrazer/
%{_datadir}/dbus-1/services/org.razer.service
%{_prefix}/lib/systemd/user/openrazer-daemon.service
%{_mandir}/man5/razer.conf.5*
%{_mandir}/man8/openrazer-daemon.8*

%files -n python3-openrazer
%{python3_sitelib}/openrazer/
%{python3_sitelib}/openrazer-*.egg-info/

%changelog
* Tue Apr 28 2026 drelbszoomer <algosystem@gmail.com> - 3.12.2-1
- Rebuild for Fedora 44
- Drop DKMS subpackage; kernel module provided by kmod-openrazer from ublue-os/akmods
- Remove openrazer-kernel-modules-dkms dependency from openrazer-daemon
