%define major 4
%define libname %mklibname %{name} %major
%define devname %mklibname -d %{name}
%define static %mklibname -s -d %{name}

Summary:	Produces a document with syntax highlighting
Name:		source-highlight
Version:	3.1.9
Release:	3
Group:		Development/Other
License:	GPLv3+
Source0:	ftp://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/src-highlite/
%rename		java2html
%rename		cpp2html

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	boost-devel >= 1.73.0-0
BuildRequires:	boost-core-devel
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

%package -n	%{libname}
Group:		System/Libraries
Summary:	Produces a document with syntax highlighting

%description -n	%{libname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n	%{devname}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%package -n	%{static}
Group:		Development/C
Summary:	Produces a document with syntax highlighting
Provides:	lib%{name}-static-devel = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n	%{static}
GNU Source-highlight produces a document with syntax highlighting
when given a source file. It handles many languages, e.g., Java,
C/C++, Prolog, Perl, PHP3, Python, Flex, HTML, and other formats,
e.g., ChangeLog and log files, as source languages and HTML, XHTML,
DocBook, ANSI color escapes, LaTeX, and Texinfo as output formats.
Input and output formats can be specified with a regular expression-
oriented syntax.

%prep
%autosetup -p1

%build
%configure \
		--with-boost-libdir=%{_libdir} \
		--enable-static

%make_build

%install
%make_install

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

%files -n %{devname}
%doc ChangeLog
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/srchilite/

%files -n %{static}
%{_libdir}/lib%{name}.a
