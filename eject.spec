Name:		eject
Summary:	A program that ejects removable media using software control
Version:	2.1.5
Release:	%mkrel 10
License:	GPLv2+
Url:		http://ca.geocities.com/jefftranter%40rogers.com/eject.html
Group:		System/Kernel and hardware
Source0:	http://ca.geocities.com/jefftranter%40rogers.com/%{name}-%{version}.tar.gz
Patch1: eject-2.1.4-scsi-rdwr.patch
Patch2: eject-2.0.13-xmalloc.patch
Patch3: eject-2.1.5-handle-spaces.patch
Patch4: eject-2.1.5-man-typo.patch
Patch5: eject-2.1.5-toggle.patch
BuildRequires:	gettext
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The eject program allows the user to eject removable media
(typically CD-ROMs, floppy disks or Iomega Jaz or Zip disks)
using software control. Eject can also control some multi-
disk CD changers and even some devices' auto-eject features.

Install eject if you'd like to eject removable media using
software control.

%prep
%setup -q -n %{name}
%patch1 -p1 -b .scsi
%patch2 -p0 -b .xmalloc
%patch3 -p0
%patch4 -p0
%patch5 -p1

%build
%configure2_5x
%make DEFAULTDEVICE="/dev/cdrom"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO ChangeLog
%{_bindir}/eject
%{_bindir}/volname
%{_mandir}/man1/eject.1*
%{_mandir}/man1/volname.1*

