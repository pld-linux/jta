# NOTE:
# - it seems to be an open source JTA implementation:
#   http://www.atomikos.com/Main/TransactionsEssentials
%define	_ver	%(echo %{version} | tr . _)
Summary:	Java Transaction API
Summary(es.UTF-8):	API de transacciones para Java
Summary(pl.UTF-8):	API transakcji do Javy
Name:		jta
Version:	1.1
Release:	0.1
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
Source0:	%{name}-%{_ver}-classes.zip
# NoSource0-md5:	f09f5b5856b85b9d1b200a36355a0572
URL:		http://java.sun.com/products/jta/
NoSource:	0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Transaction API.

%description -l es.UTF-8
API de transacciones para Java.

%description -l pl.UTF-8
API transakcji do Javy.

%prep
%setup -q -c

%build
jar cf %{name}-%{version}.jar javax/

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install *.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
