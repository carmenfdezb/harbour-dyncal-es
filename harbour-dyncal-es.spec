Name:          harbour-dyncal-es
Version:       0.2.0
Release:       1
Summary:       DynCal Spain
Group:         System/Tools
Vendor:        carmenfdezb
Distribution:  SailfishOS
Requires: harbour-dyncal >= 0.3.0-1
Packager: carmenfdezb
URL:           twitter.com/cfb014
License:       GPL

%description
Change Calendar icon accordingly with the day. It features Spanish holidays.

%files
%defattr(-,root,root,-)
/usr/share/*

%post
mkdir /usr/share/harbour-dyncal-es/backup
chmod +x /usr/share/harbour-dyncal-es/*.sh
/usr/share/harbour-dyncal-es/run.sh

%preun
/usr/share/harbour-dyncal-es/restore.sh

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-dyncal-es
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Wed Dec 30 2015 0.2
- Fix and add some icons.
- Build "noarch".

* Mon Dec 14 2015 0.1
- First build.