Name:           wl-clip-persist
Version:        0.5.0
Release:        1%{?dist}
Summary:        Keep Wayland clipboard even after programs close

License:        MIT
URL:            https://github.com/Linus789/wl-clip-persist
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo

%description
Normally, when you copy something on Wayland and then close the application
you copied from, the copied data disappears and you cannot paste it anymore.
wl-clip-persist solves that by reading clipboard data into memory and
rewriting it so it persists after the source application closes.

Requires a Wayland compositor that supports ext-data-control-v1 or
wlr-data-control-unstable-v1.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat May 30 2026 drelbszoomer <algosystem@gmail.com> - 0.5.0-1
- Initial package
