%define		_src_name	xfce4-panel-menu-plugin
Summary:	WinXP like menu for Xfce4-panel
Summary(pl):	Menu dla Xfce4 w stylu WinXP
Name:		xfce4-panelmenu-plugin
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce4panelmenu/%{_src_name}-%{version}.tar.gz
# Source0-md5:	b5f1cefc709584435ebccb52376175d7
URL:		https://developer.berlios.de/projects/xfce4panelmenu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbh-devel >= 1.0
BuildRequires:	libxfce4mcs-devel >= 4.2.0
BuildRequires:	xfce4-panel-devel >= 4.2.0
Requires:	xfce4-panel >= 4.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-panelmenu-plugin is a Xfce panel plugin that provides a menu
similar to this at WinXP.

%description -l pl
xfce4-panelmenu-plugin jest wtyczk± dla panelu Xfce, która dostarcza
menu podobne do tego z WinXP.

%prep
%setup -q -n %{_src_name}-%{version}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/menustart/*
