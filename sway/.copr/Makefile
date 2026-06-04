srpm:
	dnf install -y rpm-build spectool
	cp config.minimal sway-portals.conf $(RPM_SOURCEDIR)/
	spectool -g -R sway.spec
	rpmbuild -bs sway.spec --define "_sourcedir $(RPM_SOURCEDIR)" --define "_srcrpmdir $(outdir)"
