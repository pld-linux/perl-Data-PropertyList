%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	PropertyList
Summary:	Data::PropertyList perl module
Summary(pl):	Modu³ perla Data::PropertyList
Name:		perl-Data-PropertyList
Version:	1998.1217
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-String-Escape
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::PropertyList - Convert arbitrary objects to/from strings.

%description -l pl
Modu³ perla Data::PropertyList.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Data/PropertyList.pm
%{_mandir}/man3/*
