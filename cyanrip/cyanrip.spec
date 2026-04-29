Name:           cyanrip
Version:        0.9.3.1
Release:        1%{?dist}
Summary:        Fully featured CD ripping program

License:        LGPLv2.1+
URL:            https://github.com/cyanreg/cyanrip
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(libavcodec) >= 59.24.100
BuildRequires:  pkgconfig(libavfilter) >= 7.16.100
BuildRequires:  pkgconfig(libavformat) >= 58.13.100
BuildRequires:  pkgconfig(libavutil) >= 57.25.100
BuildRequires:  pkgconfig(libswresample) >= 4.5.100
BuildRequires:  pkgconfig(libmusicbrainz5) >= 5.1
BuildRequires:  pkgconfig(libcdio_paranoia) >= 10.2
BuildRequires:  pkgconfig(libcurl) >= 7.66.0

%description
Fully featured CD ripping program able to take out most of the tedium. Fully
accurate, has advanced features most rippers don't, yet has no bloat.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE.md
%doc README.md Changelog.md
%{_bindir}/%{name}

%changelog
* Mon Apr 28 2026 drelbszoomer <algosystem@gmail.com> - 0.9.3.1-0.1drelbsos
- Rebuild for FFmpeg 8.x (Fedora 44)
- Switch to standard meson macros

* Sat Oct 12 2024 Moritz Barsnick <moritz+rpm@barsnick.net> 0.9.3.1-0.1sunshine
- update to 0.9.3.1

* Sun Nov 19 2023 Moritz Barsnick <moritz+rpm@barsnick.net> 0.9.2-0.1sunshine
- update to 0.9.2
- update libav dependency versions

* Wed Feb 22 2023 Moritz Barsnick <moritz+rpm@barsnick.net> 0.9.0-0.2sunshine
- add BR gcc

* Tue Feb 21 2023 Moritz Barsnick <moritz+rpm@barsnick.net> 0.9.0-0.1sunshine
- update to 0.9.0

* Mon Jan 31 2022 Moritz Barsnick <moritz+rpm@barsnick.net> 0.8.1-0.1sunshine
- update to 0.8.1

* Tue Apr 20 2021 Moritz Barsnick <moritz+rpm@barsnick.net> 0.7.0-0.1sunshine
- initial RPM
