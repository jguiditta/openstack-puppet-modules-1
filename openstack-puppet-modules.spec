Name:           openstack-puppet-modules
Version:        2015.1.6
Release:        1%{?dist}
Summary:        Collection of Puppet modules for OpenStack deployment
License:        ASL 2.0 and GPLv2 and GPLv3

URL:            https://github.com/redhat-openstack

Source0:        https://github.com/redhat-openstack/%{name}/archive/%{version}.tar.gz

Patch0001: 0001-Sync-amqp-support-with-other-openstack-modules.patch
Patch0002: 0002-Add-support-for-WEBROOT-in-local_settings.patch
Patch0003: 0003-Change-default-documentation-URL.patch
Patch0004: 0004-Allow-customization-of-dhcp_domain-setting-from-agen.patch
Patch0005: 0005-Requirement-on-server-package-should-use-mysql-serve.patch

BuildArch:      noarch
Requires:       rubygem-json

%description
A collection of Puppet modules which are required to install and configure
OpenStack via installers using Puppet configuration tool.


%prep
%setup -q -n %{name}-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf


%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r $(grep ^mod Puppetfile |cut -d\' -f2) %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp Puppetfile %{buildroot}/%{_datadir}/openstack-puppet/Puppetfile
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init


%files
%{_datadir}/openstack-puppet/modules/*
%{_datadir}/openstack-puppet/Puppetfile


%changelog
* Mon Jun 15 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.6-1
- Update to upstream 2015.1.6

* Thu Jun 11 2015 Ivan Chavero <ichavero@redhat.com> 2015.1.4-1
- Update to upstream 2015.1.4
- Bump glance to master

* Tue Jun 02 2015 Ivan Chavero <ichavero@redhat.com> 2015.1.3-1
- Update to upstream 2015.1.3

* Fri May 15 2015 Lukas Bezdicka <lbezdick@redhat.com> 2015.1.2-1
- Update to upstream 2015.1.2

* Wed May 13 2015 Gaël Chamoulaud <gchamoul@redhat.com> - 2015.1.1-1
-  Updated to release 2015.1.1

* Mon May 11 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 2015.1.0-2
- Add patch to fix TripleO support

* Thu Apr 30 2015 Alan Pevec <alan.pevec@redhat.com> 2015.1.0-1
- OpenStack Kilo release
