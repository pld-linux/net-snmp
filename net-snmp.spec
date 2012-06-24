# TODO:
# - Summary and %%description in all packages
# - init scripts
# - default configs
# - perl module 
# - review %%files (add missing)
# - review Requires:
# - review Obsoletes:
# - review Provides:
# - review ucd patches:
# -- link_libsnmp_with_libcrypto
# -- noinstalled
# -- ia64
# -- include-netinet_in_h
# -- dlopen-fix
# -- glibc21
# -- manpage
# -- no_libelf
# -- init_master-libwrap
%include	/usr/lib/rpm/macros.perl
Summary:	A collection of SNMP protocol tools
Summary(es):	Agente SNMP de la UCD
Summary(pl):	Kolekcja narz�dzi do obs�ugi protoko�u SNMP
Summary(pt_BR):	Agente SNMP da UCD
Summary(ru):	����� ������ ��� ��������� SNMP �� UC-Davis
Summary(uk):	��¦� ���̦� ��� ��������� SNMP צ� UC-Davis
Name:		net-snmp
Version:	5.0.7
Release:	0.1
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/net-snmp/%{name}-%{version}.tar.gz
Source1:	%{name}d.init
Source2:	%{name}d.conf
Source3:	%{name}d.sysconfig
Source4:	%{name}trapd.init
Source5:	%{name}trapd.conf
Source6:	%{name}trapd.sysconfig
Source7:	ftp://ucd-snmp.ucdavis.edu/contrib/ucd-ipchains.tar.gz
Patch0:		%{name}-acinclude.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-rpm-implicit-libs.patch
Patch3:		%{name}-DESTDIR.patch
URL:		http://www.net-snmp.org/
BuildRequires:	autoconf >= 2.57-3
BuildRequires:	automake
BuildRequires:	libtool >= 1.4
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-devel >= 4.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
PreReq:		rc-scripts >= 0.2.0
PreReq:		%{name}-libs = %{version}
Requires(post,preun):	/sbin/chkconfig
Requires:	/usr/bin/setsid
Provides:	snmpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	cmu-snmp
Obsoletes:	snmpd
Obsoletes:	ucd-snmp

%define		_sysconfdir	/etc
%define		logfile		/var/log/snmpd.log

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management (hence the name). The UCD-SNMP project includes
various SNMP tools: an extensible agent, an SNMP library, tools for
requesting or setting information from SNMP agents, tools for
generating and handling SNMP traps, a version of the netstat command
which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd daemon, documentation, etc.

Install the ucd-snmp package if you need network management tools. You
will probably also want to install the ucd-snmp-utils package, which
contains UCD-SNMP utilities.

%description -l es
Este paquete se deriva de la implementaci�n del Protocolo Simple de
Gesti�n de Redes versi�n 2 (SNMPv2) de la Universidad Carnegie Mellon.
�til para administrar redes y hacer contabilidad.

%description -l pl
SNMP (Simple Network Management Protocol) jest protoko�ej u�ywanym do
zarz�dzania sieciami. Pakiet zawiera narz�dzia: rozbudowywalnego
agenta, bibliotek� SNMP, narz�dzia do odpytywania oraz ustawiania
informacji poprzez agent�w SNMP, narz�dzia do generowania i obs�ugi
pu�apek SNMP, wersj� komendy netstat u�ywaj�c� SNMP, przegl�dark� mib
w Tk/Perl, deamona, dokumentacj� itp.

%description -l pt_BR
Este pacote � derivado da implementa��o do Protocolo Simples de
Gerenciamento de Redes vers�o 2 (SNMPv2) da Universidade Carnegie
Mellon. �til para gerenciar redes e fazer contabilidade.

%description -l ru
SNMP (Simple Network Management Protocol) - ��� ��������, ������������
��� ���������� ����� (������ � ��������). ������ UCD-SNMP ��������
������������� SNMP-�������: ����������� �����, ���������� SNMP,
������� ��� ������� ��� ��������� ���������� �� SNMP-�������, �������
��� ��������� � ��������� SNMP-������, ������ ������� netstat,
������������ SNMP, � mib-������� �� Tk/Perl. ���� ����� ��������
������ snmpd � snmptrapd, ������������ � �.�.

%description -l uk
SNMP (Simple Network Management Protocol) - �� ��������, ����
�������������� ��� ��������� ������� (�צ��� � �����). ������ UCD-SNMP
ͦ����� Ҧ�����Φ�Φ SNMP-���̦��: ������������ �����, ¦�̦�����
SNMP, ���̦�� ��� ������� �� ������������ �������æ� צ� NMP-����Ԧ�,
���̦�� ��� ������æ� �� ������� SNMP-���Ц�, ���Ӧ� ������� netstat,
��� ����������դ SNMP, �� mib-������� �� Tk/Perl. ��� ����� ͦ�����
������ snmpd �� snmptrapd, ���������æ� � �.�.

%package libs
Summary:	NET SNMP libraries
Summary(pl):	Biblioteki SNMP
Group:		Libraries
Obsoletes:	ucd-snmp-libs
Requires:	%{name}-mibs = %{version}

%description libs
NET SNMP libraries.

%description libs -l pl
Biblioteki SNMP.

%package compat-libs
Summary:	UCD SNMP libraries
Summary(pl):	Biblioteki SNMP
Group:		Libraries
Obsoletes:	ucd-snmp-libs
Requires:	%{name}-mibs = %{version}

%description compat-libs
UCD SNMP libraries.

%description compat-libs -l pl
Biblioteki SNMP.

%package mibs
Summary:	MIB database
Group:		Applications/System

%description mibs
MIB database

%package utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Summary(es):	Utilitarios del SNMP de la UCD
Summary(pl):	Narz�dzia u�ywaj�ce protoko�u SNMP
Summary(pt_BR):	Utilit�rios do SNMP da UCD
Summary(ru):	������� ���������� ����� �� SNMP �� ������� NET-SNMP
Summary(uk):	���̦�� ��������� ������� �� SNMP � ������� NET-SNMP
Group:		Applications/System
Requires:	%{name}-libs = %{version}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils

%description utils
The ucd-snmp package contains various utilities for use with the
UCD-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You'll also need to install the ucd-snmp
package.

%description utils -l es
Varios utilitarios para uso con el SNMP de la UCD. Contiene
utilitarios como: snmpwalk, snmptest y otros.

%description utils -l pl
R�nego rodzaju narz�dzia do u�ytku z programem %{name}.

%description utils -l pt_BR
V�rios utilit�rios para uso com o SNMP da UCD. Cont�m utilit�rios
como: snmpwalk, snmptest e outros.

%description utils -l ru
����� ucd-snmp-utils �������� ������������� ������� ��� �������������
� ������� ���������� ����� UCD-SNMP.

%description utils -l uk
����� ucd-snmp-utils ͦ����� Ҧ�����Φ�Φ ���̦�� ��� ������������ �
�����Ԧ ��������� ������� UCD-SNMP.

%package utils-perl
Summary:	Network management utilities using SNMP, from the UCD-SNMP project
Summary(pl):	Narz�dzia u�ywaj�ce protoko�u SNMP
Group:		Applications/System
Requires:	%{name} = %{version}
Requires:	perl-Term-ReadKey
Requires:	perl-Tk
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils-perl

%description utils-perl
The ucd-snmp package contains various utilities for use with the
UCD-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You'll also need to install the ucd-snmp
package.

%description utils-perl -l pl
R�nego rodzaju narz�dzia do u�ytku z programem %{name}.

%package snmptrapd
Summary:	SNMP trap daemon
Summary(pl):	Demon obs�uguj�cy pu�apki SNMP
Group:		Applications/System
PreReq:		%{name} = %{version}
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.2.0
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-snmptrapd

%description snmptrapd
The ucd-snmp-snmptrapd package contains snmp trap daemon.

%description snmptrapd -l pl
Pakiet zawiera demon obs�uguj�cy pu�apki SNMP.

%package devel
Summary:	The development environment for the UCD-SNMP project
Summary(es):	Archivos de inclusi�n y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla developer�w u�ywaj�cych %{name}
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	����� ���������� ��� ������� UCD-SNMP
Summary(uk):	���������� �������� ��� ������� UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Requires:	openssl-devel
Obsoletes:	ucd-snmp-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

Install the ucd-snmp-devel package if you would like to develop
applications for use with the UCD-SNMP project's network management
tools. You'll also need to have the ucd-snmp and ucd-snmp-utils
packages installed.

%description devel -l es
Estas son las bibliotecas y archivos de inclusi�n para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creaci�n de
programas para uso en la gesti�n de redes.

%description devel -l pl
Pakiet zawiera pliki nag��wkowe i bilioteki potrzebne do rozwoju
aplikacji u�ywaj�cych protoko�u SNMP.

%description devel -l pt_BR
Estas s�o as bibliotecas e arquivos de inclus�o para desenvolvimento
com o SNMP da UCD. Com este pacote � poss�vel a cria��o de programas
para uso no gerenciamento de redes.

%description devel -l ru
����� ucd-snmp-devel �������� ���������� ������������ � ������ ���
������������� � ��������� ���������� ����� ������� UCD-SNMP.

%description devel -l uk
����� ucd-snmp-devel ͦ����� ¦�̦����� ������ͦ��� �� ������ ���
������������ � ���̦���� ��������� ������� ������� UCD-SNMP.

%package static
Summary:	Static UCD-SNMP libraries
Summary(es):	Static libraries for ucd-snmp development
Summary(pl):	Statyczne biblioteki %{name}
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com ucd-snmp
Summary(ru):	����������� ���������� ��� ������� UCD-SNMP
Summary(uk):	������Φ ¦�̦����� ��� ������� UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	ucd-snmp-static

%description static
Static UCD-SNMP libraries.

%description static -l es
Static libraries for ucd-snmp development

%description static -l pl
Statyczne biblioteki %{name}.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com ucd-snmp

%package compat-devel
Summary:	The development environment for the UCD-SNMP project
Summary(es):	Archivos de inclusi�n y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla developer�w u�ywaj�cych %{name}
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	����� ���������� ��� ������� UCD-SNMP
Summary(uk):	���������� �������� ��� ������� UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-compat-libs = %{version}
Requires:	openssl-devel
Obsoletes:	cmu-snmp-devel
Obsoletes:	ucd-snmp-devel

%description compat-devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

Install the ucd-snmp-devel package if you would like to develop
applications for use with the UCD-SNMP project's network management
tools. You'll also need to have the ucd-snmp and ucd-snmp-utils
packages installed.

%description compat-devel -l es
Estas son las bibliotecas y archivos de inclusi�n para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creaci�n de
programas para uso en la gesti�n de redes.

%description compat-devel -l pl
Pakiet zawiera pliki nag��wkowe i bilioteki potrzebne do rozwoju
aplikacji u�ywaj�cych protoko�u SNMP.

%description compat-devel -l pt_BR
Estas s�o as bibliotecas e arquivos de inclus�o para desenvolvimento
com o SNMP da UCD. Com este pacote � poss�vel a cria��o de programas
para uso no gerenciamento de redes.

%description compat-devel -l ru
����� ucd-snmp-devel �������� ���������� ������������ � ������ ���
������������� � ��������� ���������� ����� ������� UCD-SNMP.

%description compat-devel -l uk
����� ucd-snmp-devel ͦ����� ¦�̦����� ������ͦ��� �� ������ ���
������������ � ���̦���� ��������� ������� ������� UCD-SNMP.

%package compat-static
Summary:	Static UCD-SNMP libraries
Summary(es):	Static libraries for ucd-snmp development
Summary(pl):	Statyczne biblioteki %{name}
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com ucd-snmp
Summary(ru):	����������� ���������� ��� ������� UCD-SNMP
Summary(uk):	������Φ ¦�̦����� ��� ������� UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-compat-devel = %{version}
Obsoletes:	ucd-snmp-static

%description compat-static
Static UCD-SNMP libraries.

%description compat-static -l es
Static libraries for ucd-snmp development

%description compat-static -l pl
Statyczne biblioteki %{name}.

%description compat-static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com ucd-snmp

%package snmpconf
Summary:	snmpconf
Group:		Applications/System

%description snmpconf
snmpconf

%package tkmib
Summary:	MIB browser in TK
Group:		Applications/System

%description tkmib
MIB browser in TK

%prep
%setup -q -a7
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure \
	--with-logfile="%{logfile}" \
	--with-cflags="%{rpmcflags} -I%{_includedir}/rpm" \
	--with-ldflags="%{rpmldflags}" \
	--with-transports="UDP UDPIPv6 TCP TCPIPv6 Unix Callback " \
	--with-sys-location="Unknown" \
	--with-mib-modules="host disman/event-mib smux mibII/mta_sendmail \
		agentx target misc/ipfwacc tunnel" \
	--with-libwrap=%{_prefix} \
	--with-openssl=%{_prefix} \
	--disable-debugging \
	--with-persistent-directory="/var/lib/net-snmp" \
	--enable-ipv6 \
	--enable-reentrant \
	--with-sys-contact="root@localhost" \
	--enable-ucd-snmp-compatibility \
	--with-defaults \
	--with-default-snmp-version=3 \
	--enable-shared
# ucd-snmp/diskio
%{__make}

# symlinks to allow build perl module w/o installed ucd-snmp
#ln -sf snmplib ucd-snmp
#ln -sf ../ucd-snmp-config.h ucd-snmp/ucd-snmp-config.h
#cd perl/SNMP
#echo "%{_datadir}/snmp/mibs" | perl Makefile.PL
#%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{snmp,rc.d/init.d,sysconfig},/var/log}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.conf
#:> $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.local.conf
:> $RPM_BUILD_ROOT%{logfile}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/snmpd
#install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.conf
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/snmpd

install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/snmptrapd
#install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmptrapd.conf
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/snmptrapd

#install agent/mibgroup/ipfwchains/IPFWCHAINS-MIB.txt \
#	$RPM_BUILD_ROOT%{_datadir}/snmp/mibs

#cd perl/SNMP
#%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add snmpd
if [ -f /var/lock/subsys/snmpd ]; then
	/etc/rc.d/init.d/snmpd restart >&2
else
	echo "Run \"/etc/rc.d/init.d/snmpd start\" to start snmpd daemon." >&2
fi
touch %{logfile}
chmod 640 %{logfile}

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/snmpd ]; then
		/etc/rc.d/init.d/snmpd stop >&2
	fi
	/sbin/chkconfig --del snmpd
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post snmptrapd
/sbin/chkconfig --add snmptrapd
if [ -f /var/lock/subsys/snmptrapd ]; then
	/etc/rc.d/init.d/snmptrapd restart >&2
else
	echo "Run \"/etc/rc.d/init.d/snmptrapd start\" to start snmp trap daemon." >&2
fi
touch %{logfile}
chmod 640 %{logfile}

%preun snmptrapd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/snmptrapd ]; then
		/etc/rc.d/init.d/snmptrapd stop >&2
	fi
	/sbin/chkconfig --del snmptrapd
fi

%files
%defattr(644,root,root,755)
%doc README local
%doc ChangeLog EXAMPLE.conf.def EXAMPLE.conf
%doc FAQ NEWS PORTING README.snmpv3 TODO AGENT.txt

%attr(754,root,root) /etc/rc.d/init.d/snmpd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/snmpd

%dir %{_sysconfdir}/snmp
#%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmpd.conf
#%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmpd.local.conf

%attr(755,root,root) %{_sbindir}/snmpd

%{_mandir}/man1/snmpd.1*
%{_mandir}/man5/snmpd.conf.5*
%{_mandir}/man5/variables.5*

%attr(640,root,root) %ghost %{logfile}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnet*.so.*.*

%dir %{_datadir}/snmp

%files mibs
%defattr(644,root,root,755)
%{_datadir}/snmp/mibs

%files compat-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnmp.so.*.*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/encode_keychange
%attr(755,root,root) %{_bindir}/snmpbulkget
%attr(755,root,root) %{_bindir}/snmpbulkwalk
%attr(755,root,root) %{_bindir}/snmpdelta
%attr(755,root,root) %{_bindir}/snmpget
%attr(755,root,root) %{_bindir}/snmpgetnext
%attr(755,root,root) %{_bindir}/snmpnetstat
%attr(755,root,root) %{_bindir}/snmpset
%attr(755,root,root) %{_bindir}/snmpstatus
%attr(755,root,root) %{_bindir}/snmptable
%attr(755,root,root) %{_bindir}/snmptest
%attr(755,root,root) %{_bindir}/snmptranslate
%attr(755,root,root) %{_bindir}/snmptrap
%attr(755,root,root) %{_bindir}/snmpusm
%attr(755,root,root) %{_bindir}/snmpwalk
%attr(755,root,root) %{_bindir}/snmpdf
%attr(755,root,root) %{_bindir}/snmpinform
%attr(755,root,root) %{_bindir}/snmpvacm

#%{_datadir}/snmp/snmpconf/snmp.conf

%{_mandir}/man1/snmpbulkget.1*
%{_mandir}/man1/snmpbulkwalk.1*
%{_mandir}/man1/snmpcmd.1*
%{_mandir}/man1/snmpdelta.1*
%{_mandir}/man1/snmpget.1*
%{_mandir}/man1/snmpgetnext.1*
%{_mandir}/man1/snmpnetstat.1*
%{_mandir}/man1/snmpset.1*
%{_mandir}/man1/snmpstatus.1*
%{_mandir}/man1/snmptable.1*
%{_mandir}/man1/snmptest.1*
%{_mandir}/man1/snmptranslate.1*
%{_mandir}/man1/snmptrap.1*
%{_mandir}/man1/snmpusm.1*
%{_mandir}/man1/snmpwalk.1*
%{_mandir}/man1/snmpdf.1*
%{_mandir}/man1/snmpinform.1*
%{_mandir}/man5/snmp.conf.5*
%{_mandir}/man5/snmp_config.5*

%files utils-perl
%defattr(644,root,root,755)
#%doc perl/SNMP/{BUG,README,TODO} perl/SNMP/examples
%attr(755,root,root) %{_bindir}/snmpcheck
%attr(755,root,root) %{_bindir}/snmpconf
%{_mandir}/man1/snmpconf.1*
%{_datadir}/snmp/snmpconf-data
#%{perl_sitearch}/SNMP.pm
#%dir %{perl_sitearch}/auto/SNMP
#%{perl_sitearch}/auto/SNMP/autosplit.ix
#%{perl_sitearch}/auto/SNMP/SNMP.bs
#%attr(755,root,root) %{perl_sitearch}/auto/SNMP/SNMP.so

%files snmptrapd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/snmptrapd
%attr(754,root,root) /etc/rc.d/init.d/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/snmptrapd
#%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmptrapd.conf
%{_mandir}/man5/snmptrapd.conf.5*
%{_mandir}/man8/snmptrapd.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mib2c
%attr(755,root,root) %{_bindir}/net-snmp-config
%attr(755,root,root) %{_libdir}/libnet*[a-z].so
%{_libdir}/libnet*.la
%{_includedir}/net-snmp
%{_datadir}/snmp/mib2c*
%{_mandir}/man1/mib2c.1*
%{_mandir}/man3/*

%files compat-devel
%defattr(644,root,root,755)
%{_libdir}/libsnmp.la
%attr(755,root,root) %{_libdir}/libsnmp.so
%{_includedir}/ucd-snmp

%files static
%defattr(644,root,root,755)
%attr(0644,root,root) %{_libdir}/libnet*.a

%files compat-static
%defattr(644,root,root,755)
%attr(0644,root,root) %{_libdir}/libsnmp.a

%files tkmib
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/tkmib
