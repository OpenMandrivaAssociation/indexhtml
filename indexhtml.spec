Summary:	%{distribution} html welcome page
Name:		indexhtml
Version:	2013.0
Release:	0.11
Group:		System/Base
License:	GPLv2+
Url:		http://www.openmandriva.org/
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
Requires(pre):	mandriva-release-common
Requires(post): gawk coreutils sed

%description
%{distribution} index.html welcome page displayed by web browsers
when they are launched, first mail displayed on mail clients
after installation and "about" information.

%prep
%setup -q

%build
cd about
./create_html.sh

%install
install -d -m755 %{buildroot}%{_datadir}/mdk/indexhtml/
tar c -C HTML . | tar x -C %{buildroot}%{_datadir}/mdk/indexhtml/
#install -m 0755 update-indexhtml %{buildroot}%{_datadir}/mdk/indexhtml/

install -d -m755 %{buildroot}%{_datadir}/mdk/mail/text/
install -d -m755 %{buildroot}%{_datadir}/mdk/mail/html/
for lang in $(find mail/header-* -type f | sed "s|mail/header-||" ); do
	cat mail/header-$lang &> tmpfile
	cat mail/mail-$lang.txt >> tmpfile
	install -m 0644 tmpfile %{buildroot}%{_datadir}/mdk/mail/text/mail-$lang

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
#	cat mail/mail-images >> tmpfile
	install -m 0644 tmpfile %{buildroot}%{_datadir}/mdk/mail/html/mail-$lang

done

install -d -m 0755 %{buildroot}%{_datadir}/doc/HTML/
install -m 0644 HTML/index.html %{buildroot}%{_datadir}/doc/HTML/index.html
#install -d -m 0755 %{buildroot}etc/sysconfig/network-scripts/ifup.d
#cd %{buildroot}etc/sysconfig/network-scripts/ifup.d
#ln -s ../../../../%{_datadir}/mdk/indexhtml/update-indexhtml indexhtml

# add a default 
cat %{buildroot}%{_datadir}/mdk/indexhtml/index.html | \
	sed "s/#RELEASE/`cat /etc/release`/" | \
	sed "s/#PRODUCT_ID/openmandriva-lx/" | \
	sed "s/#MDV_PACK//" | \
	sed "s/#LANG/en/g" \
	> %{buildroot}%{_datadir}/doc/HTML/index.html

# about Mandriva
install -d -m755 %{buildroot}%{_datadir}/mdk/about
install -d -m755 %{buildroot}%{_datadir}/applications
install -d -m755 %{buildroot}%{_bindir}
cp about/html/* %{buildroot}%{_datadir}/mdk/about
cp -r about/style %{buildroot}%{_datadir}/mdk/about/
cp about/about-openmandriva-lx.desktop %{buildroot}%{_datadir}/applications
cp about/about-openmandriva-lx %{buildroot}%{_bindir}

%post
# done to prevent excludedocs to ignore the doc/HTML
mkdir -p %{_datadir}/doc/HTML
cat %{_datadir}/mdk/indexhtml/index.html | sed \
	-e "s!#RELEASE!`cat /etc/release`!" \
	-e "s!#PRODUCT_ID!!"  \
	-e "s!#MDV_PACK!!"  \
	-e "s!#LANG!${LC_NAME/[-_]*}!g" \
	> %{_datadir}/doc/HTML/index.html

%files
%{_datadir}/mdk/
%dir %{_datadir}/doc/HTML/
%{_datadir}/doc/HTML/index.html
#/etc/sysconfig/network-scripts/ifup.d/indexhtml
%{_datadir}/applications/about-openmandriva-lx.desktop
%{_bindir}/about-openmandriva-lx

