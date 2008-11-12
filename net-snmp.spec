# TODO
# - package or remove:
#   %{_datadir}/snmp/snmp_perl.pl
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages only for deps resolving
%bcond_without	rpm		# don't include RPM support
%bcond_without	kerberos5	# don't include kerberos support
%bcond_without	lm_sensors	# don't include sensors support
%bcond_without	perl		# don't include Perl modules and utils
%bcond_without	python		# don't include Python modules
%bcond_without	static_libs	# don't build static library
#
%include	/usr/lib/rpm/macros.perl
Summary:	A collection of SNMP protocol tools
Summary(es.UTF-8):	Agente SNMP de la UCD
Summary(pl.UTF-8):	Kolekcja narzędzi do obsługi protokołu SNMP
Summary(pt_BR.UTF-8):	Agente SNMP da UCD
Summary(ru.UTF-8):	Набор утилит для протокола SNMP от UC-Davis
Summary(uk.UTF-8):	Набір утиліт для протоколу SNMP від UC-Davis
Name:		net-snmp
Version:	5.4.2.1
Release:	1
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/net-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	984932520143f0c8bf7b7ce1fc9e1da1
Source1:	%{name}d.init
Source2:	%{name}d.conf
Source3:	%{name}d.sysconfig
Source4:	%{name}trapd.init
Source5:	%{name}trapd.conf
Source6:	%{name}trapd.sysconfig
Source7:	ucd-ipchains.tar.gz
# Source7-md5:	29949f1008f1a04d6efefd5b3ea607da
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-rpm-implicit-libs.patch
Patch2:		%{name}-config-noflags.patch
Patch3:		%{name}-manpage.patch
Patch4:		%{name}-link.patch
Patch5:		%{name}-llinterfaces.patch
Patch6:		%{name}-kernel_headers.patch
Patch7:		%{name}-rpmpath.patch
Patch8:		%{name}-snmpksm.patch
Patch9:		%{name}-python.patch
Patch10:	%{name}-lvalue.patch
Patch11:	%{name}-defaultconfig.patch
Patch12:	%{name}-use-rpm-hrmib.patch
URL:		http://www.net-snmp.org/
BuildRequires:	autoconf >= 2.61-3
BuildRequires:	automake
BuildRequires:	elfutils-devel
%{?with_kerberos5:BuildRequires:	heimdal-devel}
BuildRequires:	libtool >= 1.4
BuildRequires:	libwrap-devel
%{?with_lm_sensors:BuildRequires:	lm_sensors-devel}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_autodeps:BuildRequires:	perl-Term-ReadKey}
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with python}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with rpm}
BuildRequires:	rpm
BuildRequires:	rpm-perlprov >= 3.0.3-16
%endif
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-mibs = %{version}-%{release}
Requires:	/usr/bin/setsid
Requires:	rc-scripts >= 0.2.0
Provides:	snmpd
Obsoletes:	cmu-snmp
Obsoletes:	snmpd
Obsoletes:	ucd-snmp
Conflicts:	rpm < 4.4.9-43.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# linking libraries is ugly in this package
%define		no_install_post_check_so	1

%define		logfile		/var/log/snmpd.log

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management (hence the name). The net-snmp project includes
various SNMP tools: an extensible agent, an SNMP library, tools for
requesting or setting information from SNMP agents, tools for
generating and handling SNMP traps, a version of the netstat command
which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd daemon, documentation, etc.

%description -l es.UTF-8
Este paquete se deriva de la implementación del Protocolo Simple de
Gestión de Redes versión 2 (SNMPv2) de la Universidad Carnegie Mellon.
Útil para administrar redes y hacer contabilidad.

%description -l pl.UTF-8
SNMP (Simple Network Management Protocol) jest protokołem używanym do
zarządzania sieciami. Pakiet zawiera narzędzia: rozbudowywalnego
agenta, bibliotekę SNMP, narzędzia do odpytywania oraz ustawiania
informacji poprzez agentów SNMP, narzędzia do generowania i obsługi
pułapek SNMP, wersję komendy netstat używającą SNMP, przeglądarkę mib
w Tk/Perl, demona, dokumentację itp.

%description -l pt_BR.UTF-8
Este pacote é derivado da implementação do Protocolo Simples de
Gerenciamento de Redes versão 2 (SNMPv2) da Universidade Carnegie
Mellon. Útil para gerenciar redes e fazer contabilidade.

%description -l ru.UTF-8
SNMP (Simple Network Management Protocol) - это протокол, используемый
для управления сетью (отсюда и название). Проект net-snmp включает
разнообразные SNMP-утилиты: расширяемый агент, библиотека SNMP,
утилиты для запроса или установки информации от SNMP-агентов, утилиты
для генерации и обработки SNMP-трапов, версия команды netstat,
использующей SNMP, и mib-браузер на Tk/Perl. Этот пакет содержит
демоны snmpd и snmptrapd, документацию и т.д.

%description -l uk.UTF-8
SNMP (Simple Network Management Protocol) - це протокол, який
використовують для керування мережею (звідси і назва). Проект net-snmp
містить різноманітні SNMP-утиліти: розширюваний агент, бібліотека
SNMP, утиліти для запросу та встановлення інформації від NMP-агентів,
утиліти для генерації та обробки SNMP-трапів, версія команди netstat,
яка використовує SNMP, та mib-браузер на Tk/Perl. Цей пакет містить
демони snmpd та snmptrapd, документацію і т.і.

%package libs
Summary:	NET SNMP libraries
Summary(pl.UTF-8):	Biblioteki SNMP
Group:		Libraries
Requires:	%{name}-mibs
Obsoletes:	net-snmp-compat-libs
Obsoletes:	ucd-snmp-libs

%description libs
NET SNMP libraries.

%description libs -l pl.UTF-8
Biblioteki SNMP.

%package devel
Summary:	The development environment for the net-snmp project
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl.UTF-8):	Pliki dla programistów używających bibliotek net-snmp
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru.UTF-8):	Среда разработки для проекта UCD-SNMP
Summary(uk.UTF-8):	Середовище розробки для проекту UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	elfutils-devel
%{?with_kerberos5:Requires:	heimdal-devel}
Requires:	libwrap-devel
%{?with_lm_sensors:Requires:	lm_sensors-devel}
Requires:	openssl-devel >= 0.9.7c
Obsoletes:	ucd-snmp-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the net-snmp project's network management
tools.

%description devel -l es.UTF-8
Estas son las bibliotecas y archivos de inclusión para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creación de
programas para uso en la gestión de redes.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do rozwoju
aplikacji używających protokołu SNMP.

%description devel -l pt_BR.UTF-8
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
com o SNMP da UCD. Com este pacote é possível a criação de programas
para uso no gerenciamento de redes.

%description devel -l ru.UTF-8
Пакет ucd-snmp-devel содержит библиотеки разработчика и хедера для
использования с утилитами управления сетью проекта net-snmp.

%description devel -l uk.UTF-8
Пакет ucd-snmp-devel містить бібліотеки програміста та хедери для
використання з утилітами керування мережею проекту net-snmp.

%package static
Summary:	Static net-snmp libraries
Summary(pl.UTF-8):	Statyczne biblioteki net-snmp
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com ucd-snmp
Summary(ru.UTF-8):	Статические библиотеки для проекта net-snmp
Summary(uk.UTF-8):	Статичні бібліотеки для проекту net-snmp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description static
Static net-snmp libraries.

%description static -l pl.UTF-8
Statyczne biblioteki net-snmp.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com net-snmp.

%package compat-devel
Summary:	The development environment for the UCD-SNMP project
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl.UTF-8):	Pliki dla programistów używających bibliotek UCD-SNMP
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru.UTF-8):	Среда разработки для проекта UCD-SNMP
Summary(uk.UTF-8):	Середовище розробки для проекту UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	openssl-devel >= 0.9.7d
Obsoletes:	cmu-snmp-devel
Obsoletes:	ucd-snmp-devel

%description compat-devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

%description compat-devel -l es.UTF-8
Estas son las bibliotecas y archivos de inclusión para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creación de
programas para uso en la gestión de redes.

%description compat-devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe i biblioteki potrzebne do rozwoju
aplikacji używających protokołu SNMP.

%description compat-devel -l pt_BR.UTF-8
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
com o SNMP da UCD. Com este pacote é possível a criação de programas
para uso no gerenciamento de redes.

%description compat-devel -l ru.UTF-8
Пакет ucd-snmp-devel содержит библиотеки разработчика и хедера для
использования с утилитами управления сетью проекта UCD-SNMP.

%description compat-devel -l uk.UTF-8
Пакет ucd-snmp-devel містить бібліотеки програміста та хедери для
використання з утилітами керування мережею проекту UCD-SNMP.

%package compat-static
Summary:	Static UCD-SNMP libraries
Summary(pl.UTF-8):	Statyczne biblioteki UCD-SNMP
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com ucd-snmp
Summary(ru.UTF-8):	Статические библиотеки для проекта UCD-SNMP
Summary(uk.UTF-8):	Статичні бібліотеки для проекту UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-compat-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description compat-static
Static UCD-SNMP libraries.

%description compat-static -l pl.UTF-8
Statyczne biblioteki UCD-SNMP.

%description compat-static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com ucd-snmp.

%package mibs
Summary:	MIB database
Summary(pl.UTF-8):	Baza danych MIB
Group:		Applications/System
Conflicts:	ucd-snmp-libs

%description mibs
MIB database.

%description mibs -l pl.UTF-8
Baza danych MIB.

%package snmptrapd
Summary:	SNMP trap daemon
Summary(pl.UTF-8):	Demon obsługujący pułapki SNMP
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts >= 0.2.0
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-snmptrapd

%description snmptrapd
The ucd-snmp-snmptrapd package contains snmp trap daemon.

%description snmptrapd -l pl.UTF-8
Pakiet zawiera demon obsługujący pułapki SNMP.

%package utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Summary(es.UTF-8):	Utilitarios del SNMP de la UCD
Summary(pl.UTF-8):	Narzędzia używające protokołu SNMP
Summary(pt_BR.UTF-8):	Utilitários do SNMP da UCD
Summary(ru.UTF-8):	Утилиты управления сетью по SNMP из проекта NET-SNMP
Summary(uk.UTF-8):	Утиліти керування мережею по SNMP з проекту NET-SNMP
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-mibs = %{version}-%{release}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils

%description utils
This package contains various utilities for managing your network
using the SNMP protocol.

%description utils -l es.UTF-8
Varios utilitarios para uso con el SNMP de la UCD. Contiene
utilitarios como: snmpwalk, snmptest y otros.

%description utils -l pl.UTF-8
Różnego rodzaju narzędzia do zarządzania siecią przy użyciu protokołu
SNMP.

%description utils -l pt_BR.UTF-8
Vários utilitários para uso com o SNMP da UCD. Contém utilitários
como: snmpwalk, snmptest e outros.

%description utils -l ru.UTF-8
Пакет ucd-snmp-utils содержит разнообразные утилиты для использования
в проекте управления сетью net-snmp.

%description utils -l uk.UTF-8
Пакет ucd-snmp-utils містить різноманітні утиліти для використання в
проекті керування мережею net-snmp.

%package -n perl-SNMP
Summary:	SNMP and NetSNMP::* Perl modules
Summary(pl.UTF-8):	Moduły Perla SNMP oraz NetSNMP::*
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	ucd-snmp-utils-perl

%description -n perl-SNMP
SNMP and NetSNMP::* Perl modules - Perl interface to net-snmp.

%description -n perl-SNMP -l pl.UTF-8
Moduły Perla SNMP oraz NetSNMP::* - perlowy interfejs do net-snmp.

%package utils-perl
Summary:	Perl utilities for network management using SNMP
Summary(pl.UTF-8):	Perlowe narzędzia używające protokołu SNMP
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils-perl

%description utils-perl
This package contains various Perl utilities for managing your network
using the SNMP protocol.

%description utils-perl -l pl.UTF-8
Perlowe narzędzia do zarządzania siecią przy użyciu protokołu SNMP.

%package snmpconf
Summary:	snmpconf - creating and modifying SNMP configuration files
Summary(pl.UTF-8):	snmpconf - tworzenie i modyfikowanie plików konfiguracyjnych SNMP
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	perl-SNMP = %{version}-%{release}

%description snmpconf
snmpconf is a simple Perl script that walks you through setting up a
configuration file step by step. It should be fairly straight forward
to use.

%description snmpconf -l pl.UTF-8
snmpconf to prosty skrypt Perla pozwalający na tworzenie pliku
konfiguracyjnego krok po kroku. Powinien być w miarę prosty w użyciu.

%package tkmib
Summary:	MIB browser in Tk
Summary(pl.UTF-8):	Przeglądarka MIB-ów w Tk
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Requires:	perl-Tk

%description tkmib
MIB browser in Tk.

%description tkmib -l pl.UTF-8
Przeglądarka MIB-ów w Tk.

%package -n python-netsnmp
Summary:	Python netsnmp extension module
Summary(pl.UTF-8):	Moduł rozszerzenia netsnmp dla Pythona
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-netsnmp
The 'netsnmp' Python extension module provides a full featured,
tri-lingual SNMP (SNMPv3, SNMPv2c, SNMPv1) client API.

%description -n python-netsnmp -l pl.UTF-8
Moduł rozszerzenia netsnmp dla Pythona udostępnia pełne API klienckie
SNMP dla trzech wersji tego protokołu (SNMPv3, SNMPv2c, SNMPv1).

%prep
%setup -q -a7
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-debugging \
	--enable-as-needed \
	%{!?with_static_libs:--disable-static} \
	--with-cflags="%{rpmcflags} -I/usr/include/et" \
	--with-ldflags="%{rpmldflags}" \
	--with-defaults \
	--with-default-snmp-version=3 \
	%{?with_kerberos5:--with-krb5=%{_prefix}} \
	%{!?with_kerberos5:--without-krb5} \
	--with-openssl=%{_prefix} \
	--with-libwrap=%{_prefix} \
	--with-logfile="%{logfile}" \
	--with-zlib=%{_prefix} \
	--with-bzip2=%{_prefix} \
	--with%{!?with_perl:out}-perl-modules \
	--with%{!?with_python:out}-python-modules \
	--enable-local-smux \
	--with-mib-modules="host agentx smux mibII/mta_sendmail \
%ifarch %{ix86} %{x8664}
%if %{with lm_sensors}
			ucd-snmp/lmSensors \
%endif
%endif
			disman/event disman/schedule ucd-snmp/diskio \
			target misc/ipfwacc" \
	%{?with_kerberos5:--with-security-modules="ksm"} \
	--with-sys-contact="root@localhost" \
	--with-sys-location="Unknown" \
	--with-transports="UDP UDPIPv6 TCP TCPIPv6 Unix Callback" \
	--with-persistent-directory="/var/lib/net-snmp" \
	--enable-ucd-snmp-compatibility \
	--enable-ipv6 \
	--with%{!?with_rpm:out}-rpm

%{__make} -j1

cd perl

%{__perl} Makefile.PL \
	-NET-SNMP-IN-SOURCE=true \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}" \
	</dev/null

# avoid rpaths generated by MakeMaker
perl -pi -e 's@LD_RUN_PATH="\$\(LD_RUN_PATH\)" @@' */Makefile */*/Makefile

%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig,snmp},/var/log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.conf
:> $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.local.conf
:> $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmp.conf
:> $RPM_BUILD_ROOT%{logfile}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/snmpd
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/snmpd

install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/snmptrapd
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmptrapd.conf
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/snmptrapd

#install agent/mibgroup/ipfwchains/IPFWCHAINS-MIB.txt \
#	$RPM_BUILD_ROOT%{_datadir}/snmp/mibs

cd perl
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/perl-SNMP-%{version}
install SNMP/examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/perl-SNMP-%{version}
cd ..

# IP-Filter (non-Linux)
rm -f $RPM_BUILD_ROOT%{_bindir}/ipf-mod.pl

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Bundle/Makefile.subs.pl
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Bundle/NetSNMP/.packlist

%if %{with static_libs}
# hack: convert DynaLoader.a inside .a file to .o, as strip(1) would otherwise say invalid argument
for a in $RPM_BUILD_ROOT%{_libdir}/libnet*.a; do
	rm -f *.o *.a
	ar x $a DynaLoader.a
	if [ -f DynaLoader.a ]; then
		ar x DynaLoader.a
		ar cr $a DynaLoader.o
		ar d $a DynaLoader.a
		# remove second file too
		ar d $a DynaLoader.a
	fi
done
%else
rm -f $RPM_BUILD_ROOT%{_libdir}/libsnmp.a
%endif

%if %{with python}
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/netsnmp/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/netsnmp/*.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch %{logfile}
chmod 640 %{logfile}
/sbin/chkconfig --add snmpd
%service snmpd restart "snmpd daemon"

%preun
if [ "$1" = "0" ]; then
	%service snmpd stop
	/sbin/chkconfig --del snmpd
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%triggerpostun -- ucd-snmp
/sbin/chkconfig --add snmpd

%post snmptrapd
touch %{logfile}
chmod 640 %{logfile}
/sbin/chkconfig --add snmptrapd
%service snmptrapd restart "snmp trap daemon"

%preun snmptrapd
if [ "$1" = "0" ]; then
	%service snmptrapd stop
	/sbin/chkconfig --del snmptrapd
fi

%triggerpostun snmptrapd -- ucd-snmp-snmptrapd
/sbin/chkconfig --add snmptrapd

%files
%defattr(644,root,root,755)
%doc README local
%doc ChangeLog EXAMPLE.conf.def EXAMPLE.conf
%doc FAQ NEWS PORTING README.snmpv3 TODO AGENT.txt

%attr(754,root,root) /etc/rc.d/init.d/snmpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/snmpd

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmpd.conf
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmpd.local.conf

%attr(755,root,root) %{_sbindir}/snmpd

%{_mandir}/man5/snmpd.conf.5*
%{_mandir}/man5/snmpd.examples.5*
%{_mandir}/man5/snmpd.internal.5*
%{_mandir}/man5/variables.5*
%{_mandir}/man8/snmpd.8*

%attr(640,root,root) %ghost %{logfile}

%files libs
%defattr(644,root,root,755)
%dir %{_sysconfdir}/snmp
%attr(755,root,root) %{_libdir}/libnetsnmp.so.*.*
%attr(755,root,root) %{_libdir}/libnetsnmpagent.so.*.*
%attr(755,root,root) %{_libdir}/libnetsnmphelpers.so.*.*
%attr(755,root,root) %{_libdir}/libnetsnmpmibs.so.*.*
%attr(755,root,root) %{_libdir}/libnetsnmptrapd.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetsnmp.so.15
%attr(755,root,root) %ghost %{_libdir}/libnetsnmpagent.so.15
%attr(755,root,root) %ghost %{_libdir}/libnetsnmphelpers.so.15
%attr(755,root,root) %ghost %{_libdir}/libnetsnmpmibs.so.15
%attr(755,root,root) %ghost %{_libdir}/libnetsnmptrapd.so.15

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mib2c
%attr(755,root,root) %{_bindir}/mib2c-update
%attr(755,root,root) %{_bindir}/net-snmp-config
%attr(755,root,root) %{_libdir}/libnetsnmp.so
%attr(755,root,root) %{_libdir}/libnetsnmpagent.so
%attr(755,root,root) %{_libdir}/libnetsnmphelpers.so
%attr(755,root,root) %{_libdir}/libnetsnmpmibs.so
%attr(755,root,root) %{_libdir}/libnetsnmptrapd.so
%{_libdir}/libnetsnmp.la
%{_libdir}/libnetsnmpagent.la
%{_libdir}/libnetsnmphelpers.la
%{_libdir}/libnetsnmpmibs.la
%{_libdir}/libnetsnmptrapd.la
%{_includedir}/net-snmp
%{_datadir}/snmp/mib2c*
%{_mandir}/man1/mib2c.1*
%{_mandir}/man1/mib2c-update.1*
%{_mandir}/man1/net-snmp-config.1*
%{_mandir}/man3/[!NS]*
%{_mandir}/man5/mib2c.conf.5*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libnet*.a
%endif

%files compat-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnmp.so
%{_libdir}/libsnmp.la
%{_includedir}/ucd-snmp

%if %{with static_libs}
%files compat-static
%defattr(644,root,root,755)
%{_libdir}/libsnmp.a
%endif

%files mibs
%defattr(644,root,root,755)
%dir %{_datadir}/snmp
%{_datadir}/snmp/mibs

%files snmptrapd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/snmptrapd
%attr(754,root,root) /etc/rc.d/init.d/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmptrapd.conf
%if %{with perl}
%attr(755,root,root) %{_datadir}/snmp/snmp_perl_trapd.pl
%endif
%{_mandir}/man5/snmptrapd.conf.5*
%{_mandir}/man8/snmptrapd.8*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encode_keychange
%attr(755,root,root) %{_bindir}/snmpbulkget
%attr(755,root,root) %{_bindir}/snmpbulkwalk
%attr(755,root,root) %{_bindir}/snmpdelta
%attr(755,root,root) %{_bindir}/snmpdf
%attr(755,root,root) %{_bindir}/snmpget
%attr(755,root,root) %{_bindir}/snmpgetnext
%attr(755,root,root) %{_bindir}/snmpinform
%attr(755,root,root) %{_bindir}/snmpnetstat
%attr(755,root,root) %{_bindir}/snmpset
%attr(755,root,root) %{_bindir}/snmpstatus
%attr(755,root,root) %{_bindir}/snmptable
%attr(755,root,root) %{_bindir}/snmptest
%attr(755,root,root) %{_bindir}/snmptranslate
%attr(755,root,root) %{_bindir}/snmptrap
%attr(755,root,root) %{_bindir}/snmpusm
%attr(755,root,root) %{_bindir}/snmpvacm
%attr(755,root,root) %{_bindir}/snmpwalk
%{_mandir}/man1/encode_keychange.1*
%{_mandir}/man1/snmpbulkget.1*
%{_mandir}/man1/snmpbulkwalk.1*
%{_mandir}/man1/snmpcmd.1*
%{_mandir}/man1/snmpdelta.1*
%{_mandir}/man1/snmpdf.1*
%{_mandir}/man1/snmpget.1*
%{_mandir}/man1/snmpgetnext.1*
%{_mandir}/man1/snmpinform.1*
%{_mandir}/man1/snmpnetstat.1*
%{_mandir}/man1/snmpset.1*
%{_mandir}/man1/snmpstatus.1*
%{_mandir}/man1/snmptable.1*
%{_mandir}/man1/snmptest.1*
%{_mandir}/man1/snmptranslate.1*
%{_mandir}/man1/snmptrap.1*
%{_mandir}/man1/snmpusm.1*
%{_mandir}/man1/snmpvacm.1*
%{_mandir}/man1/snmpwalk.1*
%{_mandir}/man5/snmp.conf.5*
%{_mandir}/man5/snmp_config.5*

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmp.conf

%if %{with perl}
%files -n perl-SNMP
%defattr(644,root,root,755)
%doc perl/SNMP/{BUG,README,TODO} perl/SNMP/examples
%{perl_vendorarch}/SNMP.pm
%{perl_vendorarch}/NetSNMP
%dir %{perl_vendorarch}/auto/SNMP
%{perl_vendorarch}/auto/SNMP/autosplit.ix
%{perl_vendorarch}/auto/SNMP/SNMP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/SNMP/SNMP.so
%dir %{perl_vendorarch}/auto/NetSNMP
%dir %{perl_vendorarch}/auto/NetSNMP/*
%{perl_vendorarch}/auto/NetSNMP/*/autosplit.ix
%{perl_vendorarch}/auto/NetSNMP/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NetSNMP/*/*.so
%dir %{perl_vendorarch}/auto/NetSNMP/agent/default_store
%{perl_vendorarch}/auto/NetSNMP/agent/default_store/autosplit.ix
%{perl_vendorarch}/auto/NetSNMP/agent/default_store/default_store.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NetSNMP/agent/default_store/default_store.so
%{_mandir}/man3/NetSNMP::*.3*
%{_mandir}/man3/SNMP.3*
%{_examplesdir}/perl-SNMP-%{version}

%files utils-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fixproc
%attr(755,root,root) %{_bindir}/snmpcheck
%attr(755,root,root) %{_bindir}/traptoemail
%{_mandir}/man1/fixproc.1*
%{_mandir}/man1/traptoemail.1*
%endif

%files snmpconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/snmpconf
%{_mandir}/man1/snmpconf.1*
%{_datadir}/snmp/snmpconf-data

%if %{with perl}
%files tkmib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tkmib
%{_mandir}/man1/tkmib.1*
%endif

%if %{with python}
%files -n python-netsnmp
%defattr(644,root,root,755)
%dir %{py_sitedir}/netsnmp
%attr(755,root,root) %{py_sitedir}/netsnmp/*.so
%{py_sitedir}/netsnmp/*.py[co]
%endif
