Summary:	%{distribution} html welcome page
Name:		indexhtml
Version:	2015.0
Release:	2
Group:		System/Base
License:	GPLv2+
Url:		%{disturl}
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
Requires(pre):	distro-release-common
Requires(post): gawk
Requires(post): coreutils
Requires(post): sed

%description
%{distribution} index.html welcome page displayed by web browsers
when they are launched, first mail displayed on mail clients
after installation and "about" information.

%prep
%setup -q

%build
cd about
#./create_html.sh

%install
install -d -m755 %{buildroot}%{_datadir}/mdk/indexhtml/
cp -a HTML/* %{buildroot}%{_datadir}/mdk/indexhtml/

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

# about OpenMandriva
install -d -m755 %{buildroot}%{_datadir}/mdk/about
install -d -m755 %{buildroot}%{_datadir}/applications
install -d -m755 %{buildroot}%{_bindir}
cp about/html/* %{buildroot}%{_datadir}/mdk/about
cp -r about/style %{buildroot}%{_datadir}/mdk/about/
cp about/about-openmandriva-lx.desktop %{buildroot}%{_datadir}/applications
cp about/about-openmandriva-lx %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/doc/HTML/
ln -s %{_datadir}/mdk/indexhtml/index.html %{buildroot}%{_datadir}/doc/HTML/index.html

%post
# done to prevent excludedocs to ignore the doc/HTML
mkdir -p %{_datadir}/doc/HTML
sed -i -e "s/#PRODUCT_ID/`cat /etc/product.id`/" -e "s/#LANG/${LC_NAME/[-_]*}/g" %{_datadir}/mdk/indexhtml/index.html

%files
%{_datadir}/mdk/
%dir %{_datadir}/doc/HTML/
%{_datadir}/doc/HTML/index.html
%{_datadir}/applications/about-openmandriva-lx.desktop
%{_bindir}/about-openmandriva-lx
