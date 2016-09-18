#
# Conditional build:
#
%define		_state		stable
%define		qtver		5.5.1
%define		orgname		kdevelop

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		ka5-kdevelop
Version:	5.0.1
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/kdevelop/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	f7028cb03302ed5e67331319d656003c
URL:		http://www.kdevelop.org/
BuildRequires:	cmake >= 2.8.9
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	ka5-okteta-devel

BuildRequires:	ka5-kdevplatform-devel >= %{version}
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	clang-devel
BuildRequires:	Qt5Help-devel
BuildRequires:	qt5-assistant
BuildRequires:	docbook-dtd45-xml

BuildRequires:	libstdc++-devel >= 3.3
BuildRequires:	pkgconfig
#BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	zlib-devel >= 1.2.0
BuildConflicts:	star
Requires:	libstdc++-gdb
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
#Provides svn ioslave and perl doc ioslave
#Suggests:	kde4-kdesdk-kioslaves >= %{kdever}
#Provides additional project templates
#Suggests:	kde4-kapptemplate >= %{kdever}
#Provides ui viewer
#Suggests:	kde4-kde-dev-utils >= %{kdever}
#Suggests:	kde4-kompare >= %{kdever}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to
programs like gdb, the C/C++ compiler, and make.

KDevelop manages or provides: all development tools needed for C++
programming like Compiler, Linker, automake and autoconf; KAppWizard,
which generates complete, ready-to-go sample applications;
Classgenerator, for creating new classes and integrating them into the
current project; File management for sources, headers, documentation
etc. to be included in the project; The creation of User-Handbooks
written with SGML and the automatic generation of HTML-output with the
KDE look and feel; Automatic HTML-based API-documentation for your
project's classes with cross-references to the used libraries;
Internationalization support for your application, allowing
translators to easily add their target language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%description -l de.UTF-8
KDevelop ist eine grafische Entwicklungsumgebung für KDE.

Das KDevelop-Projekt wurde 1998 begonnen, um eine einfach zu
bedienende grafische (integrierte) Entwicklungsumgebung für C++ und C
auf Unix-basierten Betriebssystemen bereitzustellen. Seit damals ist
die KDevelop-IDE öffentlich unter der GPL erhältlich und unterstützt
u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%description -l pl.UTF-8
KDevelop to zintegrowane środowisko programistyczne dla KDE, dające
wiele możliwości przydatnych programistom oraz zunifikowany interfejs
do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obsługuje lub zawiera: wszystkie narzędzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generujący kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i włączania
ich do projektu; zarządzanie plikami źródłowymi, nagłówkowymi,
dokumentacją itp.; tworzenie podręczników użytkownika pisanych w SGML
i automatyczne generowanie wyjścia HTML pasującego do KDE;
automatyczne tworzenie dokumentacji API w HTML do klas projektu z
odniesieniami do używanych bibliotek; wsparcie dla
internacjonalizacji, pozwalające tłumaczom łatwo dodawać pliki z
tłumaczeniami do projektu.

KDevelop ma także tworzenie interfejsów użytkownika przy użyciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integrację z
KDbg; edycję ikon przy pomocy KIconEdit; dołączanie innych programów
potrzebnych do programowania przez dodanie ich do menu Tools według
własnych potrzeb.

%package devel
Summary:	kdevelop - header files and development documentation
Summary(pl.UTF-8):	kdevelop - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and development documentation for
kdevelop.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevelop.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_mime_database
%update_desktop_database

%postun
/sbin/ldconfig
%update_mime_database
%update_desktop_database_postun

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdevelop
%attr(755,root,root) %{_bindir}/kdevelop!
%attr(755,root,root) %{_bindir}/kdev_includepathsconverter
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/*/kdev*.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krunner_kdevelopsessions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/dataengine/plasma_engine_kdevelopsessions.so
%attr(755,root,root) %{_libdir}/libKDevClangPrivate.so.*
%attr(755,root,root) %{_libdir}/libkdevcmakecommon.so
%{_datadir}/appdata/*
%{_datadir}/doc/HTML/en/kdevelop
%{_datadir}/kdevappwizard
%{_datadir}/kdevclangsupport
%{_datadir}/kdevcodegen/templates/*
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevgdb
%{_datadir}/kdevmanpage
%{_datadir}/kdevqmakebuilder
%{_datadir}/kdevqmljssupport
%{_datadir}/knotifications5/*
%{_datadir}/mime/packages/*
%{_datadir}/kservices5/*
%{_datadir}/plasma/plasmoids/kdevelopsessions
%{_datadir}/plasma/services/org.kde.plasma.dataengine.kdevelopsessions.operations
%{_desktopdir}/org.kde.kdevelop.desktop
%{_desktopdir}/org.kde.kdevelop_ps.desktop
%{_iconsdir}/*/*x*/*/*.png

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KDevelop
%{_includedir}/kdevelop
