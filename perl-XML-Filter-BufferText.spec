%define modname	XML-Filter-BufferText
%define modver	1.01

Summary:	Filter to put all characters() in one event
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX)

%description
This is a very simple filter. One common cause of grief (and programmer error)
is that XML parsers aren't required to provide character events in one chunk.
They can, but are not forced to, and most don't. This filter does the trivial
but oft-repeated task of putting all characters into a single event.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 BufferText.pm Changes README

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3/*

