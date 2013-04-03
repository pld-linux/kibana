# TODO
# - configs to webapps
# - webserver config
Summary:	Web interface to Logstash and ElasticSearch
Name:		kibana
Version:	0.2.0
Release:	0.3
License:	BSD
Group:		Daemons
Source0:	https://github.com/rashidkpc/Kibana/archive/v%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	167a533a8a2d4ec4458e86cfe6b5e0b1
URL:		http://kibana.org/
BuildRequires:	rpmbuild(macros) >= 1.228
Requires:	ruby-rack
Requires:	ruby-rack-protection
Requires:	ruby-sinatra
Requires:	ruby-tilt
Requires:	ruby-tzinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Kibana is a highly scalable interface for Logstash and ElasticSearch that
allows you to efficiently search, graph, analyze and otherwise make sense of a
mountain of logs.

%prep
%setup -q -n Kibana-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a . $RPM_BUILD_ROOT%{_appdir}

%{__rm} $RPM_BUILD_ROOT%{_appdir}/{.{gitignore,travis.yml},{README,LICENSE}.md}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%dir %{_appdir}
%{_appdir}/Gemfile
%{_appdir}/Gemfile.lock
%{_appdir}/Rakefile

%{_appdir}/KibanaConfig.rb
%{_appdir}/config.ru

%{_appdir}/kibana-daemon.rb
%{_appdir}/kibana.gemspec
%{_appdir}/kibana.rb

%{_appdir}/lib
%{_appdir}/views

%dir %{_appdir}/static
%{_appdir}/static/*.html
%{_appdir}/static/favicon.ico
%{_appdir}/static/images

%dir %{_appdir}/static/lib
%dir %{_appdir}/static/lib/css
%dir %{_appdir}/static/lib/css/images
%dir %{_appdir}/static/lib/js
%dir %{_appdir}/static/lib/js/lib

# doc?
%dir %{_appdir}/sample
%{_appdir}/sample/kibana

# rm tests?
%{_appdir}/spec

# jquery-twitter-bootstrap
%dir %{_appdir}/static/lib/bootstrap
%dir %{_appdir}/static/lib/bootstrap/css
%dir %{_appdir}/static/lib/bootstrap/img
%dir %{_appdir}/static/lib/bootstrap/js
%{_appdir}/static/lib/bootstrap/css/bootstrap.css
%{_appdir}/static/lib/bootstrap/css/bootstrap.min.css
%{_appdir}/static/lib/bootstrap/img/glyphicons-halflings-white.png
%{_appdir}/static/lib/bootstrap/img/glyphicons-halflings.png
%{_appdir}/static/lib/bootstrap/js/bootstrap.js
%{_appdir}/static/lib/bootstrap/js/bootstrap.min.js
%{_appdir}/static/lib/css/bootstrap.min.css
%{_appdir}/static/lib/js/lib/bootstrap-datepicker.js

# jquery-ui
%{_appdir}/static/lib/css/images/ui-*.png
%{_appdir}/static/lib/css/jquery-ui-1.8.16.custom.css
%{_appdir}/static/lib/css/jquery.ui.datepicker.css
%{_appdir}/static/lib/js/lib/jquery-ui-1.8.16.custom.min.js

%{_appdir}/static/lib/css/font-awesome.css
%dir %{_appdir}/static/lib/font
%{_appdir}/static/lib/font/fontawesome-webfont.eot
%{_appdir}/static/lib/font/fontawesome-webfont.svg
%{_appdir}/static/lib/font/fontawesome-webfont.ttf
%{_appdir}/static/lib/font/fontawesome-webfont.woff

# jquery
%{_appdir}/static/lib/js/jquery-1.7.2.min.js
%{_appdir}/static/lib/js/lib/jquery.min.js

# js-json2
%{_appdir}/static/lib/js/lib/json2.js

%{_appdir}/static/lib/js/ajax.js
%{_appdir}/static/lib/js/lib/date.js
%{_appdir}/static/lib/js/lib/excanvas.min.js
%{_appdir}/static/lib/js/lib/iso8601.min.js
%{_appdir}/static/lib/js/lib/jquery.flot.min.js
%{_appdir}/static/lib/js/lib/jquery.flot.pie.min.js
%{_appdir}/static/lib/js/lib/jquery.flot.selection.min.js
%{_appdir}/static/lib/js/lib/jquery.flot.stack.min.js
%{_appdir}/static/lib/js/lib/jquery.history.js
%{_appdir}/static/lib/js/lib/jquery.smartresize.js
%{_appdir}/static/lib/js/lib/safebase64.js
%{_appdir}/static/lib/js/shared.js
%{_appdir}/static/lib/js/stream.js
%{_appdir}/static/lib/css/stream.css
%{_appdir}/static/lib/css/style.css
