%define modname	XML-Filter-BufferText
%define modver	1.01

Summary:	Filter to put all characters() in one event
Name:		perl-%{modname}
Version:	%{modver}
Release:	22
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Filter-BufferText
Source0:	https://cpan.metacpan.org/authors/id/R/RB/RBERJON/XML-Filter-BufferText-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:  perl(Test::Simple)
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

