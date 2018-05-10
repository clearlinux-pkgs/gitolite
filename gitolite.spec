#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gitolite
Version  : 3.6.7
Release  : 8
URL      : https://github.com/sitaramc/gitolite/archive/v3.6.7.tar.gz
Source0  : https://github.com/sitaramc/gitolite/archive/v3.6.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gitolite-bin
Requires: gitolite-data
Patch1: build.patch

%description
============================================
WARNING: THE TEST SUITE DELETES STUFF FIRST!
============================================

%package bin
Summary: bin components for the gitolite package.
Group: Binaries
Requires: gitolite-data

%description bin
bin components for the gitolite package.


%package data
Summary: data components for the gitolite package.
Group: Data

%description data
data components for the gitolite package.


%prep
%setup -q -n gitolite-3.6.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506189587
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1506189587
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%exclude /var/lib/gitolite/.ssh/authorized_keys
/usr/lib/perl5/5.26.1/Gitolite/Cache.pm
/usr/lib/perl5/5.26.1/Gitolite/Common.pm
/usr/lib/perl5/5.26.1/Gitolite/Conf.pm
/usr/lib/perl5/5.26.1/Gitolite/Conf/Explode.pm
/usr/lib/perl5/5.26.1/Gitolite/Conf/Load.pm
/usr/lib/perl5/5.26.1/Gitolite/Conf/Store.pm
/usr/lib/perl5/5.26.1/Gitolite/Conf/Sugar.pm
/usr/lib/perl5/5.26.1/Gitolite/Easy.pm
/usr/lib/perl5/5.26.1/Gitolite/Hooks/PostUpdate.pm
/usr/lib/perl5/5.26.1/Gitolite/Hooks/Update.pm
/usr/lib/perl5/5.26.1/Gitolite/Rc.pm
/usr/lib/perl5/5.26.1/Gitolite/Setup.pm
/usr/lib/perl5/5.26.1/Gitolite/Test.pm
/usr/lib/perl5/5.26.1/Gitolite/Test/Tsh.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Alias.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/AutoCreate.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/CpuTime.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Kindergarten.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Mirroring.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Motd.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/RefexExpr.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/RepoUmask.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Shell.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/TProxy.pm
/usr/lib/perl5/5.26.1/Gitolite/Triggers/Writable.pm

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
