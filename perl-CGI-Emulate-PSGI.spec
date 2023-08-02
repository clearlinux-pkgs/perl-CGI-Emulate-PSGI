#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-CGI-Emulate-PSGI
Version  : 0.23
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/CGI-Emulate-PSGI-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/CGI-Emulate-PSGI-0.23.tar.gz
Summary  : 'PSGI adapter for CGI'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-CGI-Emulate-PSGI-license = %{version}-%{release}
Requires: perl-CGI-Emulate-PSGI-perl = %{version}-%{release}
Requires: perl(CGI)
Requires: perl(HTTP::Response)
Requires: perl(URI)
BuildRequires : buildreq-cpan
BuildRequires : perl(CGI)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
CGI::Emulate::PSGI - PSGI adapter for CGI
SYNOPSIS
my $app = CGI::Emulate::PSGI->handler(sub {
# Existing CGI code
});

%package dev
Summary: dev components for the perl-CGI-Emulate-PSGI package.
Group: Development
Provides: perl-CGI-Emulate-PSGI-devel = %{version}-%{release}
Requires: perl-CGI-Emulate-PSGI = %{version}-%{release}

%description dev
dev components for the perl-CGI-Emulate-PSGI package.


%package license
Summary: license components for the perl-CGI-Emulate-PSGI package.
Group: Default

%description license
license components for the perl-CGI-Emulate-PSGI package.


%package perl
Summary: perl components for the perl-CGI-Emulate-PSGI package.
Group: Default
Requires: perl-CGI-Emulate-PSGI = %{version}-%{release}

%description perl
perl components for the perl-CGI-Emulate-PSGI package.


%prep
%setup -q -n CGI-Emulate-PSGI-0.23
cd %{_builddir}/CGI-Emulate-PSGI-0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CGI-Emulate-PSGI
cp %{_builddir}/CGI-Emulate-PSGI-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-CGI-Emulate-PSGI/82717a9c29ee8516411ec4760124809724b76c32 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CGI::Emulate::PSGI.3
/usr/share/man/man3/CGI::Parse::PSGI.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CGI-Emulate-PSGI/82717a9c29ee8516411ec4760124809724b76c32

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
