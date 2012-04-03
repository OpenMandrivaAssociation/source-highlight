%define name	source-highlight
%define	version 3.1.6
%define release %mkrel 2

%define major 4
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name
Summary: 	Produces a document with syntax highlighting
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group: 		Development/Other
License: 	GPLv3+
Source: 	ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
URL: 		http://www.gnu.org/software/src-highlite/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	java2html
Obsoletes:	cpp2html
Provides:	java2html
Provides:	cpp2html

BuildRequires:	bison 
BuildRequires:  flex
BuildRequires:  boost-devel
BuildRequires:	ctags help2man
Requires:	ctags help2man

%description
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %libname
Group: System/Libraries
Summary:Produces a document with syntax highlighting

%description -n %libname
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %develname
Group: Development/C
Summary:Produces a document with syntax highlighting
Provides: lib%name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %develname
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n %staticname
Group: Development/C
Summary:Produces a document with syntax highlighting
Provides: lib%name-static-devel = %version-%release
Requires: %develname = %version-%release

%description -n %staticname
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
%configure2_5x --disable-dependency-tracking \
	--with-boost-libdir=%_libdir
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -fr %{buildroot}%{_datadir}/doc/

%post
%_install_info %{name}.info

%postun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc AUTHORS README CREDITS NEWS TODO.txt THANKS
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_sysconfdir}/bash_completion.d/*

%files -n %libname
%defattr (-,root,root)
%_libdir/lib%{name}.so.%{major}*

%files -n %develname
%defattr (-,root,root)
%doc ChangeLog
%_libdir/lib%{name}.so
%_libdir/pkgconfig/*.pc
%_includedir/srchilite/

%files -n %staticname
%defattr (-,root,root)
%_libdir/lib%{name}.a
