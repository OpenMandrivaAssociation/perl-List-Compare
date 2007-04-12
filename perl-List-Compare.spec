%define module	List-Compare
%define name	perl-%{module}
%define version 0.33
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Compare elements of two or more lists
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/List/%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch

%description
This module allows to compare elements of two or more lists.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/List
%{_mandir}/*/*


