Name:           woof
Version:        15.3.0
Release:        1%{?dist}
Summary:        A continuation of the MBF source port for modern systems

License:        GPL-2.0-or-later
URL:            https://github.com/fabiangreffrath/woof
# Tracks upstream's default branch (master) rather than a tagged release.
Source0:        %{url}/archive/refs/heads/master.tar.gz#/%{name}-master.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  SDL3-devel >= 3.4.0
BuildRequires:  openal-soft-devel >= 1.22.0
BuildRequires:  alsa-lib-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  libxmp-devel
BuildRequires:  yyjson-devel
BuildRequires:  libebur128-devel
BuildRequires:  libspng-devel

%description
MBF stands for "Marine's Best Friend" and is widely regarded as the successor of the Boom source port by TeamTNT. It serves as the code base for popular Doom source ports such as PrBoom+/DSDA-Doom or The Eternity Engine. As the original engine was limited to run only under MS-DOS, it has been ported to Windows by Team Eternity under the name WinMBF in 2004. Woof! is developed based on the WinMBF code with the aim to make MBF more widely available and convenient to use on modern systems.

To achieve this goal, this source port is less strict regarding its faithfulness to the original MBF. It is focused on quality-of-life enhancements, bug fixes and compatibility improvements. However, all changes have been introduced in good faith that they are in line with the original author's intentions and even for the trained eye, this source port should still look very familiar to the original MBF.

In summary, this project's goal is to fast-forward MBF.EXE from DOS to 21st century and remove all the stumbling blocks on the way. Furthermore, just as MBF was ahead of its time, this project dedicates itself to early adoption of new modding features such as DEHEXTRA+DSDHacked, UMAPINFO and MBF21.

%prep
%autosetup -n %{name}-master

%build
%cmake -DWITH_DISCORD_RPC=OFF
%cmake_build

%install
%cmake_install

%files
%{_bindir}/woof
%{_bindir}/woof-setup
%{_datadir}/woof/
%{_datadir}/doc/woof/
%{_datadir}/applications/io.github.fabiangreffrath.woof*.desktop
%{_datadir}/metainfo/io.github.fabiangreffrath.woof.metainfo.xml
%{_datadir}/icons/hicolor/128x128/apps/woof*.png
%{_datadir}/bash-completion/completions/woof
%{_mandir}/man6/woof.6*
%{_mandir}/man6/woof-setup.6*

%changelog
* Wed Jul 1 2026 drelbszoomer <algosystem@gmail.com> - 15.3.0-1

* Sun Jun 14 2026 drelbszoomer <algosystem@gmail.com> - 15.2.0-1
- Imported recipe from deudz/woof COPR
- Track upstream master; migrate to SDL3 and current optional dependencies
