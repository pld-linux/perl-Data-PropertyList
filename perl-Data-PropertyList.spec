%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Data-PropertyList perl module
Summary(pl):	Modu� perla Data-PropertyList
Name:		perl-Data-PropertyList
Version:	1998.1217
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/Data-PropertyList-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-String-Escape
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-String-Escape
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Data-PropertyList - Convert arbitrary objects to/from strings.

%description -l pl
Modu� perla Data-PropertyList.

%prep
%setup -q -n Data-PropertyList-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Data/PropertyList
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Data/PropertyList.pm
%{perl_sitearch}/auto/Data/PropertyList

%{_mandir}/man3/*
