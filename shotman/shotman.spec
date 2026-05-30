Name:           shotman
Version:        0.5.0
Release:        1%{?dist}
Summary:        Uncompromising screenshot GUI for Wayland compositors

License:        ISC
URL:            https://sr.ht/~whynothugo/shotman
Source0:        https://git.sr.ht/~whynothugo/shotman/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  pkgconfig(xkbcommon)

Recommends:     slurp >= 1.4.0

%description
shotman takes a screenshot and shows it in a small floating thumbnail window.
The screenshot can then be copied with Ctrl+C, deleted with d, or dismissed
with Escape.

Requires a Wayland compositor supporting wlr_layer_shell,
ext-image-copy-capture, ext-image-capture-source, and
single-pixel-buffer-v1. Region capture requires slurp.

%prep
%autosetup -n %{name}-v%{version}

%build
SHOTMAN_VERSION=%{version} cargo build --release

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Generate and install shell completions
target/release/shotman_completions bash > %{name}.bash
target/release/shotman_completions zsh > _%{name}
target/release/shotman_completions fish > %{name}.fish

install -Dm644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%license LICENCE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Sat May 30 2026 drelbszoomer <algosystem@gmail.com> - 0.5.0-1
- Initial package
