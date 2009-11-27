%define name odvr
%define version 0.1.5
%define release %mkrel 1

Summary: User-space driver for USB-enabled Olympus DVRs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv3
Group: System/Kernel and hardware
Url: http://code.google.com/p/odvr/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel
BuildRequires: usb1.0-devel
BuildRequires: usb-compat-devel
BuildRequires: sndfile-devel

%description
odvr is a user-space driver for USB-enabled Olympus DVRs that do not
support the USB Mass Storage specification. odvr is tested against the
VN-960PC, but should support other "VN" Olympus models. See
SupportedDevices for a list of known-working devices.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
%__install -d %{buildroot}
%__install -d %{buildroot}%{_bindir}
%__install -m 755 odvr %{buildroot}%{_bindir}
%__install -m 755 odvr-gui %{buildroot}%{_bindir}
%__install -d %{buildroot}%_sysconfdir/udev/rules.d
%__install -m 644 41-odvr.rules %{buildroot}%_sysconfdir/udev/rules.d

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/odvr
%{_bindir}/odvr-gui
%_sysconfdir/udev/rules.d/41-odvr.rules
