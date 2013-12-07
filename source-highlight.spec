%define major 4
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary:	Produces a document with syntax highlighting
Name:		source-highlight
Version:	3.1.7
Release:	5
Group:		Development/Other
License:	GPLv3+
Source:		ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/src-highlite/
%rename	java2html
%rename cpp2html

BuildRequires:	bison 
BuildRequires:	flex
BuildRequires:	boost-devel
BuildRequires:	ctags
BuildRequires:	help2man
Requires:	ctags
Requires:	help2man

%description
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{libname}
Group:		System/Libraries
Summary:	Produces a document with syntax highlighting

%description -n %{libname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{develname}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %{staticname}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	lib%name-static-devel = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%prep
%setup -q

%build
%configure2_5x \
	--disable-dependency-tracking \
	--with-boost-libdir=%{_libdir}

%make

%install
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc/

%files
%doc AUTHORS README CREDITS NEWS TODO.txt THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_sysconfdir}/bash_completion.d/*

%files -n %{libname}
%_libdir/lib%{name}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%_libdir/lib%{name}.so
%_libdir/pkgconfig/*.pc
%_includedir/srchilite/

%files -n %{staticname}
%_libdir/lib%{name}.a


%changelog
* Mon Jul 02 2012 Crispin Boylan <crisb@mandriva.org> 3.1.6-3
+ Revision: 807853
- Rebuild for new boost

* Tue Apr 03 2012 Crispin Boylan <crisb@mandriva.org> 3.1.6-2
+ Revision: 789038
- Rebuild for new boost

* Wed Dec 28 2011 Götz Waschk <waschk@mandriva.org> 3.1.6-1
+ Revision: 746179
- new version
- remove libtool archive

* Sat Sep 03 2011 Götz Waschk <waschk@mandriva.org> 3.1.5-1
+ Revision: 698174
- update file list
- new major
- new version

* Mon May 30 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.1.4-1
+ Revision: 681869
- update to 3.1.4

* Tue Mar 15 2011 Funda Wang <fwang@mandriva.org> 3.1.3-5
+ Revision: 644921
- rebuild for new boost

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 3.1.3-4mdv2011.0
+ Revision: 572621
- rebuild

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 3.1.3-3mdv2011.0
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 3.1.3-2mdv2010.1
+ Revision: 500055
- rebuild for new boost

* Sat Jan 16 2010 Götz Waschk <waschk@mandriva.org> 3.1.3-1mdv2010.1
+ Revision: 492493
- update to new version 3.1.3

* Wed Dec 23 2009 Götz Waschk <waschk@mandriva.org> 3.1.2-1mdv2010.1
+ Revision: 481912
- new version
- add library package

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.11.1-2mdv2009.1
+ Revision: 358058
- rebuild for latest libboost

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 2.11.1-1mdv2009.1
+ Revision: 319341
- new version 2.11.1

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 2.11-2mdv2009.1
+ Revision: 316580
- rebuild for new boost

* Tue Dec 02 2008 Funda Wang <fwang@mandriva.org> 2.11-1mdv2009.1
+ Revision: 308976
- specify boost libdir
- fix file list
- new version 2.11

* Thu Oct 23 2008 Götz Waschk <waschk@mandriva.org> 2.10-2mdv2009.1
+ Revision: 296737
- fix build
- rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - rebuild against new boost

* Tue Jul 22 2008 Funda Wang <fwang@mandriva.org> 2.10-1mdv2009.0
+ Revision: 239935
- update to new version 2.10

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 2.9-1mdv2009.0
+ Revision: 196718
- New version 2.9

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 2.8-2mdv2008.1
+ Revision: 106331
- Rebuild against new boost

* Mon Oct 15 2007 Funda Wang <fwang@mandriva.org> 2.8-1mdv2008.1
+ Revision: 98365
- New version 2.8

* Sun Jun 24 2007 Funda Wang <fwang@mandriva.org> 2.7-1mdv2008.0
+ Revision: 43565
- New version

