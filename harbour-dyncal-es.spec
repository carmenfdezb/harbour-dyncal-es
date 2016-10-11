Name:          harbour-dyncal-es
Version:       0.3.0
Release:       2
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