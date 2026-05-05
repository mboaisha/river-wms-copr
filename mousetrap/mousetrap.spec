%global commit      e370b6b152dc9477affc9b1ee167f5ae6bed6579
%global shortcommit %(c=%{commit}; echo ${c:0:10})
%global commitdate  20260430

Name:           mousetrap
Version:        0.1^git%{commitdate}.%{shortcommit}
Release:        %autorelease
Summary:        A minimal window manager replicating stumpwm/ratpoison behavior

License:        MIT
URL:            https://codeberg.org/g4b/mousetrap
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson >= 1.10.0
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.47
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(spdlog)
BuildRequires: 	git-core

Requires:       river >= 0.4.0

%description
Mousetrap is a minimal Wayland window manager for the river compositor that
replicates the behavior of stumpwm and ratpoison: all windows are fullscreen
(frame splitting is on the roadmap), keyboard-driven with prefix-based
bindings (GNU screen-style), no window decorations, and a minimal themeable
UI based on layer-shell message and input boxes.

A configuration file is required for any keybindings to work. An example
config.toml is installed under %{_pkgdocdir}; copy it to
~/.config/mousetrap/ and customize.

%prep
%autosetup -n %{name}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md config.toml
%{_bindir}/mousetrap
%{_bindir}/river_input

%changelog
%autochangelog
