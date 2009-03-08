#
# Conditional build:
%bcond_without	kernel		# without kernel modules
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	userspace	# without userspace package
#
%define		snap	2009.02.18
%define		rev	148847
%define		modsrc	modules/linux
%define		rel	1
Summary:	VMWare guest utilities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware
Name:		open-vm-tools
Version:	%{snap}_%{rev}
Release:	%{rel}
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/open-vm-tools/%{name}-%{snap}-%{rev}.tar.gz
# Source0-md5:	6e473ebdf29f1b15388149bc2fde6941
Source1:	%{name}-packaging
Source2:	%{name}-modprobe.d
Source3:	%{name}-init
Source4:	%{name}-vmware-user.desktop
URL:		http://open-vm-tools.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.453
%if %{with userspace}
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libdnet-devel
BuildRequires:	libfuse-devel
BuildRequires:	libicu-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	uriparser-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	ethtool
Requires:	libdnet
Requires:	libicu
%endif
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.16
%endif
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VMWare guest utilities.

%description -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware.

%package gui
Summary:	VMware guest utitities
Summary(pl.UTF-8):	Narzędzia dla systemu-gościa dla VMware.
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gui
VMWare guest utilities. This package contains GUI part of tools.

%description gui -l pl.UTF-8
Narzędzia dla systemu-gościa dla VMware. Ten pakiet zawiera graficzną
część narzędzi.

%package -n kernel%{_alt_kernel}-misc-pvscsi
Summary:	VMware pvscsi Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware pvscsi
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-pvscsi
VMware pvscsi Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-pvscsi -l pl.UTF-8
Moduł jądra Linuksa VMware pvscsi.

%package -n kernel%{_alt_kernel}-misc-vmblock
Summary:	VMware vmblock Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmblock
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmblock
VMware vmblock Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmblock -l pl.UTF-8
Moduł jądra Linuksa VMware vmblock.

%package -n kernel%{_alt_kernel}-misc-vmci
Summary:	VMware vmci Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmci
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmci
VMware vmci Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmci -l pl.UTF-8
Moduł jądra Linuksa VMware vmci.

%package -n kernel%{_alt_kernel}-misc-vmhgfs
Summary:	VMware vmhgfs Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmhgfs
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmhgfs
VMware vmhgfs Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmhgfs -l pl.UTF-8
Moduł jądra Linuksa VMware vmhgfs.

%package -n kernel%{_alt_kernel}-misc-vmmemctl
Summary:	VMware vmmemctl Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmmemctl
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmmemctl
VMware vmmemctl Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmmemctl -l pl.UTF-8
Moduł jądra Linuksa VMware vmmemctl.

%package -n kernel%{_alt_kernel}-misc-vmsync
Summary:	VMware vmsync Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmsync
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmsync
VMware vmsync Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmsync -l pl.UTF-8
Moduł jądra Linuksa VMware vmsync.

%package -n kernel%{_alt_kernel}-misc-vmxnet
Summary:	VMware vmxnet Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmxnet
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmxnet
VMware vmxnet Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmxnet -l pl.UTF-8
Moduł jądra Linuksa VMware vmxnet.

%package -n kernel%{_alt_kernel}-misc-vmxnet3
Summary:	VMware vmxnet3 Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vmxnet3
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vmxnet3
VMware vmxnet3 Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vmxnet3 -l pl.UTF-8
Moduł jądra Linuksa VMware vmxnet3.

%package -n kernel%{_alt_kernel}-misc-vsock
Summary:	VMware vsock Linux kernel module
Summary(pl.UTF-8):	Moduł jądra Linuksa VMware vsock
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.9.0-7
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-misc-vsock
VMware vsock Linux kernel module.

%description -n kernel%{_alt_kernel}-misc-vsock -l pl.UTF-8
Moduł jądra Linuksa VMware vsock.

%prep
%setup -q -n %{name}-%{snap}-%{rev}
cp %{SOURCE1} packaging

%build
%if %{with kernel}
%build_kernel_modules -C %{modsrc}/pvscsi	-m pvscsi	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmblock	-m vmblock	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmci		-m vmci		SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmhgfs	-m vmhgfs	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmmemctl	-m vmmemctl	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmsync	-m vmsync	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmxnet	-m vmxnet	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vmxnet3	-m vmxnet3	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%build_kernel_modules -C %{modsrc}/vsock	-m vsock	SRCROOT=$PWD VM_KBUILD=26 VM_CCVER=%{cc_version}
%endif

%if %{with userspace}
%configure2_13 \
	--without-kernel-modules
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kernel}
%install_kernel_modules -m %{modsrc}/pvscsi/pvscsi	-d misc
%install_kernel_modules -m %{modsrc}/vmblock/vmblock	-d misc
%install_kernel_modules -m %{modsrc}/vmci/vmci		-d misc
%install_kernel_modules -m %{modsrc}/vmhgfs/vmhgfs	-d misc
%install_kernel_modules -m %{modsrc}/vmmemctl/vmmemctl	-d misc
%install_kernel_modules -m %{modsrc}/vmsync/vmsync	-d misc
%install_kernel_modules -m %{modsrc}/vmxnet/vmxnet	-d misc
%install_kernel_modules -m %{modsrc}/vmxnet3/vmxnet3	-d misc
%install_kernel_modules -m %{modsrc}/vsock/vsock	-d misc
%endif

%if %{with userspace}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/sbin/mount.vmhgfs
ln -sf %{_sbindir}/mount.vmhgfs $RPM_BUILD_ROOT/sbin/mount.vmhgfs
%ifarch %{x8664}
mv $RPM_BUILD_ROOT/etc/pam.d/vmware-guestd-x64 $RPM_BUILD_ROOT/etc/pam.d/vmware-guestd
%endif
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}

install -d $RPM_BUILD_ROOT/etc/{modprobe.d,rc.d/init.d,xdg/autostart}
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/modprobe.d/%{name}.conf
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/xdg/autostart/vmware-user.desktop
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add open-vm-tools
%service open-vm-tools restart "Open Virtual Machine"

%preun
if [ "$1" = "0" ]; then
	%service open-vm-tools stop
	/sbin/chkconfig --del open-vm-tools
fi

%post	-n kernel%{_alt_kernel}-misc-pvscsi
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmblock
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmci
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmhgfs
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmmemctl
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmsync
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmxnet
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vmxnet3
%depmod %{_kernel_ver}

%post	-n kernel%{_alt_kernel}-misc-vsock
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README packaging
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/vmware-guestd
%dir /etc/vmware-tools
%attr(755,root,root) /etc/vmware-tools/*vm-*
%config(noreplace) %verify(not md5 mtime size) /etc/vmware-tools/tools.conf
%dir /etc/vmware-tools/plugins
%attr(755,root,root) /sbin/mount.vmhgfs
%attr(755,root,root) %{_bindir}/vmtoolsd
%attr(755,root,root) %{_bindir}/vmware-checkvm
%attr(755,root,root) %{_bindir}/vmware-hgfsclient
%attr(755,root,root) %{_bindir}/vmware-toolbox-cmd
%attr(4755,root,root) %{_bindir}/vmware-user-suid-wrapper
%attr(755,root,root) %{_bindir}/vmware-xferlogs
%attr(755,root,root) %{_sbindir}/mount.vmhgfs
%attr(755,root,root) %{_sbindir}/vmware-guestd
%attr(755,root,root) %{_libdir}/lib*.so*
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libguestInfo.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libhgfsServer.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libpowerOps.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libtimeSync.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libvix.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmsvc/libvmbackup.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libhgfsServer.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libresolutionSet.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libvix.so
%attr(755,root,root) %{_libdir}/open-vm-tools/plugins/vmusr/libvixUser.so

%attr(754,root,root) /etc/rc.d/init.d/%{name}
/etc/modprobe.d/%{name}.conf

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vmware-toolbox
%attr(755,root,root) %{_bindir}/vmware-user
%{_desktopdir}/vmware-user.desktop
%{_sysconfdir}/xdg/autostart/vmware-user.desktop

%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-misc-pvscsi
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/pvscsi.ko*

%files -n kernel%{_alt_kernel}-misc-vmblock
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmblock.ko*
%attr(755,root,root) %{_bindir}/vmware-vmblock-fuse

%files -n kernel%{_alt_kernel}-misc-vmci
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmci.ko*

%files -n kernel%{_alt_kernel}-misc-vmhgfs
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmhgfs.ko*

%files -n kernel%{_alt_kernel}-misc-vmmemctl
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmmemctl.ko*

%files -n kernel%{_alt_kernel}-misc-vmsync
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmsync.ko*

%files -n kernel%{_alt_kernel}-misc-vmxnet
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmxnet.ko*

%files -n kernel%{_alt_kernel}-misc-vmxnet3
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vmxnet3.ko*

%files -n kernel%{_alt_kernel}-misc-vsock
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/vsock.ko*
%endif
