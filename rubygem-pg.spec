# Generated from pg-0.14.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	pg

Summary:	Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/]
Name:		rubygem-%{rbname}

Version:	0.14.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://bitbucket.org/ged/ruby-pg
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	pq-devel

%description
Pg is the Ruby interface to the {PostgreSQL
RDBMS}[http://www.postgresql.org/].
It works with {PostgreSQL 8.3 and later}.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/ext
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/ext/*.c
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pg
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pg/*.rb
%{ruby_sitearchdir}/*.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/POSTGRES
