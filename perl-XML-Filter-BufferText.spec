%define upstream_name    XML-Filter-BufferText
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Filter to put all characters() in one event
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::SAX)
BuildArch:	noarch

%description
This is a very simple filter. One common cause of grief (and programmer error)
is that XML parsers aren't required to provide character events in one chunk.
They can, but are not forced to, and most don't. This filter does the trivial
but oft-repeated task of putting all characters into a single event.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 BufferText.pm Changes README

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-5mdv2012.0
+ Revision: 765840
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-4
+ Revision: 764336
- rebuilt for perl-5.14.x

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-3
+ Revision: 763378
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-2
+ Revision: 667417
- mass rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 401863
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.01-10mdv2009.0
+ Revision: 224617
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.01-9mdv2008.1
+ Revision: 180653
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 23 2007 Anne Nicolas <ennael@mandriva.org> 1.01-8mdv2008.0
+ Revision: 92388
- bump release (oden)

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-7mdv2008.0
+ Revision: 87099
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-6mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-5mdk
- Fix According to perl Policy
    - BuildRequires
    - Source URL

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-4mdk
- Fix BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.01-3mdk
- Fix BuildRequires

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-2mdk 
- spec cleanup
- don't ship useless empty directories
- make test in %%check

* Mon Jan 17 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.01-1mdk 
- first mdk release

