Name:		eject
Summary:	A program that ejects removable media using software control
Version:	2.1.5
Release:	%mkrel 12
License:	GPLv2+
Url:		https://ca.geocities.com/jefftranter%40rogers.com/eject.html
Group:		System/Kernel and hardware
Source0:	http://ca.geocities.com/jefftranter%40rogers.com/%{name}-%{version}.tar.gz
Patch1: eject-2.1.4-scsi-rdwr.patch
Patch2: eject-2.0.13-xmalloc.patch
Patch3: eject-2.1.5-handle-spaces.patch
Patch4: eject-2.1.5-man-typo.patch
Patch5: eject-2.1.5-toggle.patch
#Patch6:	eject-2.1.5-unlock.patch
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
#patch6 -p1

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-10mdv2011.0
+ Revision: 664130
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-9mdv2011.0
+ Revision: 605099
- rebuild

* Wed Jan 27 2010 Funda Wang <fwang@mandriva.org> 2.1.5-8mdv2010.1
+ Revision: 496907
- sync with gentoo patches (bug#46189)

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix licence

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.5-7mdv2010.0
+ Revision: 424384
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-6mdv2009.1
+ Revision: 318040
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1.5-5mdv2009.0
+ Revision: 220721
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.1.5-4mdv2008.1
+ Revision: 149692
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 26 2007 Adam Williamson <awilliamson@mandriva.org> 2.1.5-3mdv2008.0
+ Revision: 44351
- drop supermount patch as we are dropping supermount, rebuild for 2008


* Wed Aug 30 2006 Helio Chissini de Castro <helio@mandriva.com> 2.1.5-2mdv2007.0
Added gentoo patch for fix the infamous "Safely remove" KDE bug, which indeed
wasn't KDE bug. 
Fix http://qa.mandriva.com/show_bug.cgi?id=23278

* Fri Jul 07 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.1.5-1mdv2007.0
- 2.1.5

* Fri Dec 23 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.1.4-1mdk
- 2.1.4
- update P0

* Mon Oct 17 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.1.3-2mdk
- add BuildRequires: automake1.9

* Fri Oct 14 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.1.3-1mdk
- 2.1.3
- regenerate supermount patch (P0)
- drop old patches (P1-P6)
- %%mkrel

* Fri Dec 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.13-6mdk
- sync with fedora
- cosmetics
- fix summary-ended-with-dot

* Wed Sep 01 2004 Warly <warly@mandrakesoft.com> 2.0.13-5mdk
- rebuild

