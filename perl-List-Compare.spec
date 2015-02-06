%define upstream_name	 List-Compare
%define upstream_version 0.38

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Compare elements of two or more lists
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/List/List-Compare-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::CaptureOutput)
BuildArch:	noarch

%description
This module allows to compare elements of two or more lists.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files 
%doc Changes README
%{perl_vendorlib}/List
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2010.0
+ Revision: 402573
- update to 0.56

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.37-2mdv2009.0
+ Revision: 268539
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.0
+ Revision: 217098
- update to new version 0.37

* Sun May 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.0
+ Revision: 211161
- update to new version 0.36

* Thu May 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.0
+ Revision: 210022
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2008.1
+ Revision: 106566
- update to new version 0.34
- update to new version 0.34


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-2mdv2007.0
+ Revision: 134299
- rebuild

* Wed Mar 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdk
- New release 0.33

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdk
- New release 0.32

* Sun Jun 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-3mdk 
- spec cleanup
- don't ship useless empty dirs
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.31-2mdk
- fix buildrequires in a backward compatible way

* Tue Oct 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.31-1mdk
- 0.31

* Thu Jun 10 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3-1mdk 
- first mdk release


