Name:           maestral
Version:        1.9.6
Release:        1%{?dist}
Summary:        Open-source Dropbox client for macOS and Linux
License:        MIT
URL:            https://github.com/samschott/maestral
Source0:        %{url}/archive/v%{version}/maestral-%{version}.tar.gz
Source1:        https://files.pythonhosted.org/packages/source/m/maestral-qt/maestral_qt-1.9.8.tar.gz

BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-rpm-macros

# Fedora-provided runtime deps
Requires:       python3-click >= 8.2.0
Requires:       python3-fasteners >= 0.15
Requires:       python3-keyring >= 22
Requires:       python3-packaging
Requires:       python3-pathspec >= 0.5.8
Requires:       python3-requests >= 2.16.2
Requires:       python3-rich
Requires:       python3-setuptools
Requires:       python3-typing-extensions
Requires:       python3-watchdog >= 2.0.1

%global debug_package %{nil}

%description
Maestral is an open-source Dropbox client for Linux. It provides a lightweight
daemon that runs in the background and syncs your Dropbox folder.

%package qt
Summary:        Qt GUI for Maestral
Requires:       %{name} = %{version}-%{release}
Requires:       python3-pyqt6
Requires:       python3-markdown2

%description qt
Qt GUI interface for the Maestral Dropbox daemon, providing a system tray
icon, account info, and sync status window.

%prep
%autosetup -n maestral-%{version}

%build
# built in %%install via pip

%install
# Bundle non-Fedora deps (installed --no-deps to avoid pulling in Fedora packages)
pip3 install \
    --root %{buildroot} \
    --prefix %{_prefix} \
    --no-deps \
    --no-warn-script-location \
    "dropbox==12.0.2" \
    "stone==3.3.1" \
    "ply" \
    "desktop-notifier==6.2.0" \
    "bidict" \
    "dbus-fast" \
    "keyrings.alt" \
    "Pyro5" \
    "serpent" \
    "survey" \
    "xattr"

# Install maestral itself from source
pip3 install \
    --root %{buildroot} \
    --prefix %{_prefix} \
    --no-deps \
    --no-warn-script-location \
    .

# Install maestral-qt from the bundled source
pip3 install \
    --root %{buildroot} \
    --prefix %{_prefix} \
    --no-deps \
    --no-warn-script-location \
    %{_sourcedir}/maestral_qt-1.9.8.tar.gz

# Remove binaries we don't want to ship
rm -f %{buildroot}%{_bindir}/keyring
rm -f %{buildroot}%{_bindir}/pyro5-*
rm -f %{buildroot}%{_bindir}/stone

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_bindir}/maestral
%{_bindir}/xattr
%{python3_sitelib}/maestral/
%{python3_sitelib}/maestral-%{version}.dist-info/
# Bundled non-Fedora deps
%{python3_sitelib}/dropbox/
%{python3_sitelib}/dropbox-*.dist-info/
%{python3_sitelib}/stone/
%{python3_sitelib}/stone-*.dist-info/
%{python3_sitelib}/ply/
%{python3_sitelib}/ply-*.dist-info/
%{python3_sitelib}/desktop_notifier/
%{python3_sitelib}/desktop_notifier-*.dist-info/
%{python3_sitelib}/bidict/
%{python3_sitelib}/bidict-*.dist-info/
%dir %{python3_sitelib}/keyrings/
%{python3_sitelib}/keyrings/__init__.py
%dir %{python3_sitelib}/keyrings/__pycache__/
%{python3_sitelib}/keyrings/__pycache__/
%{python3_sitelib}/keyrings/alt/
%{python3_sitelib}/keyrings.alt-*.dist-info/
%{python3_sitelib}/Pyro5/
%{python3_sitelib}/pyro5-*.dist-info/
%{python3_sitelib}/serpent*
%{python3_sitelib}/__pycache__/serpent*
%{python3_sitelib}/survey/
%{python3_sitelib}/survey-*.dist-info/
%{python3_sitearch}/xattr/
%{python3_sitearch}/xattr-*.dist-info/
%{python3_sitearch}/dbus_fast/
%{python3_sitearch}/dbus_fast-*.dist-info/
%{_datadir}/icons/hicolor/512x512/apps/maestral.png

%files qt
%{_bindir}/maestral_qt
%{python3_sitelib}/maestral_qt/
%{python3_sitelib}/maestral_qt-*.dist-info/
%{_datadir}/applications/maestral.desktop
%{_datadir}/icons/maestral.png

%changelog
* Sat May 30 2026 drelbszoomer <algosystem@gmail.com> - 1.9.6-1
- Initial package (maestral 1.9.6, maestral-qt 1.9.8)
- Bundles non-Fedora deps: dropbox, Pyro5, desktop-notifier, keyrings.alt, survey, xattr, dbus-fast, bidict
