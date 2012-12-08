%define name indexhtml
%define version 2012.1
%define release %mkrel 1

Summary:	ROSA Linux html welcome page
Name:		%{name}
Version:	%{version}
Release: 	%{release}
URL:		http://wike.rosalinux.ru
Requires(pre):	mandriva-release-common
Requires(post): gawk coreutils sed
BuildRequires:  intltool
Source:		indexhtml-%{version}.tar.bz2
Provides:	indexhtml
Group:		System/Base
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

Obsoletes: %name = 2012lts

%description
ROSA Linux index.html welcome page displayed by web browsers
when they are launched, first mail displayed on mail clients
after installation and "about" information.

%prep

%setup -q -n  indexhtml-%version

%build
cd about
./create_html.sh

%install
rm -fr %buildroot/

find $RPM_BUILD_DIR/%name -name ".svn" -print | xargs /bin/rm -fr

install -d -m 0755 %buildroot/%_datadir/mdk/indexhtml/
tar c -C HTML . | tar x -C %buildroot/%_datadir/mdk/indexhtml/

install -d -m 0755 %buildroot/%_datadir/doc/HTML/
install -m 0644 HTML/index.html %buildroot/%_datadir/doc/HTML/index.html

#use for default
cp -rf %buildroot/%_datadir/mdk/indexhtml/* %buildroot/%_datadir/doc/HTML/

# about Mandriva
install -d -m 0755 %buildroot/%_datadir/mdk/about
install -d -m 0755 %buildroot/%_datadir/applications
install -d -m 0755 %buildroot/%{_bindir}
cp about/html/* %buildroot/%_datadir/mdk/about
cp -r about/style %buildroot/%_datadir/mdk/about/
cp about/about-mandriva.desktop %buildroot/%_datadir/applications
cp about/about-mandriva %buildroot/%{_bindir}

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,-)
%_datadir/mdk/
%_datadir/doc/HTML/
#/etc/sysconfig/network-scripts/ifup.d/indexhtml
%_datadir/applications/about-mandriva.desktop
%{_bindir}/about-mandriva


%changelog
* Mon Jan 31 2011 Belov Denis <denis.belov@rosalab.ru> 2010.1-3
- Rename package
- Add source10
- Add Provides indexhtml
- Edit spec

* Tue May 04 2010 Anne Nicolas <anne.nicolas@mandriva.com> 2010.1-2mdv2010.1
+ Revision: 541986
- update about image

* Sun May 02 2010 Anne Nicolas <anne.nicolas@mandriva.com> 2010.1-1mdv2010.1
+ Revision: 541680
- update for 2010 Spring release

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-8mdv2010.1
+ Revision: 520128
- rebuilt for 2010.1

* Fri Feb 05 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.0-7mdv2010.1
+ Revision: 501205
- Fix missing dependency in post script

* Fri Oct 30 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-6mdv2010.0
+ Revision: 460249
- fix image

* Thu Oct 29 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-5mdv2010.0
+ Revision: 459954
- update translations

* Wed Oct 28 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-4mdv2010.0
+ Revision: 459672
- update banner

* Wed Oct 28 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-3mdv2010.0
+ Revision: 459659
- fix path
- add about-mandriva script

* Wed Oct 28 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-2mdv2010.0
+ Revision: 459649
- update translations for desktop file
- add desktop file for "about Mandriva"

* Mon Oct 26 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-1mdv2010.0
+ Revision: 459374
- update texte for about
- add "about" in indexhtml

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.1-3mdv2010.0
+ Revision: 425336
- rebuild

* Wed Apr 22 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2009.1-2mdv2009.1
+ Revision: 368770
- update mail date

* Fri Apr 03 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2009.1-1mdv2009.1
+ Revision: 363757
- update for 2009.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-2mdv2009.1
+ Revision: 351250
- rebuild

* Wed Sep 10 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-1mdv2009.0
+ Revision: 283496
- Release 2009.0
- Disable wget/gawk dependencies, not needed

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2008.1-5mdv2009.0
+ Revision: 231707
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-4mdv2009.0
+ Revision: 221631
- rebuild

* Tue Mar 25 2008 Anne Nicolas <anne.nicolas@mandriva.com> 2008.1-3mdv2008.1
+ Revision: 189870
- Fix Requires(post) - bug 39198

* Thu Mar 06 2008 Anne Nicolas <anne.nicolas@mandriva.com> 2008.1-2mdv2008.1
+ Revision: 180994
- new release
- clean images directory
- fix url link on image

* Thu Feb 28 2008 Anne Nicolas <anne.nicolas@mandriva.com> 2008.1-1mdv2008.1
+ Revision: 176181
- new disconnected image for 2008.1

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2008.0-2mdv2008.1
+ Revision: 150287
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 15 2007 Adam Williamson <awilliamson@mandriva.org> 2008.0-1mdv2008.0
+ Revision: 52262
- update clean rules for SVN files not CVS
- new release 2008.0 (update for new buildsystem and SVN)

* Sun Jul 15 2007 Adam Williamson <awilliamson@mandriva.org> 2007.0-8mdv2008.0
+ Revision: 52256
- rebuild for 2008
- Import indexhtml



* Thu Sep 21 2006 Warly <warly@mandriva.com> 2007.0-7mdv2007.0
- fix my stupid mkdir

* Wed Sep 20 2006 Warly <warly@mandriva.com> 2007.0-6mdv2007.0
- manually create the /usr/share/doc/HTML in post to workarround excludedocs 
  ignoring this directory

* Mon Sep 18 2006 Warly <warly@mandriva.com> 2007.0-5mdv2007.0
- must explicitely add /usr/share/doc/HTML as dir for excludedocs not to ignore it

* Thu Sep 14 2006 Warly <warly@mandriva.com> 2007.0-4mdv2007.0
- really fix the default index.html when build by build bot (without /etc/sysconfig/system)

* Thu Sep 14 2006 Warly <warly@mandriva.com> 2007.0-3mdv2007.0
- fix default index.html generation problem

* Thu Aug 31 2006 Warly <warly@mandriva.com> 2007.0-2mdv2007.0
- add a default index.html so that /usr/share/doc/HTML is created and 
  in case of --noscripts install
- simplify somewhat the script

* Mon Aug 21 2006 Romain d'Alverny <rdalverny@mandriva.com> 2007.0-1mdk
- updated background image, CSS and links

* Thu Feb 23 2006 Romain d'Alverny <rdalverny@mandriva.com> 2006.0-3mdk
- improved html, javascript and spec file %%post instructions; system
  language and product are now set at install

* Wed Sep 14 2005 Frederic Lepied <flepied@mandriva.com> 2006.0-2mdk
- updated translations

* Thu Sep  1 2005 Frederic Lepied <flepied@mandriva.com> 2006.0-1mdk
- 2006

* Tue Aug 16 2005 Pablo Saratxaga <pablo@mandriva.com> 10.2-6mdk
- changed name to "Mandriva Linux" in images
- some more translations

* Fri Jul 29 2005 Pablo Saratxaga <pablo@mandriva.com> 10.2-5mdk
- changed names to "Mandriva Linux"
- removed update-indexhtml from the rpm, now the network testing is
  done in testonline.html (loaded trough javascript)

* Mon Apr 11 2005 Warly <warly@mandrakesoft.com> 10.2-4mdk
- revert to previous update-indexhtml method

* Thu Mar 31 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 10.2-3mdk 
- removed update-indexhtml from the rpm, now the network testing is
  done in testonline.html (loaded trough javascript)
- put back the creation of index.html in the rpm %%post script
  (and improved it a bit)
- translation updates

* Fri Jan 28 2005 Frederic Lepied <flepied@mandrakesoft.com> 10.2-2mdk
- po updates
- don't block when updating index

* Wed Jan 19 2005 Frederic Lepied <flepied@mandrakesoft.com> 10.2-1mdk
- updated translations
- bumped the version
- dynamic index support

* Mon Oct 04 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.1-5mdk
- updated translations (sk,ka,nn,nl,hr,gl,ky,ca,pt,fa)

* Tue Sep 21 2004 David Baudens <baudens@mandrakesoft.com> 10.1-4mdk
- Images: don't display borders

* Fri Sep 10 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.1-3mdk
- various new translations

* Tue Sep 07 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.1-2mdk
- new versions of the html and first-mail files

* Thu Sep 02 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.1-1mdk
- new versions of the html and first-mail files

* Wed Apr 07 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.0-11mdk
- corrected accent in generated multipart mail

* Mon Mar 29 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 10.0-12mdk
- integrated Basque translations
- Updates/additions for Catalan, Armenian, Chinese, Tajik, Macedonian,
  Slovenian, Polish, Azeri, Kyrgyz, Arabic

* Fri Mar 12 2004 David Baudens <baudens@mandrakesoft.com> 10.0-11mdk
- Switch to Mandrakelinux

* Fri Feb 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-10mdk
- Update po

* Thu Feb 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-9mdk
- Update po

* Tue Feb 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-8mdk
- Update first mail

* Mon Feb 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-7mdk
- Fix header

* Mon Feb 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-6mdk
- Use new first message

* Tue Feb 17 2004 David Baudens <baudens@mandrakesoft.com> 10.0-5mdk
- Don't install placeholder.h (seems useless)

* Tue Feb 17 2004 David Baudens <baudens@mandrakesoft.com> 10.0-4mdk
- Fix update

* Mon Feb 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-3mdk
- Install first mail

* Fri Feb 06 2004 David Baudens <baudens@mandrakesoft.com> 10.0-2mdk
- Fix update

* Tue Jan 27 2004 David Baudens <baudens@mandrakesoft.com> - 10.0-1mdk
- New english files. All old translations have been removed

* Mon Sep 01 2003 David Baudens <baudens@mandrakesoft.com> - 9.1-10mdk
- Remove Safari
- Updated Azeri, Swedish, Danish and Hebrew pages
- added Hindi and Uzbek cyrillic pages
- changed names of Serbian pages to match new naming
- added Chinese "welcome" to image

* Wed Mar 26 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 9.1-9mdk
- Fix japanase stylesheet

* Thu Mar 13 2003 Frederic Lepied <flepied@mandrakesoft.com> 9.1-8mdk
- removed buggy %%postun

* Tue Mar 11 2003 Frederic Lepied <flepied@mandrakesoft.com> 9.1-7mdk
- removed obsolete sites from title bar

* Mon Mar 10 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 9.1-6mdk
- various new translations
- corrected stylesheet link on default page

* Fri Mar 07 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 9.1-5mdk
- Fix indexhtml page location

* Thu Mar 06 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 9.1-4mdk
- fix generation of the html file
- cleanup before removal

* Thu Feb 27 2003 David BAUDENS <baudens@mandrakesoft.com> 9.1-3mdk
- Move in /usr/share/mdk

* Mon Feb 24 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 9.1-2mdk
- updated message of the indexhtml pages

* Wed Jan 29 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 9.1-1mdk
- updated Finnish, Ukrainian and Tamil files
- added Hebrew, Nynorsk and Tajiki files
- added favicon.png so browsers supporting it can display a nice mdk icon
- changed stylesheet for chinese, as konqueror didn't displayed all chars

* Fri Nov 22 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 9.0-9mdk
- small corrections on various files (fixed links)
- updated Estonian and Catalan files

* Mon Nov 18 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 9.0-8mdk
- Added Finnish file
- corrected Japanese typo
- updated Macedonian and traditional Chinese files

* Thu Sep 12 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-7mdk
- Fix one bad translation in french page

* Thu Sep  5 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 9.0-6mdk
- Updated Chinese and Slovak pages
- Added Portuguese and Maltese files
- s/linux-mandrake.com/mandrakelinux.com/g

* Tue Sep 03 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-5mdk
- Remove obsoletes pages and flags
- Add MandrakeClub links

* Thu Aug 29 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 9.0-4mdk
- added Tamil page; updated Korean and Norwegian pages
- fixed another typo (thanks to Per Oyvind Karlsen)

* Thu Aug 29 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-3mdk
- Fix a typo (thanks to Quel Qun)

* Fri Aug 16 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 9.0-2mdk
- updated Czech and Polish files
- fixed Linux Weekly News urls

* Mon Jul 29 2002 David BAUDENS <baudens@mandrakesoft.com> 9.0-1mdk
- fix a typo. Thanks to Spearman

* Mon Jul 22 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-7mdk
- updated Slovak file

* Tue Jul 16 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-6mdk
- fixed a typo in English file
- updated Romanian and Bulgarian files

* Mon Mar 11 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-5mdk
- updated cy, da, nl, sr, ru, hr, ms, sl pages

* Mon Mar 04 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-4mdk
- Remove MamaLinux from french page

* Wed Feb 20 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-3mdk
- checked all pages with mozilla and konqueror, and do some changes in
  stylesheets so they all display correctly

* Tue Feb 19 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-2mdk
- updated Italian and Arabic files

* Fri Feb 08 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 8.2-1mdk
- changed version to match distribution version
- fixed Japanese encoding declaration; converted to utf-8 the iso-8859-13
  (Netscape has a bug with it) and iso-8859-14 (alsmot no browser supports
  it) pages.

* Fri Dec 07 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.1-10mdk
- updates of various translated files; utf-8 used instead of marginal
  encodings

* Fri Oct 26 2001 David BAUDENS <bauden@mandrakesoft.com> 8.1-9mdk
- Fix bad links in english and french pages

* Mon Sep 24 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.1-8mdk
- rebuild including latest translations

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-7mdk
- Add german translation (thanks to Stefan Siegel)

* Fri Sep 21 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-6mdk
- Fix a typo in french page
- Add french links in french page

* Mon Sep 17 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-5mdk
- Fix french translation (thanks to Laurent MONTEL)
- Fix english translation (thanks to Frederic BASTOK)

* Sun Sep 16 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-4mdk
- Add french translation

* Thu Sep 13 2001 David BAUDENS <baudens@mandrakesoft.com> 8.1-3mdk
- Use new indexhtml page for english

* Tue Sep 06 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.1-2mdk
- fixed typos in Hungarian file

* Mon Aug 13 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.1-1mdk
- changed to 8.1 the version number.
- Updated Hungarian page, added Bosanski page

* Fri Apr 20 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.0-4mdk
- added Traditional Chinese page
- corrected Red Hat Linux name (bug #2919)

* Mon Apr 16 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-3mdk
- Fix dead link in index-fr.html

* Fri Apr 12 2001 David BAUDENS <baudens@mandrakesoft.com> 8.0-2mdk
- Changed index-en.html, index-fr.html and index.html

* Tue Mar 06 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 8.0-1mdk
- changed version to 8.0
- added some more html files

* Thu Jan 30 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 7.2-1mdk
- added Georgian and Azeri files
- correction and updates for Croatian, Lithuanian and Macedonian
- changed version to 7.2

* Fri Oct 06 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-12mdk
- added Korean page

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 7.1-11mdk
- fix out the conflict with mine and pablo upload

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 7.1-10mdk
- corrected %%pre script, Pablo sucks

* Mon Sep 04 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-9mdk
- added Greek page
- corrections to Czech page
- macrozification

* Mon Aug 28 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-8mdk
- corrections to the Polish file

* Mon Jul 17 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-7mdk
- added Basque file

* Mon Jul 03 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-6mdk
- corrected typos in the Czech file
- corrected the charset declaration of some pages

* Fri Jun 16 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-5mdk
- Added Arabic file

* Mon May 22 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-4mdk
- Corrected typo in Russian file (a word was truncated)

* Thu May 18 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-3mdk
- Added simplified Chinese & Afrikaans files

* Fri Apr 21 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.1-2mdk
- added Slovenian and Vietnamese pages

* Tue Apr 18 2000 Warly <warly@mandrakesoft.com> 7.1-1mdk
- 7.1

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 7.0-6mdk
- Changed logo, icon.

* Thu Feb 03 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7.0-5mdk
- added Serbian (both latin and Cyrillic) language file

* Mon Jan 10 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Latvian page

* Wed Jan 05 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Japanese page

* Mon Dec 27 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- corrected some html pages
- added Esperanto page

* Tue Dec 21 1999 Florent Villard <warly@mandrakesoft.com>
- new images for 7.0

* Tue Nov 16 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added cs, gl translations

* Fri Nov 05 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added bg, da, et, mk, sk translations

* Fri Sep 28 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added translations for br, ca, cy, pt

* Fri Sep 17 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added translations for ga,is,lt,pl,ru,tr,uk

* Tue Sep 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added translations for de,hu,nl,ro

* Sat Aug 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added es,fr,id,no,wa files & descriptions; added a bar on bottom of
  all pages to choose the language.

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rewriting the .spec.
- Build for new environement (Rel: 3mdk).

* Thu Apr 29 1999 Gaël Duval <gael@linux-mandrake.com>
- lipstick

* Thu Apr 25 1999 Gaël Duval <gael@linux-mandrake.com>
- updated for Linux-Mandrake 6.0

* Thu Jan 21 1999 Gaël Duval <gael@linux-mandrake.com>
- updated for Linux-Mandrake 5.3

* Mon Nov 16 1998 Gaël Duval <gael@linux-mandrake.com>
- updated for Linux-Mandrake

* Sun Oct 11 1998 Bill Nottingham <notting@redhat.c9om>
- point to 5.2 installation guide
- 90 days installation support, not 30

* Tue Oct  6 1998 Matt Wilson <msw@redhat.com>
- Remove link to Applixware as we no longer ship it.

* Sat Sep 19 1998 Jeff johnson <jbj@redhat.com>
- update version to 5.2.
- tweak description so that it's slightly different than summary.

* Tue Jul 21 1998 Jeff Johnson <jbj@redhat.com>
- fix spelling error.
- add build root.

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Edward C. Bailey <ed@redhat.com>
- Added link to 5.1 Installation Guide

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- changed summary and description for new version of RPM

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- updated for 5.0.. new links to various LDP guides

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Tue Apr 15 1997 Erik Troan <ewt@redhat.com>
- Incorporated Otto's fix into tarball properly. 

* Mon Apr 14 1997 Otto Hammersmith <otto@redhat.com>
- Fixed an error in /usr/doc/HTML/index.html that said we provided 
  60 days of installation support, not 30 like it should.  
