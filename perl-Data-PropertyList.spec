%include	/usr/lib/rpm/macros.perl
Summary:	Data-PropertyList perl module
Summary(pl):	Modu� perla Data-PropertyList
Name:		perl-Data-PropertyList
Version:	1998.1217
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-PropertyList-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-String-Escape
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data-PropertyList - Convert arbitrary objects to/from strings.

%description -l pl
Modu� perla Data-PropertyList.

%prep
%setup -q -n Data-PropertyList-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Data/PropertyList.pm
%{_mandir}/man3/*
