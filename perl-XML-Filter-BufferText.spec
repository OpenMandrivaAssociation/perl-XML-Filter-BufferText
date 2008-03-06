%define module  XML-Filter-BufferText
%define name    perl-%{module}
%define version 1.01
%define release %mkrel 9

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Filter to put all characters() in one event
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(XML::SAX)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is a very simple filter. One common cause of grief (and programmer error)
is that XML parsers aren't required to provide character events in one chunk.
They can, but are not forced to, and most don't. This filter does the trivial
but oft-repeated task of putting all characters into a single event.

%prep
%setup -q -n %{module}-%{version}
chmod 644 BufferText.pm Changes README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/*/*

