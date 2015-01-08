%define _buildid .1

Name:           perl-MySQL-Config
Version:        1.04
Release:        1%{?_buildid}%{?dist}
Summary:        Parse and utilize MySQL's /etc/my.cnf and ~/.my.cnf files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MySQL-Config/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DA/DARREN/MySQL-Config-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Parse and utilize MySQL's /etc/my.cnf and ~/.my.cnf files

%prep
%setup -q -n MySQL-Config-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jan 08 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 1.04-1
- Add initial spec file
