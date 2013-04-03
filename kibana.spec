Summary:	Make sense of a mountain of logs Now in Ruby!
Name:		kibana
Version:	0.2.0
Release:	0.1
License:	Apache v2.0
Group:		Daemons
Source0:	https://github.com/rashidkpc/Kibana/archive/v%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	167a533a8a2d4ec4458e86cfe6b5e0b1
URL:		http://kibana.org/
BuildRequires:	rpmbuild(macros) >= 1.228
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n Kibana-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
