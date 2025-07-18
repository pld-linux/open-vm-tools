# Conditional build:
%bcond_without	apidocs		# without API docs
%bcond_without	x		# build with X11 support

Summary:	VMWare guest utilities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware
Name:		open-vm-tools
Version:	13.0.0
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/System
#Source0:	https://github.com/vmware/open-vm-tools/archive/%{version}.tar.xz
Source0:	https://github.com/vmware/open-vm-tools/archive/refs/tags/stable-%{version}.tar.gz
# Source0-md5:	277a55da4d7a8be5bea6151bfe6a81af
Source1:	%{name}-packaging
Source2:	%{name}-modprobe.d
Source3:	%{name}-init
Source4:	%{name}-vmware-user.desktop
Source5:	vmware-vmblock-fuse.service
Source6:	vmtoolsd.pamd
Patch0:		%{name}-dnd.patch
Patch1:		iopl.patch
URL:		https://github.com/vmware/open-vm-tools
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	libdnet-devel
BuildRequires:	libdrm-devel
BuildRequires:	libfuse3-devel >= 3.10.0
BuildRequires:	libicu-devel
BuildRequires:	libmspack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtirpc-devel
BuildRequires:	libxml2-devel
BuildRequires:	mscgen
BuildRequires:	openssl-devel >= 1.0.1
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-devel >= 3.0.0
BuildRequires:	rpcsvc-proto
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	udev-devel
BuildRequires:	xmlsec1-devel
%if %{with x}
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libsigc++-devel >= 2.5.1
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
%endif
Requires:	ethtool
Requires:	glib2 >= 1:2.34.0
Requires:	libdnet
Requires:	libicu
Requires:	openssl >= 1.0.1
ExclusiveArch:	%{ix86} %{x8664} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libDeployPkg.so.0.0.0

%description
VMWare guest utilities.

%description -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware.

%package devel
Summary:	Header files for open-vm-tools
Summary(pl.UTF-8):	Pliki nagłówkowe open-vm-tools
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for open-vm-tools.

%description devel -l pl.UTF-8
Pliki nagłówkowe open-vm-tools.

%package        sdmp
Summary:	Service Discovery Plugin
Summary(pl.UTF-8):	Wtyczka Service Discovery
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description      sdmp
The Service Discovery plugin connects with the vRealize Operations
Manager product. This plug-in provides fabric admins with more
information to better manage VMs at large scale. VMware Tools already
collects some data from VMs, but it is not sufficient. This plug-in
collects additional data and relays it to vRealize Operations Manager
if the management feature is enabled. The plugin is enabled by default
and can be disabled at any time by the guest administrator inside the
guest.

%description      sdmp -l pl.UTF-8
Wtyczka Service Discovery łączy się z produktem vRealize Operations
Manager. Ta wtyczka zapewnia administratorom sieci szkieletowej więcej
informacji w celu lepszego zarządzania maszynami wirtualnymi na dużą
skalę. VMware Tools już zbiera pewne dane z maszyn wirtualnych, ale to
nie wystarcza. Ta wtyczka zbiera dodatkowe dane i przekazuje je do
vRealize Operations Manager, jeśli funkcja zarządzania jest włączona.
Wtyczka jest domyślnie włączona i może zostać wyłączona w dowolnym
momencie przez administratora gościa wewnątrz gościa.

%package        salt-minion
Summary:	Script file to install/uninstall salt-minion
Summary(pl.UTF-8):	Skrypt do instalowania/usuwania salt-minion
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	coreutils
Requires:	curl
Requires:	gawk
Requires:	grep
Requires:	systemd
ExclusiveArch:	x86_64

%description    salt-minion
Salt Project is a Python based open-source software for event driven
IT automation, remote task execution and configuration management.
Salt requires a salt-minion to be deployed in the guest. Salt specific
guest variables are set on the host side per VM basis and subsequently
read by VMware Tools inside guest. VMware Tools then downloads the
salt bundle and spins up a salt-minion instance inside the guest.
Supports only 64 bit OSes.

%description    salt-minion -l pl.UTF-8
Projekt Salt to oparte na języku Python oprogramowanie open source do
automatyzacji IT sterowanej zdarzeniami, zdalnego wykonywania zadań i
zarządzania konfiguracją. Salt wymaga użycia salt-minion'a
uruchomionego w gościu. Zmienne gościa specyficzne dla Salt są
ustawiane po stronie hosta dla każdej maszyny wirtualnej, a następnie
odczytywane przez narzędzia VMware Tools wewnątrz gościa. VMware Tools
następnie pobiera pakiet salt i uruchamia instancję salt-minion
wewnątrz gościa. Wspierane są tylko 64-bitowe systemy operacyjne

%package static
Summary:	Static open-vm-tools libraries
Summary(pl.UTF-8):	Statyczne biblioteki open-vm-tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static open-vm-tools libraries.

%description static -l pl.UTF-8
Statyczne biblioteki open-vm-tools.

%package gui
Summary:	VMware guest utitities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware.
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libsigc++ >= 2.5.1

%description gui
VMWare guest utilities. This package contains GUI part of tools.

%description gui -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware. Ten pakiet zawiera graficzną
część narzędzi.

%package apidocs
Summary:	VMware API documentation
Summary(pl.UTF-8):	Dokumentacja do API VMware
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description apidocs
This package contains VMware API documentation.

%description apidocs -l pl.UTF-8
Ten pakiet zawiera dokumentację do API VMware.

%package -n udev-open-vm-tools
Summary:	UDEV rules for open-vm-tools
Summary(pl.UTF-8):	Reguły UDEV dla open-vm-tools
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	udev-core

%description -n udev-open-vm-tools
UDEV rules for open-vm-tools.

%description -n udev-open-vm-tools -l pl.UTF-8
Reguły UDEV dla open-vm-tools.

%prep
%setup -q -n %{name}-stable-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

cp %{SOURCE1} open-vm-tools/packaging
%{__sed} -i '1s,%{_bindir}/env bash$,%{__bash},' \
	open-vm-tools/services/plugins/componentMgr/svtminion.sh

%build
cd open-vm-tools
rm -rf autom4te.cache
install -d config
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure2_13 \
	--disable-tests \
	--without-kernel-modules \
	--enable-resolutionkms \
	--enable-servicediscovery \
	--enable-salt-minion \
%if %{with x}
	--with-x
%else
	--without-x
%endif
%{__make} \
	CFLAGS="%{rpmcflags} -Wno-unused-but-set-variable" \
	CXXFLAGS="%{rpmcxxflags} -std=c++11 -Wno-unused-but-set-variable"

%install
rm -rf $RPM_BUILD_ROOT

cd open-vm-tools
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/open-vm-tools/plugins/common/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

install -d $RPM_BUILD_ROOT/etc/{modprobe.d,rc.d/init.d,xdg/autostart}
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/modprobe.d/%{name}.conf
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/xdg/autostart/vmware-user.desktop
cp %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/vmtoolsd

install -d $RPM_BUILD_ROOT%{systemdunitdir}
cp %{SOURCE5} $RPM_BUILD_ROOT%{systemdunitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add open-vm-tools
%service open-vm-tools restart "Open Virtual Machine"
%systemd_post vmware-vmblock-fuse.service

%post sdmp
%service open-vm-tools restart "Open Virtual Machine"

%preun
if [ "$1" = "0" ]; then
	%service open-vm-tools stop
	/sbin/chkconfig --del open-vm-tools
fi
%systemd_preun vmware-vmblock-fuse.service

%postun
/sbin/ldconfig
%systemd_reload

%postun sdmp
%service open-vm-tools restart "Open Virtual Machine"

%files
%defattr(644,root,root,755)
%doc README.md ReleaseNotes.md open-vm-tools/AUTHORS open-vm-tools/ChangeLog open-vm-tools/README open-vm-tools/packaging
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/vmtoolsd
%dir %{_sysconfdir}/vmware-tools
%attr(755,root,root) %{_sysconfdir}/vmware-tools/*vm-*
%{_sysconfdir}/vmware-tools/tools.conf.example
%{_sysconfdir}/vmware-tools/vgauth.conf
%dir %{_sysconfdir}/vmware-tools/vgauth
%{_sysconfdir}/vmware-tools/vgauth/schemas
%attr(755,root,root) %{_sysconfdir}/vmware-tools/statechange.subr
%dir %{_sysconfdir}/vmware-tools/scripts
%dir %{_sysconfdir}/vmware-tools/scripts/vmware
%attr(755,root,root) %{_sysconfdir}/vmware-tools/scripts/vmware/network
%attr(755,root,root) %{_bindir}/VGAuthService
%attr(755,root,root) %{_bindir}/vm-support
%attr(755,root,root) %{_bindir}/vmhgfs-fuse
%attr(755,root,root) %{_bindir}/vmtoolsd
%attr(755,root,root) %{_bindir}/vmware-alias-import
%attr(755,root,root) %{_bindir}/vmware-checkvm
%attr(755,root,root) %{_bindir}/vmware-hgfsclient
%attr(755,root,root) %{_bindir}/vmware-namespace-cmd
%attr(755,root,root) %{_bindir}/vmware-rpctool
%attr(755,root,root) %{_bindir}/vmware-toolbox-cmd
%attr(755,root,root) %{_bindir}/vmware-xferlogs
%attr(755,root,root) %{_bindir}/vmware-vgauth-cmd
%attr(755,root,root) %{_bindir}/vmware-vgauth-smoketest
%attr(755,root,root) %{_bindir}/vmware-vmblock-fuse
%attr(755,root,root) %{_libdir}/libDeployPkg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libDeployPkg.so.0
%attr(755,root,root) %{_libdir}/libguestStoreClient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguestStoreClient.so.0
%attr(755,root,root) %{_libdir}/libguestlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguestlib.so.0
%attr(755,root,root) %{_libdir}/libvgauth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvgauth.so.0
%attr(755,root,root) %{_libdir}/libvmtools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvmtools.so.0
%attr(755,root,root) %{_libdir}/libhgfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhgfs.so.0
%dir %{_libdir}/open-vm-tools
%dir %{_libdir}/open-vm-tools/plugins
%dir %{_libdir}/open-vm-tools/plugins/vmsvc
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libappInfo.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libcomponentMgr.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libdeployPkgPlugin.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libgdp.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libguestInfo.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libguestStore.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libpowerOps.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libresolutionKMS.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libtimeSync.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libvmbackup.so
%dir %{_libdir}/open-vm-tools/plugins/common
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/common/libhgfsServer.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/common/libvix.so
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%{systemdunitdir}/vmware-vmblock-fuse.service
/etc/modprobe.d/%{name}.conf
%dir %{_datadir}/open-vm-tools
%dir %{_datadir}/open-vm-tools/messages
%lang(de) %{_datadir}/open-vm-tools/messages/de
%lang(en) %{_datadir}/open-vm-tools/messages/en
%lang(es) %{_datadir}/open-vm-tools/messages/es
%lang(fr) %{_datadir}/open-vm-tools/messages/fr
%lang(it) %{_datadir}/open-vm-tools/messages/it
%lang(ja) %{_datadir}/open-vm-tools/messages/ja
%lang(ko) %{_datadir}/open-vm-tools/messages/ko
%lang(zh_CN) %{_datadir}/open-vm-tools/messages/zh_CN
%lang(zh_TW) %{_datadir}/open-vm-tools/messages/zh_TW

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libDeployPkg.so
%attr(755,root,root) %{_libdir}/libguestlib.so
%attr(755,root,root) %{_libdir}/libguestStoreClient.so
%attr(755,root,root) %{_libdir}/libvgauth.so
%attr(755,root,root) %{_libdir}/libvmtools.so
%attr(755,root,root) %{_libdir}/libhgfs.so
%dir %{_includedir}/libDeployPkg
%{_includedir}/libDeployPkg/*.h
%dir %{_includedir}/vmGuestLib
%{_includedir}/vmGuestLib/includeCheck.h
%{_includedir}/vmGuestLib/vmGuestLib.h
%{_includedir}/vmGuestLib/vmSessionId.h
%{_includedir}/vmGuestLib/vm_basic_types.h
%{_libdir}/libDeployPkg.la
%{_libdir}/libguestlib.la
%{_libdir}/libguestStoreClient.la
%{_libdir}/libvgauth.la
%{_libdir}/libvmtools.la
%{_libdir}/libhgfs.la
%{_pkgconfigdir}/libDeployPkg.pc
%{_pkgconfigdir}/vmguestlib.pc

%ifarch x86_64
%files salt-minion
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/componentMgr/
%dir %{_libdir}/%{name}/componentMgr/saltMinion/
%attr(755,root,root) %{_libdir}/%{name}/componentMgr/saltMinion/svtminion.sh
%endif

%files sdmp
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/serviceDiscovery/
%dir %{_libdir}/%{name}/serviceDiscovery/scripts/
%attr(755,root,root) %{_libdir}/%{name}/plugins/vmsvc/libserviceDiscovery.so
%attr(755,root,root) %{_libdir}/%{name}/serviceDiscovery/scripts/get-connection-info.sh
%attr(755,root,root) %{_libdir}/%{name}/serviceDiscovery/scripts/get-listening-process-info.sh
%attr(755,root,root) %{_libdir}/%{name}/serviceDiscovery/scripts/get-listening-process-perf-metrics.sh
%attr(755,root,root) %{_libdir}/%{name}/serviceDiscovery/scripts/get-versions.sh

%files static
%defattr(644,root,root,755)
%{_libdir}/libDeployPkg.a
%{_libdir}/libguestlib.a
%{_libdir}/libguestStoreClient.a
%{_libdir}/libvgauth.a
%{_libdir}/libvmtools.a
%{_libdir}/libhgfs.a

%if %{with x}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vmwgfxctrl
%attr(755,root,root) %{_bindir}/vmware-user
%attr(4755,root,root) %{_bindir}/vmware-user-suid-wrapper
%{_sysconfdir}/xdg/autostart/vmware-user.desktop
%dir %{_libdir}/open-vm-tools/plugins/vmusr
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libdesktopEvents.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libdndcp.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libresolutionSet.so
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc open-vm-tools/docs/api/build/html/*
%endif

%files -n udev-open-vm-tools
%defattr(644,root,root,755)
/lib/udev/rules.d/99-vmware-scsi-udev.rules
