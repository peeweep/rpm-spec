Name:           supersm
Version:        0.5.1
Release:        1%{?dist}
Summary:        Super Symlink Manager.

License:        MIT
URL:            https://github.com/peeweep/%{name}
Source0:        https://github.com/peeweep/%{name}/archive/%{version}.tar.gz

BuildRequires:  g++
BuildRequires:  cmake
BuildRequires:  boost-static
BuildRequires:  glibc-static
BuildRequires:  libstdc++-static

%description
A Super Symlink Manager

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/*
%license LICENSE

%changelog
* Fri May 28 2021 peeweep <peeweep@0x0.ee> - 0.5.1-1
- Initial RPM release
