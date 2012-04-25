%define name            invada-studio-plugins-lv2
%define version         1.2.0
%define release         6

%define ladspadir       %{_libdir}/ladspa

Name:           %{name}
Summary:        Studio LV2 plugins with GUI
Version:        %{version}
Release:        %{release}

Source:         http://launchpad.net/invada-studio/ladspa/0.3/+download/%{name}_%{version}-nopkg.tgz
Patch0:         invada-studio-1.2.0-update-turtle.patch
URL:            http://www.invadarecords.com/Downloads.php?ID=00000264
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        GPLv2
Group:          Sound
BuildRequires:  cairo-devel slv2-devel
BuildRequires:  gtk+2-devel libglade2.0-devel

%description
This package provides a kit of LV2 plugins for sound studio usage
developed by Invada Records under GPLv2 license. It contains delay,
distortion, dynamics, low- and high-pass filter, phaser, early-reflection
reverbs, input amp, meter and test-tone plugins.

%prep
%setup -q
%patch0 -p1

%build
# replace /usr/local/lib/lv2 directory by appropriate lv2 directory
perl -pi -e 's/\/local\/lib/\/%{_lib}/g' Makefile
%make

%install
rm -rf %{buildroot}

%make install-sys DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/lv2/invada.lv2/*


