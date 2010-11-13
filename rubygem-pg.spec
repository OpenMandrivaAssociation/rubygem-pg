%define oname pg

Name:           rubygem-%{oname}
Version:        0.9.0
Release:        %mkrel 1
Summary:        A Ruby interface to the PostgreSQL RDBMS
License:        GPLv2+ or Ruby License
Group:          Development/Ruby
Source0:        http://rubygems.org/gems/%{oname}-%{version}.gem
URL:            http://bitbucket.org/ged/ruby-pg/
BuildRequires:  rubygems
BuildRequires:  postgresql-devel
BuildRequires:  ruby-devel
Requires:       rubygems
Requires:       postgresql-server
Provides:       rubygem(%{oname}) = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This is the extension library to access a PostgreSQL database from Ruby.
This library works with PostgreSQL 7.4 and later.


%prep

%build
mkdir -p .%{ruby_gemdir}
gem install --local --install-dir .%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -rf .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# Move Arch dependent libs to sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so %{buildroot}%{ruby_sitearchdir}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.require_paths
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/rake/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/BSD
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Contributors
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/GPL
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile*
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README*
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/pg_ext.so
