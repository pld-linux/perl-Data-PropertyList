%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	PropertyList
Summary:	Data::PropertyList - convert arbitrary objects to/from strings
Summary(pl):	Data::PropertyList - konwersja dowolnych obiektów do/z ³añcuchów tekstowych
Name:		perl-Data-PropertyList
Version:	1998.1217
Release:	9
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d685c3ae087d1e55d4b0adc0dd4c2108
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ perla Data::PropertyList udostêpnia funkcje przekszta³caj±c±
struktury z zagnie¿d¿onymi wska¼nikami do formatu tekstowego NeXT's
Property List i z powrotem.

Jest on przydatny do zachowywania informacji z aplikacji w pliku
tekstowym i jej odczytywania z pliku. Przydaje siê te¿ do generowania
komunikatów o b³êdach podczas odpluskwiania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/PropertyList.pm
%{_mandir}/man3/*
