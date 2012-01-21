%define upstream_name    XML-Filter-BufferText
%define upstream_version 1.01

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 4

Summary:        Filter to put all characters() in one event
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(XML::SAX)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a very simple filter. One common cause of grief (and programmer error)
is that XML parsers aren't required to provide character events in one chunk.
They can, but are not forced to, and most don't. This filter does the trivial
but oft-repeated task of putting all characters into a single event.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
