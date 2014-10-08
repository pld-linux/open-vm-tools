#
# Conditional build:
%bcond_without	kernel		# without kernel modules
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	userspace	# without userspace package
%bcond_with	verbose		# verbose build (V=1)

%if %{without kernel}
%undefine	with_dist_kernel
%endif

# The goal here is to have main, userspace, package built once with
# simple release number, and only rebuild kernel packages with kernel
# version as part of release number, without the need to bump release
# with every kernel change.
%if 0%{?_pld_builder:1} && %{with kernel} && %{with userspace}
%{error:kernel and userspace cannot be built at the same time on PLD builders}
exit 1
%endif

%if "%{_alt_kernel}" != "%{nil}"
%if 0%{?build_kernels:1}
%{error:alt_kernel and build_kernels are mutually exclusive}
exit 1
%endif
%undefine	with_userspace
%global		_build_kernels		%{alt_kernel}
%else
%global		_build_kernels		%{?build_kernels:,%{?build_kernels}}
%endif

%define		kbrs	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo "BuildRequires:kernel%%{_alt_kernel}-module-build >= 3:2.6.20.2" ; done)
%define		kpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%kernel_pkg ; done)
%define		bkpkg	%(echo %{_build_kernels} | tr , '\\n' | while read n ; do echo %%undefine alt_kernel ; [ -z "$n" ] || echo %%define alt_kernel $n ; echo %%build_kernel_pkg ; done)

%define		snap    2011.10.26
%define		subver	%(echo %{snap} | tr -d .)
%define		ver     9.4.6
%define		rev     1770165
%define		rel	2
%define		pname	open-vm-tools
%define		modsrc	modules/linux
Summary:	VMWare guest utilities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware
Name:		%{pname}%{?_pld_builder:%{?with_kernel:-kernel}}%{_alt_kernel}
Version:	%{ver}
#Release:	0.%{subver}.%{rel}%{?with_kernel:@%{_kernel_ver_str}}
Release:	%{rel}%{?_pld_builder:%{?with_kernel:@%{_kernel_ver_str}}}
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/project/open-vm-tools/open-vm-tools/stable-9.4.x/%{pname}-%{ver}-%{rev}.tar.gz
# Source0-md5:	3969daf1535d34e1c5f0c87a779b7642
#Source0:	http://downloads.sourceforge.net/open-vm-tools/open-vm-tools/%{snap}/%{pname}-%{snap}-%{rev}.tar.gz
Source1:	%{pname}-packaging
Source2:	%{pname}-modprobe.d
Source3:	%{pname}-init
Source4:	%{pname}-vmware-user.desktop
Patch0:		%{pname}-linux-3.10.patch
Patch2:		%{pname}-linux-3.12.patch
Patch3:		%{pname}-linux-3.14.patch
Patch4:		%{pname}-linux-3.15.patch
Patch5:		%{pname}-linux-3.16.patch
URL:		http://open-vm-tools.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.679
%if %{with userspace}
BuildRequires:	autoconf
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	gtk+2-devel
BuildRequires:	gtkmm-devel >= 2.4.0
BuildRequires:	libdnet-devel
BuildRequires:	libfuse-devel
BuildRequires:	libicu-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	procps-devel >= 1:3.3.3-2
BuildRequires:	uriparser-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	ethtool
Requires:	libdnet
Requires:	libicu
Obsoletes:	kernel-misc-pvscsi
Obsoletes:	kernel-misc-vmmemctl
%endif
%{?with_dist_kernel:%{expand:%kbrs}}
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{pname}-%{version}-root-%(id -u -n)

%description
VMWare guest utilities.

%description -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware.

%package devel
Summary:	Header files for open-vm-tools
Summary(pl.UTF-8):	Pliki nagłówkowe open-vm-tools
Group:		Development/Libraries
Requires:	%{pname} = %{epoch}:%{version}-%{release}

%description devel
Header files for open-vm-tools.

%description devel -l pl.UTF-8
Pliki nagłówkowe open-vm-tools.

%package static
Summary:	Static open-vm-tools libraries
Summary(pl.UTF-8):	Statyczne biblioteki open-vm-tools
Group:		Development/Libraries
Requires:	%{pname}-devel = %{epoch}:%{version}-%{release}

%description static
Static open-vm-tools libraries.

%description static -l pl.UTF-8
Statyczne biblioteki open-vm-tools.

%package gui
Summary:	VMware guest utitities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware.
Group:		Applications/System
Requires:	%{pname} = %{epoch}:%{version}-%{release}

%description gui
VMWare guest utilities. This package contains GUI part of tools.

%description gui -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware. Ten pakiet zawiera graficzną
część narzędzi.

%define	kernel_pkg()\
%package -n kernel%{_alt_kernel}-misc-vmblock\
Summary:	VMware vmblock Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmblock\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vmblock\
VMware vmblock Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vmblock -l pl.UTF-8\
Moduł jądra Linuksa VMware vmblock.\
\
%package -n kernel%{_alt_kernel}-misc-vmci\
Summary:	VMware vmci Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmci\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vmci\
VMware vmci Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vmci -l pl.UTF-8\
Moduł jądra Linuksa VMware vmci.\
\
%package -n kernel%{_alt_kernel}-misc-vmhgfs\
Summary:	VMware vmhgfs Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmhgfs\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vmhgfs\
VMware vmhgfs Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vmhgfs -l pl.UTF-8\
Moduł jądra Linuksa VMware vmhgfs.\
\
%package -n kernel%{_alt_kernel}-misc-vmsync\
Summary:	VMware vmsync Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmsync\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vmsync\
VMware vmsync Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vmsync -l pl.UTF-8\
Moduł jądra Linuksa VMware vmsync.\
\
%package -n kernel%{_alt_kernel}-misc-vmxnet\
Summary:	VMware vmxnet Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmxnet\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vmxnet\
VMware vmxnet Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vmxnet -l pl.UTF-8\
Moduł jądra Linuksa VMware vmxnet.\
\
%package -n kernel%{_alt_kernel}-misc-vsock\
Summary:	VMware vsock Linux kernel module\
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vsock\
Release:	%{rel}@%{_kernel_ver_str}\
Group:		Base/Kernel\
Requires(post,postun):	/sbin/depmod\
Requires:	dev >= 2.9.0-7\
%if %{with dist_kernel}\
%requires_releq_kernel\
Requires(postun):	%releq_kernel\
%endif\
\
%description -n kernel%{_alt_kernel}-misc-vsock\
VMware vsock Linux kernel module.\
\
%description -n kernel%{_alt_kernel}-misc-vsock -l pl.UTF-8\
Moduł jądra Linuksa VMware vsock.\
\
%if %{with kernel}\
%files -n kernel%{_alt_kernel}-misc-vmblock\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vmblock.ko*\
\
%files -n kernel%{_alt_kernel}-misc-vmhgfs\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vmhgfs.ko*\
\
%if %{_kernel_version_code} < %{_kernel_version_magic 3 10 0}\
%files -n kernel%{_alt_kernel}-misc-vmci\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vmci.ko*\
\
%files -n kernel%{_alt_kernel}-misc-vmsync\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vmsync.ko*\
%endif\
\
%files -n kernel%{_alt_kernel}-misc-vmxnet\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vmxnet.ko*\
\
%files -n kernel%{_alt_kernel}-misc-vsock\
%defattr(644,root,root,755)\
/lib/modules/%{_kernel_ver}/misc/vsock.ko*\
%endif\
\
%post	-n kernel%{_alt_kernel}-misc-vmblock\
%depmod %{_kernel_ver}\
\
%post	-n kernel%{_alt_kernel}-misc-vmci\
%depmod %{_kernel_ver}\
\
%post	-n kernel%{_alt_kernel}-misc-vmhgfs\
%depmod %{_kernel_ver}\
\
%post	-n kernel%{_alt_kernel}-misc-vmsync\
%depmod %{_kernel_ver}\
\
%post	-n kernel%{_alt_kernel}-misc-vmxnet\
%depmod %{_kernel_ver}\
\
%post	-n kernel%{_alt_kernel}-misc-vsock\
%depmod %{_kernel_ver}\
%{nil}

%define build_kernel_pkg()\
export OVT_SOURCE_DIR=$PWD\
%build_kernel_modules -C %{modsrc}/vmblock -m vmblock SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%build_kernel_modules -C %{modsrc}/vmhgfs -m vmhgfs SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%build_kernel_modules -C %{modsrc}/vmxnet -m vmxnet SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%build_kernel_modules -C %{modsrc}/vsock -m vsock SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%install_kernel_modules -D installed -m %{modsrc}/vmblock/vmblock -d misc\
%install_kernel_modules -D installed -m %{modsrc}/vmhgfs/vmhgfs -d misc\
%install_kernel_modules -D installed -m %{modsrc}/vmxnet/vmxnet -d misc\
%install_kernel_modules -D installed -m %{modsrc}/vsock/vsock -d misc\
%if %{_kernel_version_code} < %{_kernel_version_magic 3 10 0}\
%build_kernel_modules -C %{modsrc}/vmci -m vmci SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%build_kernel_modules -C %{modsrc}/vmsync -m vmsync SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}\
%install_kernel_modules -D installed -m %{modsrc}/vmci/vmci -d misc\
%install_kernel_modules -D installed -m %{modsrc}/vmsync/vmsync -d misc\
%endif\
%{nil}

%{?with_kernel:%{expand:%kpkg}}

%prep
#setup -q -n %{pname}-%{snap}-%{rev}
%setup -q -n %{pname}-%{ver}-%{rev}
%if %{with kernel}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%endif

cp %{SOURCE1} packaging
%{__sed} -i -e 's|##{BUILD_OUTPUT}##|build|' docs/api/doxygen.conf

%build
%{?with_kernel:%{expand:%bkpkg}}

%if %{with userspace}
rm -rf autom4te.cache
install -d config
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
export CUSTOM_PROCPS_NAME=procps
%configure2_13 \
	--without-kernel-modules
%{__make} \
	CFLAGS="%{rpmcflags} -Wno-unused-but-set-variable"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kernel}
install -d $RPM_BUILD_ROOT
cp -a installed/* $RPM_BUILD_ROOT
%endif

%if %{with userspace}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/sbin/mount.vmhgfs
ln -sf %{_sbindir}/mount.vmhgfs $RPM_BUILD_ROOT/sbin/mount.vmhgfs
rm -f $RPM_BUILD_ROOT%{_libdir}/open-vm-tools/plugins/common/*.la

install -d $RPM_BUILD_ROOT/etc/{modprobe.d,rc.d/init.d,xdg/autostart}
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/modprobe.d/%{pname}.conf
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{pname}
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/xdg/autostart/vmware-user.desktop
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add open-vm-tools
%service open-vm-tools restart "Open Virtual Machine"

%preun
if [ "$1" = "0" ]; then
	%service open-vm-tools stop
	/sbin/chkconfig --del open-vm-tools
fi

%postun -p /sbin/ldconfig

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README packaging
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/vmtoolsd
%dir /etc/vmware-tools
%attr(755,root,root) /etc/vmware-tools/*vm-*
%attr(755,root,root) /etc/vmware-tools/statechange.subr
%dir /etc/vmware-tools/scripts
%dir /etc/vmware-tools/scripts/vmware
%attr(755,root,root) /etc/vmware-tools/scripts/vmware/network
%attr(755,root,root) /sbin/mount.vmhgfs
%attr(755,root,root) %{_bindir}/vmtoolsd
%attr(755,root,root) %{_bindir}/vmware-checkvm
%attr(755,root,root) %{_bindir}/vmware-hgfsclient
%attr(755,root,root) %{_bindir}/vmware-rpctool
%attr(755,root,root) %{_bindir}/vmware-toolbox-cmd
%attr(4755,root,root) %{_bindir}/vmware-user-suid-wrapper
%attr(755,root,root) %{_bindir}/vmware-xferlogs
%attr(755,root,root) %{_bindir}/vmware-vmblock-fuse
%attr(755,root,root) %{_sbindir}/mount.vmhgfs
%attr(755,root,root) %{_libdir}/libguestlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguestlib.so.0
%attr(755,root,root) %{_libdir}/libvmtools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvmtools.so.0
%attr(755,root,root) %{_libdir}/libhgfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhgfs.so.0
%dir %{_libdir}/open-vm-tools
%dir %{_libdir}/open-vm-tools/plugins
%dir %{_libdir}/open-vm-tools/plugins/vmsvc
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libguestInfo.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libpowerOps.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libtimeSync.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libvmbackup.so
%dir %{_libdir}/open-vm-tools/plugins/common
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/common/libhgfsServer.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/common/libvix.so
%dir %{_libdir}/open-vm-tools/plugins/vmusr
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libdesktopEvents.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libdndcp.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libresolutionSet.so
%attr(754,root,root) /etc/rc.d/init.d/%{pname}
/etc/modprobe.d/%{pname}.conf
%dir %{_datadir}/open-vm-tools
%dir %{_datadir}/open-vm-tools/messages
%lang(de) %{_datadir}/open-vm-tools/messages/de
%lang(ja) %{_datadir}/open-vm-tools/messages/ja
%lang(ko) %{_datadir}/open-vm-tools/messages/ko
%lang(zh_CN) %{_datadir}/open-vm-tools/messages/zh_CN

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguestlib.so
%attr(755,root,root) %{_libdir}/libvmtools.so
%attr(755,root,root) %{_libdir}/libhgfs.so
%dir %{_includedir}/vmGuestLib
%{_includedir}/vmGuestLib/includeCheck.h
%{_includedir}/vmGuestLib/vmGuestLib.h
%{_includedir}/vmGuestLib/vmSessionId.h
%{_includedir}/vmGuestLib/vm_basic_types.h
%{_libdir}/libguestlib.la
%{_libdir}/libvmtools.la
%{_libdir}/libhgfs.la
%{_pkgconfigdir}/vmguestlib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libguestlib.a
%{_libdir}/libvmtools.a
%{_libdir}/libhgfs.a

%files gui
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/vmware-user.desktop
%endif
