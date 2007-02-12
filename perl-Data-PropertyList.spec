#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Data
%define		pnam	PropertyList
Summary:	Data::PropertyList - convert arbitrary objects to/from strings
Summary(pl.UTF-8):   Data::PropertyList - konwersja dowolnych obiektów do/z łańcuchów tekstowych
Name:		perl-Data-PropertyList
Version:	1998.1217
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d685c3ae087d1e55d4b0adc0dd4c2108
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-String-Escape
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Propertylist Perl module provides functions that turn data
structures with nested references into NeXT's Property List text
format and back again.

You may find this useful for saving and loading application
information in text files, or perhaps for generating error messages
while debugging.

%description -l pl.UTF-8
Moduł Perla Data::PropertyList udostępnia funkcje przekształcającą
struktury z zagnieżdżonymi wskaźnikami do formatu tekstowego NeXT's
Property List i z powrotem.

Jest on przydatny do zachowywania informacji z aplikacji w pliku
tekstowym i jej odczytywania z pliku. Przydaje się też do generowania
komunikatów o błędach podczas odpluskwiania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/PropertyList.pm
%{_mandir}/man3/*
