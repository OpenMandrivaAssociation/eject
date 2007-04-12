%define	name	eject
%define	version	2.1.5
%define	release	2

Name:		%{name}
Summary:	A program that ejects removable media using software control
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Url:		http://ca.geocities.com/jefftranter%40rogers.com/eject.html
Group:		System/Kernel and hardware
Source0:	http://ca.geocities.com/jefftranter%40rogers.com/%{name}-%{version}.tar.gz
Patch0: eject-2.1.4-supermount.patch
Patch1: eject-2.1.4-scsi-rdwr.patch
BuildRequires:	gettext
BuildRequires:	automake1.9
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
%patch0 -p1 -b .supermount
%patch1 -p1 -b .scsi

%build
%configure
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

