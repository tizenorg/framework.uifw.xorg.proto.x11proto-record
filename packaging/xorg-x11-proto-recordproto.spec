
Name:       xorg-x11-proto-recordproto
Summary:    X.Org X11 Protocol recordproto
Version:    1.14.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/recordproto-%{version}.tar.gz
Provides:   recordproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build

%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}




%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/recordproto.pc
%{_includedir}/X11/extensions/recordstr.h
%{_includedir}/X11/extensions/recordconst.h
%{_includedir}/X11/extensions/recordproto.h
%{_docdir}/recordproto


