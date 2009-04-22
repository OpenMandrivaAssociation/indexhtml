%define name indexhtml
%define version 2009.1
%define release %mkrel 2

Summary:	Mandriva Linux html welcome page
Name:		%{name}
Version:	%{version}
Release: 	%{release}
URL:		http://start.mandriva.com/
#Requires:	wget, gawk
Requires(pre):	mandriva-release-common
Source:		%{name}-%{version}.tar.bz2
Group:		System/Base
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch


%description
Mandriva Linux index.html welcome page displayed by web browsers
when they are launched; and first mail displayed on mail clients
after installation.

%prep

%setup -q

%build

%install
rm -fr %buildroot/

find $RPM_BUILD_DIR/%name -name ".svn" -print | xargs /bin/rm -fr

install -d -m 0755 %buildroot/%_datadir/mdk/indexhtml/
tar c -C HTML . | tar x -C %buildroot/%_datadir/mdk/indexhtml/
install -m 0755 update-indexhtml %buildroot/%_datadir/mdk/indexhtml/

install -d -m 0755 %buildroot/%_datadir/mdk/mail/text/
install -d -m 0755 %buildroot/%_datadir/mdk/mail/html/
for lang in $(find mail/header-* -type f | sed "s|mail/header-||" ); do
	cat mail/header-$lang &> tmpfile
	cat mail/mail-$lang.txt >> tmpfile
	install -m 0644 tmpfile %buildroot/%_datadir/mdk/mail/text/mail-$lang

	cat mail/header-$lang &> tmpfile
	echo "Content-Type: multipart/related; type=\"multipart/alternative\";" >>tmpfile
	echo "	 boundary=\"=-tThpx1YEZqL4gn53WjQ1\"" >> tmpfile
	echo "" >> tmpfile
	echo "--=-tThpx1YEZqL4gn53WjQ1" >> tmpfile
	echo "Content-Type: multipart/alternative; boundary=\"=-aFPGjTr5jUHhXPWxbLcT\"" >>tmpfile
	echo "" >> tmpfile
	echo "--=-aFPGjTr5jUHhXPWxbLcT" >> tmpfile
	cat mail/mail-$lang.txt >> tmpfile
	cat mail/mail-$lang.html >> tmpfile
	cat mail/mail-images >> tmpfile
	install -m 0644 tmpfile %buildroot/%_datadir/mdk/mail/html/mail-$lang

done

install -d -m 0755 %buildroot/%_datadir/doc/HTML/
install -m 0644 HTML/index.html %buildroot/%_datadir/doc/HTML/index.html
#install -d -m 0755 %buildroot/etc/sysconfig/network-scripts/ifup.d
#cd %buildroot/etc/sysconfig/network-scripts/ifup.d
#ln -s ../../../../%_datadir/mdk/indexhtml/update-indexhtml indexhtml

# add a default 
cat %buildroot/%_datadir/mdk/indexhtml/index.html | \
	sed "s/#MDV_RELEASE/`cat /etc/release`/" | \
	sed "s/#MDV_PRODUCT/download/" | \
	sed "s/#MDV_PACK//" | \
	sed "s/#LANG/en/g" \
	> %buildroot/%_datadir/doc/HTML/index.html


%clean
rm -fr %buildroot

%post
# done to prevent excludedocs to ignore the doc/HTML
mkdir -p  %_datadir/doc/HTML
cat %_datadir/mdk/indexhtml/index.html | \
	sed "s/#MDV_RELEASE/`cat /etc/release`/" | \
	sed "s/#MDV_PRODUCT/`gawk -F= '/META_CLASS/ { print $2 }' /etc/sysconfig/system`/" | \
	sed "s/#MDV_PACK//" | \
	sed "s/#LANG/${LC_NAME/[-_]*}/g" \
	> %_datadir/doc/HTML/index.html

%files
%defattr(-,root,root,-)
%_datadir/mdk/
%dir %_datadir/doc/HTML/
%_datadir/doc/HTML/index.html
#/etc/sysconfig/network-scripts/ifup.d/indexhtml
