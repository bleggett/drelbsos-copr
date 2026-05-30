Name:           slurp
Version:        1.5.0
Release:        1%{?dist}
Summary:        Select a region in a Wayland compositor

License:        MIT
URL:            https://github.com/emersion/slurp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  wayland-devel
BuildRequires:  scdoc

%description
slurp allows the user to select a region or a window in a Wayland compositor
by clicking and dragging. It reads a list of pre-defined regions from stdin
and highlights them when the mouse hovers over them. Selected regions are
printed to stdout.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri May 30 2026 drelbszoomer <algosystem@gmail.com> - 1.5.0-1
- Initial package
