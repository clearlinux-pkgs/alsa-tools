#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-tools
Version  : 1.2.11
Release  : 6
URL      : https://www.alsa-project.org/files/pub/tools/alsa-tools-1.2.11.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/tools/alsa-tools-1.2.11.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/tools/alsa-tools-1.2.11.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: alsa-tools-bin = %{version}-%{release}
Requires: alsa-tools-data = %{version}-%{release}
Requires: alsa-tools-lib = %{version}-%{release}
Requires: alsa-tools-license = %{version}-%{release}
Requires: alsa-tools-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : fltk-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-build.patch

%description
Some sort of GUI for ld10k1.
Still early stage of development.
Source is ugly (better not to read).
Don't expeect everything will work.
To compile needs QT instaled.
First install ld10k1.

%package bin
Summary: bin components for the alsa-tools package.
Group: Binaries
Requires: alsa-tools-data = %{version}-%{release}
Requires: alsa-tools-license = %{version}-%{release}

%description bin
bin components for the alsa-tools package.


%package data
Summary: data components for the alsa-tools package.
Group: Data

%description data
data components for the alsa-tools package.


%package dev
Summary: dev components for the alsa-tools package.
Group: Development
Requires: alsa-tools-lib = %{version}-%{release}
Requires: alsa-tools-bin = %{version}-%{release}
Requires: alsa-tools-data = %{version}-%{release}
Provides: alsa-tools-devel = %{version}-%{release}
Requires: alsa-tools = %{version}-%{release}

%description dev
dev components for the alsa-tools package.


%package lib
Summary: lib components for the alsa-tools package.
Group: Libraries
Requires: alsa-tools-data = %{version}-%{release}
Requires: alsa-tools-license = %{version}-%{release}

%description lib
lib components for the alsa-tools package.


%package license
Summary: license components for the alsa-tools package.
Group: Default

%description license
license components for the alsa-tools package.


%package man
Summary: man components for the alsa-tools package.
Group: Default

%description man
man components for the alsa-tools package.


%prep
%setup -q -n alsa-tools-1.2.11
cd %{_builddir}/alsa-tools-1.2.11
%patch -P 1 -p1
pushd ..
cp -a alsa-tools-1.2.11 buildavx2
popd

%build
## build_prepend content
for subdir in $(make list_subdirs); do
(cd $subdir && autoreconf -vfi);
done
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707785091
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
for subdir in $(make list_subdirs); do
(cd $subdir && autoreconf -vfi);
done
## build_prepend end
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707785091
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-tools
cp %{_builddir}/alsa-tools-%{version}/as10k1/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/9db6e6f4189b7101178eef598c9985910e51456d || :
cp %{_builddir}/alsa-tools-%{version}/echomixer/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/alsa-tools-%{version}/envy24control/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647 || :
cp %{_builddir}/alsa-tools-%{version}/hdspconf/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/alsa-tools-%{version}/hdsploader/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/alsa-tools-%{version}/hdspmixer/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/alsa-tools-%{version}/ld10k1/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
cp %{_builddir}/alsa-tools-%{version}/ld10k1/COPYING.LIB %{buildroot}/usr/share/package-licenses/alsa-tools/597bf5f9c0904bd6c48ac3a3527685818d11246d || :
cp %{_builddir}/alsa-tools-%{version}/qlo10k1/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647 || :
cp %{_builddir}/alsa-tools-%{version}/rmedigicontrol/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647 || :
cp %{_builddir}/alsa-tools-%{version}/sb16_csp/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647 || :
cp %{_builddir}/alsa-tools-%{version}/seq/sbiload/COPYING %{buildroot}/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/as10k1
/V3/usr/bin/cspctl
/V3/usr/bin/dl10k1
/V3/usr/bin/echomixer
/V3/usr/bin/envy24control
/V3/usr/bin/hda-verb
/V3/usr/bin/hdajackretask
/V3/usr/bin/hdajacksensetest
/V3/usr/bin/hdspconf
/V3/usr/bin/hdsploader
/V3/usr/bin/hdspmixer
/V3/usr/bin/ld10k1
/V3/usr/bin/lo10k1
/V3/usr/bin/mixartloader
/V3/usr/bin/pcxhrloader
/V3/usr/bin/rmedigicontrol
/V3/usr/bin/sbiload
/V3/usr/bin/sscape_ctl
/V3/usr/bin/us428control
/V3/usr/bin/usx2yloader
/V3/usr/bin/vxloader
/usr/bin/as10k1
/usr/bin/cspctl
/usr/bin/dl10k1
/usr/bin/echomixer
/usr/bin/envy24control
/usr/bin/hda-verb
/usr/bin/hdajackretask
/usr/bin/hdajacksensetest
/usr/bin/hdspconf
/usr/bin/hdsploader
/usr/bin/hdspmixer
/usr/bin/hwmixvolume
/usr/bin/init_audigy
/usr/bin/init_audigy_eq10
/usr/bin/init_live
/usr/bin/ld10k1
/usr/bin/ld10k1d
/usr/bin/lo10k1
/usr/bin/mixartloader
/usr/bin/pcxhrloader
/usr/bin/rmedigicontrol
/usr/bin/sbiload
/usr/bin/sscape_ctl
/usr/bin/us428control
/usr/bin/usx2yloader
/usr/bin/vxloader

%files data
%defattr(-,root,root,-)
/usr/share/applications/echomixer.desktop
/usr/share/applications/envy24control.desktop
/usr/share/applications/hdajackretask.desktop
/usr/share/applications/hdspconf.desktop
/usr/share/applications/hdspmixer.desktop
/usr/share/applications/hwmixvolume.desktop
/usr/share/icons/hicolor/128x128/apps/hdajackretask.png
/usr/share/icons/hicolor/128x128/apps/hwmixvolume.png
/usr/share/icons/hicolor/256x256/apps/hdajackretask.png
/usr/share/icons/hicolor/256x256/apps/hwmixvolume.png
/usr/share/icons/hicolor/48x48/apps/echomixer.png
/usr/share/icons/hicolor/48x48/apps/envy24control.png
/usr/share/icons/hicolor/48x48/apps/hdajackretask.png
/usr/share/icons/hicolor/48x48/apps/hdspconf.png
/usr/share/icons/hicolor/48x48/apps/hdspmixer.png
/usr/share/icons/hicolor/48x48/apps/hwmixvolume.png
/usr/share/ld10k1/effects/copy_2.emu10k1
/usr/share/ld10k1/effects/eq10.emu10k1
/usr/share/ld10k1/effects/fxbus.emu10k1
/usr/share/ld10k1/effects/mono_switch_2.emu10k1
/usr/share/ld10k1/effects/mono_switch_2x2.emu10k1
/usr/share/ld10k1/effects/output.emu10k1
/usr/share/ld10k1/effects/prologic.emu10k1
/usr/share/ld10k1/effects/simple.emu10k1
/usr/share/ld10k1/effects/sto51.emu10k1
/usr/share/ld10k1/effects/switch_2.emu10k1
/usr/share/ld10k1/effects/switch_2x2.emu10k1
/usr/share/ld10k1/effects/switch_6.emu10k1
/usr/share/ld10k1/effects/tone.emu10k1
/usr/share/ld10k1/effects/vol_2.emu10k1
/usr/share/ld10k1/effects/vol_master.emu10k1
/usr/share/sounds/opl3/drums.o3
/usr/share/sounds/opl3/drums.sb
/usr/share/sounds/opl3/std.o3
/usr/share/sounds/opl3/std.sb

%files dev
%defattr(-,root,root,-)
/usr/include/lo10k1/comm.h
/usr/include/lo10k1/ld10k1_error.h
/usr/include/lo10k1/ld10k1_fnc.h
/usr/include/lo10k1/liblo10k1.h
/usr/include/lo10k1/liblo10k1ef.h
/usr/include/lo10k1/liblo10k1lf.h
/usr/include/lo10k1/lo10k1.h
/usr/include/lo10k1/version.h
/usr/lib64/liblo10k1.so
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/liblo10k1.so.0.0.0
/usr/lib64/liblo10k1.so.0
/usr/lib64/liblo10k1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-tools/133efad5329acf364135c569ac01ec084c3d4647
/usr/share/package-licenses/alsa-tools/597bf5f9c0904bd6c48ac3a3527685818d11246d
/usr/share/package-licenses/alsa-tools/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/alsa-tools/9db6e6f4189b7101178eef598c9985910e51456d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cspctl.1
/usr/share/man/man1/envy24control.1
