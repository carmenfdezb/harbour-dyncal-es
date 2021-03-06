Name:          harbour-dyncal-es
Version:       0.4.0
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

%pre
if [ $1 = 2 ]; then
	// Do stuff specific to upgrades
/usr/share/harbour-dyncal-es/restore.sh
rm -rf /usr/share/harbour-dyncal-es/icons/*.*
fi

%post
if [ $1 = 1 ]; then
	// Do stuff specific to first install
mkdir /usr/share/harbour-dyncal-es/backup
fi
chmod +x /usr/share/harbour-dyncal-es/*.sh
/usr/share/harbour-dyncal-es/run.sh

%preun
if [ $1 = 0 ]; then
	// Do stuff specific to uninstalls
/usr/share/harbour-dyncal-es/restore.sh
fi

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
* Wed Oct 12 2016 0.4.0-1
- Upgrade issue fixed.

* Tue Oct 11 2016 0.3.0-2
- Minor fix.

* Tue Oct 11 2016 0.3.0-1
- Bug fix.
- Icons improved: high-res and redesigned.
- Updated to 2016-2017 calendar.

* Wed Dec 30 2015 0.2
- Fix and add some icons.
- Build "noarch".

* Mon Dec 14 2015 0.1
- First build.