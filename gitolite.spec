#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : gitolite
Version  : 3.6.13
Release  : 51
URL      : https://github.com/sitaramc/gitolite/archive/v3.6.13/gitolite-3.6.13.tar.gz
Source0  : https://github.com/sitaramc/gitolite/archive/v3.6.13/gitolite-3.6.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gitolite-bin = %{version}-%{release}
Requires: gitolite-data = %{version}-%{release}
Requires: gitolite-license = %{version}-%{release}
Requires: gitolite-perl = %{version}-%{release}
Requires: perl(Redis)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-makefile.patch

%description
#!/usr/bin/perl
use strict;
use warnings;
use lib $ENV{GL_LIBDIR};
use Gitolite::Easy;

%package bin
Summary: bin components for the gitolite package.
Group: Binaries
Requires: gitolite-data = %{version}-%{release}
Requires: gitolite-license = %{version}-%{release}

%description bin
bin components for the gitolite package.


%package data
Summary: data components for the gitolite package.
Group: Data

%description data
data components for the gitolite package.


%package license
Summary: license components for the gitolite package.
Group: Default

%description license
license components for the gitolite package.


%package perl
Summary: perl components for the gitolite package.
Group: Default
Requires: gitolite = %{version}-%{release}

%description perl
perl components for the gitolite package.


%prep
%setup -q -n gitolite-3.6.13
cd %{_builddir}/gitolite-3.6.13
%patch -P 1 -p1
pushd ..
cp -a gitolite-3.6.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737561548
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1737561548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gitolite
cp %{_builddir}/gitolite-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gitolite/9171b73c58271d57144d45127d0ac8f1b766c50d || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
make install DESTDIR=%{buildroot} VER=%{version}_v3
popd
GOAMD64=v2
make install DESTDIR=%{buildroot} VER=%{version}
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gitolite

%files data
%defattr(-,root,root,-)
/usr/share/gitolite/VERSION
/usr/share/gitolite/VREF/COUNT
/usr/share/gitolite/VREF/EMAIL-CHECK
/usr/share/gitolite/VREF/FILETYPE
/usr/share/gitolite/VREF/MAX_NEWBIN_SIZE
/usr/share/gitolite/VREF/MERGE-CHECK
/usr/share/gitolite/VREF/NAME_NC
/usr/share/gitolite/VREF/VOTES
/usr/share/gitolite/VREF/lock
/usr/share/gitolite/VREF/partial-copy
/usr/share/gitolite/VREF/refex-expr
/usr/share/gitolite/commands/1plus1
/usr/share/gitolite/commands/D
/usr/share/gitolite/commands/access
/usr/share/gitolite/commands/compile-template-data
/usr/share/gitolite/commands/config
/usr/share/gitolite/commands/create
/usr/share/gitolite/commands/creator
/usr/share/gitolite/commands/desc
/usr/share/gitolite/commands/fork
/usr/share/gitolite/commands/git-annex-shell
/usr/share/gitolite/commands/git-config
/usr/share/gitolite/commands/help
/usr/share/gitolite/commands/htpasswd
/usr/share/gitolite/commands/info
/usr/share/gitolite/commands/list-dangling-repos
/usr/share/gitolite/commands/lock
/usr/share/gitolite/commands/mirror
/usr/share/gitolite/commands/motd
/usr/share/gitolite/commands/newbranch
/usr/share/gitolite/commands/option
/usr/share/gitolite/commands/owns
/usr/share/gitolite/commands/perms
/usr/share/gitolite/commands/print-default-rc
/usr/share/gitolite/commands/push
/usr/share/gitolite/commands/readme
/usr/share/gitolite/commands/rsync
/usr/share/gitolite/commands/sshkeys-lint
/usr/share/gitolite/commands/sskm
/usr/share/gitolite/commands/sudo
/usr/share/gitolite/commands/svnserve
/usr/share/gitolite/commands/symbolic-ref
/usr/share/gitolite/commands/who-pushed
/usr/share/gitolite/commands/writable
/usr/share/gitolite/gitolite
/usr/share/gitolite/gitolite-shell
/usr/share/gitolite/lib/Gitolite/Cache.pm
/usr/share/gitolite/lib/Gitolite/Common.pm
/usr/share/gitolite/lib/Gitolite/Conf.pm
/usr/share/gitolite/lib/Gitolite/Conf/Explode.pm
/usr/share/gitolite/lib/Gitolite/Conf/Load.pm
/usr/share/gitolite/lib/Gitolite/Conf/Store.pm
/usr/share/gitolite/lib/Gitolite/Conf/Sugar.pm
/usr/share/gitolite/lib/Gitolite/Easy.pm
/usr/share/gitolite/lib/Gitolite/Hooks/PostUpdate.pm
/usr/share/gitolite/lib/Gitolite/Hooks/Update.pm
/usr/share/gitolite/lib/Gitolite/Rc.pm
/usr/share/gitolite/lib/Gitolite/Setup.pm
/usr/share/gitolite/lib/Gitolite/Test.pm
/usr/share/gitolite/lib/Gitolite/Test/Tsh.pm
/usr/share/gitolite/lib/Gitolite/Triggers.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Alias.pm
/usr/share/gitolite/lib/Gitolite/Triggers/AutoCreate.pm
/usr/share/gitolite/lib/Gitolite/Triggers/CpuTime.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Kindergarten.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Mirroring.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Motd.pm
/usr/share/gitolite/lib/Gitolite/Triggers/RefexExpr.pm
/usr/share/gitolite/lib/Gitolite/Triggers/RepoUmask.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Shell.pm
/usr/share/gitolite/lib/Gitolite/Triggers/TProxy.pm
/usr/share/gitolite/lib/Gitolite/Triggers/Writable.pm
/usr/share/gitolite/syntactic-sugar/continuation-lines
/usr/share/gitolite/syntactic-sugar/keysubdirs-as-groups
/usr/share/gitolite/syntactic-sugar/macros
/usr/share/gitolite/syntactic-sugar/refex-expr
/usr/share/gitolite/triggers/bg
/usr/share/gitolite/triggers/expand-deny-messages
/usr/share/gitolite/triggers/partial-copy
/usr/share/gitolite/triggers/post-compile/create-with-reference
/usr/share/gitolite/triggers/post-compile/ssh-authkeys
/usr/share/gitolite/triggers/post-compile/ssh-authkeys-shell-users
/usr/share/gitolite/triggers/post-compile/ssh-authkeys-split
/usr/share/gitolite/triggers/post-compile/update-description-file
/usr/share/gitolite/triggers/post-compile/update-git-configs
/usr/share/gitolite/triggers/post-compile/update-git-daemon-access-list
/usr/share/gitolite/triggers/post-compile/update-gitweb-access-list
/usr/share/gitolite/triggers/post-compile/update-gitweb-daemon-from-options
/usr/share/gitolite/triggers/renice
/usr/share/gitolite/triggers/repo-specific-hooks
/usr/share/gitolite/triggers/set-default-roles
/usr/share/gitolite/triggers/upstream

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gitolite/9171b73c58271d57144d45127d0ac8f1b766c50d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
