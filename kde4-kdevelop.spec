#
# Conditional build:
#
%define		_state		unstable
%define		_kdever		4.2.0
%define		_qtver		4.4
%define		svnrev		1027000
%define		orgname		kdevelop

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		kde4-kdevelop
Version:	3.9.95
Release:	0.%{svnrev}.1
License:	GPL
Group:		X11/Development/Tools
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/KDE/kdevelop
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{version}/src/%{orgname}-%{version}.tar.bz2
Source0:	%{orgname}-%{version}-%{svnrev}.tar.bz2
# Source0-md5:	1949513701e452768ab5a1a6f44c4f90
URL:		http://www.kdevelop.org/
BuildRequires:	cmake >= 2.6.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	kde4-kdevplatform-devel >= 0.9.95
BuildRequires:	QtCore-devel >= %{_qtver}
BuildRequires:	QtDBus-devel >= %{_qtver}
BuildRequires:	QtDesigner-devel >= %{_qtver}
BuildRequires:	QtGui-devel >= %{_qtver}
BuildRequires:	QtNetwork-devel >= %{_qtver}
BuildRequires:	QtScript-devel >= %{_qtver}
BuildRequires:	QtTest-devel >= %{_qtver}
BuildRequires:	QtSvg-devel >= %{_qtver}
BuildRequires:	Qt3Support-devel >= %{_qtver}
BuildRequires:	perl-base >= 5.8
BuildRequires:	zlib-devel >= 1.2.0
BuildRequires:	libstdc++-devel >= 3.3
BuildRequires:	gcc-c++ >= 3.3
BuildConflicts:	star
Requires:	kde4-kdebase >= %{_kdever}
Requires:	kde4-kdelibs >= %{_kdever}
Requires:	QtCore >= %{_qtver}
Requires:	QtDBus >= %{_qtver}
Requires:	QtDesigner >= %{_qtver}
Requires:	QtGui >= %{_qtver}
Requires:	QtNetwork >= %{_qtver}
Requires:	QtScript >= %{_qtver}
Requires:	glibc
Requires:	libgcc
Requires:	kde4-kdevplatform >= 0.9.93
Requires:	libstdc++ >= 3.3
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
bedienende grafische (integrierte Entwicklungsumgebung) für C++ und C
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

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install app/kdevelop.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kdev_includepathresolver
%attr(755,root,root) %{_bindir}/kdevelop
#%attr(755,root,root) %{_bindir}/lcov_geninfo
#%attr(755,root,root) %{_bindir}/qmake-parser
#%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_cppdebugger.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_lcovsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_makebuilder.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_qmakebuilder.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_valgrindsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_veritassettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevcmake_settings.so
%attr(755,root,root) %{_libdir}/kde4/kdevastyle.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakebuilder.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakedocumentation.so
%attr(755,root,root) %{_libdir}/kde4/kdevcmakemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevcoverage.so
#%attr(755,root,root) %{_libdir}/kde4/kdevcppdebugger.so
%attr(755,root,root) %{_libdir}/kde4/kdevcpplanguagesupport.so
%attr(755,root,root) %{_libdir}/kde4/kdevcustommakemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentview.so
%attr(755,root,root) %{_libdir}/kde4/kdevgdb.so
%attr(755,root,root) %{_libdir}/kde4/kdevgrepview.so
%attr(755,root,root) %{_libdir}/kde4/kdevindent.so
%attr(755,root,root) %{_libdir}/kde4/kdevmakebuilder.so
#%attr(755,root,root) %{_libdir}/kde4/kdevqmakebuilder.so
#%attr(755,root,root) %{_libdir}/kde4/kdevqmakemanager.so
#%attr(755,root,root) %{_libdir}/kde4/kdevqtdesigner.so
%attr(755,root,root) %{_libdir}/kde4/kdevqtestview.so
%attr(755,root,root) %{_libdir}/kde4/kdevqthelp.so
%attr(755,root,root) %{_libdir}/kde4/kdevvalgrind.so
%attr(755,root,root) %{_libdir}/libkdev4cmakecommon.so
%attr(755,root,root) %{_libdir}/libkdev4cppduchain.so
%attr(755,root,root) %{_libdir}/libkdev4cppparser.so
%attr(755,root,root) %{_libdir}/libkdev4cpprpp.so
#%attr(755,root,root) %{_libdir}/libkdev4qmakeparser.so
#%attr(755,root,root) %{_libdir}/libkdev4qmakeduchain.so
%attr(755,root,root) %{_libdir}/libkdevqtest.so
%attr(755,root,root) %{_libdir}/libkdevveritascoverage.so
%attr(755,root,root) %{_libdir}/libveritascpp.so
%{_desktopdir}/kdevelop.desktop

%{_datadir}/apps/cmake/modules/FindKDevelop.cmake
#%{_datadir}/apps/cmake/modules/KDevelopMacros.cmake
%{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevcmakebuilder
%{_datadir}/apps/kdevcmakemanager
#%{_datadir}/apps/kdevcppdebugger
%{_datadir}/apps/kdevcustommakemanager
%{_datadir}/apps/kdevdocumentview
%{_datadir}/apps/kdevelop
%dir %{_datadir}/apps/kdevgdb
%{_datadir}/apps/kdevgdb/kdevgdbui.rc
%dir %{_datadir}/apps/kdevgdb/printers
%{_datadir}/apps/kdevgdb/printers/gdbinit
%{_datadir}/apps/kdevgdb/printers/qt4.py
%{_datadir}/apps/kdevgrepview
#%{_datadir}/apps/kdevqmakebuilder
#%{_datadir}/apps/kdevqtdesigner
%{_datadir}/apps/kdevvalgrind
%{_datadir}/config/kdeveloprc
%dir %{_datadir}/apps/kdevcppsupport
%{_datadir}/apps/kdevcppsupport/kdevcppsupport.rc
%dir %{_datadir}/apps/kdevcoverage
%{_datadir}/apps/kdevcoverage/kdevcoverage.rc
%dir %{_datadir}/apps/kdevqtest
%{_datadir}/apps/kdevqtest/kdevqtest.rc

%{_iconsdir}/*/*x*/*/*.png
#%{_datadir}/kde4/services/kcm_kdev_cppdebugger.desktop
%{_datadir}/kde4/services/kcm_kdev_lcovsettings.desktop
%{_datadir}/kde4/services/kcm_kdev_makebuilder.desktop
#%{_datadir}/kde4/services/kcm_kdev_qmakebuilder.desktop
#%{_datadir}/kde4/services/kcm_kdev_valgrindsettings.desktop
%{_datadir}/kde4/services/kcm_kdev_veritassettings.desktop
%{_datadir}/kde4/services/kcm_kdevcmake_settings.desktop
%{_datadir}/kde4/services/kdevastyle.desktop
%{_datadir}/kde4/services/kdevcmakebuilder.desktop
%{_datadir}/kde4/services/kdevcmakedocumentation.desktop
%{_datadir}/kde4/services/kdevcmakemanager.desktop
%{_datadir}/kde4/services/kdevcoverage.desktop
#%{_datadir}/kde4/services/kdevcppdebugger.desktop
%{_datadir}/kde4/services/kdevcppsupport.desktop
%{_datadir}/kde4/services/kdevcustommakemanager.desktop
%{_datadir}/kde4/services/kdevdocumentview.desktop
%{_datadir}/kde4/services/kdevgdb.desktop
%{_datadir}/kde4/services/kdevgrepview.desktop
%{_datadir}/kde4/services/kdevindent.desktop
%{_datadir}/kde4/services/kdevmakebuilder.desktop
#%{_datadir}/kde4/services/kdevqmakebuilder.desktop
#%{_datadir}/kde4/services/kdevqmakemanager.desktop
#%{_datadir}/kde4/services/kdevqtdesigner.desktop
%{_datadir}/kde4/services/kdevqtest.desktop
%{_datadir}/kde4/services/kdevqthelp.desktop
%{_datadir}/kde4/services/kdevvalgrind.desktop
%{_datadir}/applications/kde4/kdevelop.desktop

%{_includedir}/kdevelop
