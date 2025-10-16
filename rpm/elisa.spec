Name:       elisa
Version:    25.04.3
Release:    1
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
License:    LGPLv3+ and CC-BY-SA
URL:        https://community.kde.org/Elisa
Source0:    %{name}-%{version}.tar.xz
Patch0:     0001-desktop-qtrunner.patch
Patch1:     0002-dont-set-style.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kxmlgui-devel
#BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-kdbusaddons-devel
#BuildRequires:  kf6-kirigami2-devel
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kiconthemes-devel
#BuildRequires:  kf6-kio-widgets-libs
BuildRequires:  kf6-kfilemetadata-devel

Requires:       qt-runner-qt6
#Requires:       kf6-kirigami2
Requires:       kf6-kirigami
Requires:       kf6-kcrash
Requires:       kf6-kiconthemes
Requires:       kf6-kio-widgets-libs
Requires:       kf6-kfilemetadata
Requires:       kf6-kdbusaddons
Requires:       kf6-kxmlgui
Requires:       kf6-kio-file-widgets
Requires:       kf6-kio-gui

%global __requires_exclude ^libelisaLib.*$|

%description
Elisa is a simple music player aiming to provide a nice experience for its
users.
%if 0%{?_chum}
PackageName: Elisa
Type: desktop-application
DeveloperName: KDE Project
PackagerName: Adam Pigg
Categories:
 - Audio
Custom:
  Repo: https://invent.kde.org/multimedia/elisa
  PackagingRepo: https://github.com/sailfishos-chum/elisa
Icon: https://raw.githubusercontent.com/sailfishos-chum/elisa/main/logo.png
Screenshots:
 - https://raw.githubusercontent.com/sailfishos-chum/elisa/main/screenshot-1.png
 - https://raw.githubusercontent.com/sailfishos-chum/elisa/main/screenshot-2.png
 - https://raw.githubusercontent.com/sailfishos-chum/elisa/main/screenshot-3.png
%endif

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/elisa
%{_datadir}/applications/org.kde.elisa.desktop
%{_datadir}/dbus-1/services/org.kde.elisa.service
%{_datadir}/icons/hicolor/*/apps/elisa*
%{_datadir}/qlogging-categories6/elisa.categories
%exclude %{_kf6_metainfodir}/org.kde.elisa.appdata.xml
%{_qt6_libdir}/elisa/
#%%{_qt6_libdir}/qt6/qml/org/kde/elisa/
#%%{_datadir}/locale/
