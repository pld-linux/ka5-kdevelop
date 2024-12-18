#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	webengine	# build without webengine

%define		kdeappsver	23.08.5
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdevelop

%ifarch x32
%undefine with_webengine
%endif

Summary:	KDE Integrated Development Environment
Summary(de.UTF-8):	KDevelop ist eine grafische Entwicklungsumgebung für KDE
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE
Summary(pt_BR.UTF-8):	Ambiente Integrado de Desenvolvimento para o KDE
Summary(zh_CN.UTF-8):	KDE C/C++集成开发环境
Name:		ka5-kdevelop
Version:	23.08.5
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e643b040806cb4547f104950bde6b5f2
URL:		http://www.kdevelop.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Help-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
%{?with_webengine:BuildRequires:	Qt5WebEngine-devel >= %{qtver}}
BuildRequires:	astyle-devel >= 3.1
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	clang-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	grantlee-qt5-devel
BuildRequires:	ka5-kdevelop-pg-qt
BuildRequires:	ka5-libkomparediff2-devel >= 5.4.0
BuildRequires:	ka5-okteta-devel >= 1:0.26.9-3
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemmodels-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-krunner-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-plasma-framework-devel >= %{kframever}
BuildRequires:	kf5-purpose-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	kf5-threadweaver-devel >= %{kframever}
BuildRequires:	kp5-libksysguard-devel
BuildRequires:	libstdc++-devel >= 3.3
BuildRequires:	llvm-mlir-devel
BuildRequires:	meson >= 0.51
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-assistant >= %{qtver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info >= 1.9
BuildRequires:	subversion-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.0
BuildConflicts:	star
Requires:	%{name}-data = %{version}-%{release}
Requires:	libstdc++-gdb
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles .*\\.zshrc

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
die KDevelop-IDE öffentlich unter der GPL erhältlich und
unterstützt u. a. Qt-, KDE-, GNOME-, C++- und C-Projekte.

%description -l pl.UTF-8
KDevelop to zintegrowane środowisko programistyczne dla KDE, dające
wiele możliwości przydatnych programistom oraz zunifikowany
interfejs do programów typu gdb, kompilator C/C++ oraz make.

KDevelop obsługuje lub zawiera: wszystkie narzędzia programistyczne
potrzebne do programowania w C++ jak kompilator, linker, automake,
autoconf; KAppWizard, generujący kompletne, gotowe do uruchomienia,
proste aplikacje; Classgenerator do tworzenia nowych klas i
włączania ich do projektu; zarządzanie plikami źródłowymi,
nagłówkowymi, dokumentacją itp.; tworzenie podręczników
użytkownika pisanych w SGML i automatyczne generowanie wyjścia HTML
pasującego do KDE; automatyczne tworzenie dokumentacji API w HTML do
klas projektu z odniesieniami do używanych bibliotek; wsparcie dla
internacjonalizacji, pozwalające tłumaczom łatwo dodawać pliki z
tłumaczeniami do projektu.

KDevelop ma także tworzenie interfejsów użytkownika przy użyciu
edytora dialogów WYSIWYG; odpluskwianie aplikacji poprzez integrację
z KDbg; edycję ikon przy pomocy KIconEdit; dołączanie innych
programów potrzebnych do programowania przez dodanie ich do menu
Tools według własnych potrzeb.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Development/Tools
Requires:	filesystem >= 4.1-18
Obsoletes:	bash-completion-kdevelop <= 23.08.4-1
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

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
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DFORCE_BASH_COMPLETION_INSTALLATION=ON \
	-DCppcheck_EXECUTABLE:PATH=/usr/bin/cppcheck \
	-DClangTidy_EXECUTABLE:PATH=/usr/bin/clang-tidy
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

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

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdevelop
%attr(755,root,root) %{_bindir}/kdevelop!
%attr(755,root,root) %{_bindir}/kdev_includepathsconverter
%attr(755,root,root) %{_libdir}/libKDevClangPrivate.so.*
%attr(755,root,root) %{_libdir}/libKDevCMakeCommon.so.*
%attr(755,root,root) %{_libdir}/libKDevCompileAnalyzerCommon.so.*
%attr(755,root,root) %{_libdir}/libKDevelopSessionsWatch.so
%dir %{_libdir}/qt5/plugins/kf5/krunner
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/krunner/krunner_kdevelopsessions.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/kdevelopsessions
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/private/kdevelopsessions/libkdevelopsessionsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/kdevelopsessions/qmldir

#kdevplatform
%attr(755,root,root) %{_bindir}/kdev_dbus_socket_transformer
%attr(755,root,root) %{_bindir}/kdev_format_source
%attr(755,root,root) %{_bindir}/kdevplatform_shell_environment.sh
%attr(755,root,root) %{_libdir}/libKDevPlatformDebugger.so.*.*.*
%ghost %{_libdir}/libKDevPlatformDebugger.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformDocumentation.so.*.*.*
%ghost %{_libdir}/libKDevPlatformDocumentation.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformInterfaces.so.*.*.*
%ghost %{_libdir}/libKDevPlatformInterfaces.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformLanguage.so.*.*.*
%ghost %{_libdir}/libKDevPlatformLanguage.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformOutputView.so.*.*.*
%ghost %{_libdir}/libKDevPlatformOutputView.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformProject.so.*.*.*
%ghost %{_libdir}/libKDevPlatformProject.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformSerialization.so.*.*.*
%ghost %{_libdir}/libKDevPlatformSerialization.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformShell.so.*.*.*
%ghost %{_libdir}/libKDevPlatformShell.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformSublime.so.*.*.*
%ghost %{_libdir}/libKDevPlatformSublime.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformUtil.so.*.*.*
%ghost %{_libdir}/libKDevPlatformUtil.so.???
%attr(755,root,root) %{_libdir}/libKDevPlatformVcs.so.*.*.*
%ghost %{_libdir}/libKDevPlatformVcs.so.???
%dir %{_libdir}/qt5/plugins/grantlee
%dir %{_libdir}/qt5/plugins/grantlee/5.3
%attr(755,root,root) %{_libdir}/qt5/plugins/grantlee/*/kdev_filters.so
%dir %{_libdir}/qt5/plugins/kdevplatform
%dir %{_libdir}/qt5/plugins/kdevplatform/51?
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/*/kdev*.so

%{_libdir}/qt5/qml/org/kde/kdevplatform/qmldir
%dir %{_libdir}/qt5/qml/org/kde/kdevplatform
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so

%files data
%defattr(644,root,root,755)
%{bash_compdir}/kdevelop
%dir %{_datadir}/kdevplatform
%dir %{_datadir}/kdevplatform/shellutils
%{_datadir}/kdevplatform/shellutils/.zshrc
%{_datadir}/kdevappwizard
%{_datadir}/kdevclangsupport
%{_datadir}/kdevelop
%{_datadir}/kdevfiletemplates
%{_datadir}/kdevgdb
%{_datadir}/kdevlldb
%{_datadir}/kdevmanpage
%{_datadir}/kdevqmljssupport
%{_datadir}/knotifications5/*
%{_datadir}/knsrcfiles/kdev*.knsrc
%{_datadir}/metainfo/*
%{_datadir}/mime/packages/*
%{_datadir}/kservices5/*
%{_datadir}/plasma/plasmoids/kdevelopsessions
%{_desktopdir}/org.kde.kdevelop.desktop
%{_desktopdir}/org.kde.kdevelop_*.desktop
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/qlogging-categories5/kdev*.categories
%{_datadir}/kdevcodegen
%{_datadir}/kdevcodeutils
%{_datadir}/kservicetypes5/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.svg
%{_iconsdir}/hicolor/*/apps/*.svg

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KDevelop
%{_includedir}/kdevelop

#kdevplatform
%{_includedir}/kdevplatform
%{_libdir}/libKDevPlatformDebugger.so
%{_libdir}/libKDevPlatformDocumentation.so
%{_libdir}/libKDevPlatformInterfaces.so
%{_libdir}/libKDevPlatformLanguage.so
%{_libdir}/libKDevPlatformOutputView.so
%{_libdir}/libKDevPlatformProject.so
%{_libdir}/libKDevPlatformSerialization.so
%{_libdir}/libKDevPlatformShell.so
%{_libdir}/libKDevPlatformSublime.so
%{_libdir}/libKDevPlatformUtil.so
%{_libdir}/libKDevPlatformVcs.so
%dir %{_libdir}/cmake/KDevPlatform
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfig.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformConfigVersion.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformMacros.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets.cmake
%{_libdir}/cmake/KDevPlatform/KDevPlatformTargets-pld.cmake
