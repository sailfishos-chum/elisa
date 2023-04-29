Name:       elisa
Version:    23.04.0
Release:    1
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
License:    LGPLv3+ and CC-BY-SA
URL:        https://community.kde.org/Elisa
Source0:    %{name}-%{version}.tar.xz
Patch0:     0001-desktop-qtrunner.patch
Patch1:     0002-use-breeze-style.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
BuildRequires:  opt-qt5-qtmultimedia-devel
BuildRequires:  opt-qt5-qtsvg-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kconfig-devel
BuildRequires:  opt-kf5-kio-devel
BuildRequires:  opt-kf5-kcoreaddons-devel
BuildRequires:  opt-kf5-kxmlgui-devel
BuildRequires:  opt-kf5-kcrash-devel
BuildRequires:  opt-kf5-kdbusaddons-devel
BuildRequires:  opt-kf5-kirigami2-devel
BuildRequires:  opt-kf5-kconfigwidgets-devel
BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-kf5-kiconthemes-devel
BuildRequires:  opt-kf5-kio-widgets-libs
BuildRequires:  opt-kf5-kfilemetadata-devel

Requires:       qt-runner
Requires:       opt-kf5-kirigami2
Requires:       opt-kf5-kcrash
Requires:       opt-kf5-kiconthemes
Requires:       opt-kf5-kio-widgets-libs
Requires:       opt-kf5-kfilemetadata
Requires:       opt-kf5-kdbusaddons
Requires:       opt-kf5-kxmlgui
Requires:       opt-kf5-kio-file-widgets
Requires:       opt-kf5-kio-gui

%global __requires_exclude ^libelisaLib.*$|
%{?opt_kf5_default_filter}

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
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
		-DKDE_INSTALL_BINDIR:PATH=/usr/bin \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr/
%make_build
popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%files
%license COPYING
%{_bindir}/elisa
%{_datadir}/applications/org.kde.elisa.desktop
%{_datadir}/dbus-1/services/org.kde.elisa.service
%{_datadir}/icons/hicolor/*/apps/elisa*
%{_datadir}/qlogging-categories5/elisa.categories
%{_opt_kf5_metainfodir}/org.kde.elisa.appdata.xml
%{_opt_qt5_libdir}/elisa/
%{_opt_qt5_libdir}/qt5/qml/org/kde/elisa/
%{_datadir}/locale/
