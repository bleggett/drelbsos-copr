srpm:
	dnf install -y rpm-build spectool
	spectool -g -R cyanrip/cyanrip.spec
	rpmbuild -bs cyanrip/cyanrip.spec --define "_sourcedir $(RPM_SOURCEDIR)" --define "_srcrpmdir $(outdir)"
