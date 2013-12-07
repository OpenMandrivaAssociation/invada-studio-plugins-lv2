%define name            invada-studio-plugins-lv2
%define version         1.2.0
%define release          7
%define debug_package          %{nil}

%define ladspadir       %{_libdir}/ladspa

Name:           %{name}
Summary:        Studio LV2 plugins with GUI
Version:        %{version}
Release:        %{release}

Source:         http://launchpad.net/invada-studio/ladspa/0.3/+download/%{name}_%{version}-nopkg.tgz
Patch0:         invada-studio-1.2.0-update-turtle.patch
URL:            http://www.invadarecords.com/Downloads.php?ID=00000264
License:        GPLv2
Group:          Sound
BuildRequires:  lv2-devel
BuildRequires:  cairo-devel slv2-devel
BuildRequires:  pkgconfig(gtk+-2.0) libglade2.0-devel

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




%changelog
* Wed Apr 25 2012 Frank Kober <emuse@mandriva.org> 1.2.0-6
+ Revision: 793407
- rebuild adding patch from falktx fixing lv2 descriptors
- rebuild adding patch from falktx fixing lv2 descriptors

* Sun Dec 04 2011 Frank Kober <emuse@mandriva.org> 1.2.0-5
+ Revision: 737636
+ rebuild (emptylog)

* Sat Dec 03 2011 Frank Kober <emuse@mandriva.org> 1.2.0-4
+ Revision: 737509
- Fixed BR name change

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2011.0
+ Revision: 612400
- the mass rebuild of 2010.1 packages

* Tue Apr 06 2010 Frank Kober <emuse@mandriva.org> 1.2.0-2mdv2010.1
+ Revision: 531917
- bump release
- fix requires

* Tue Apr 06 2010 Frank Kober <emuse@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 531915
- import invada-studio-plugins-lv2


