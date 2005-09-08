# TODO:
# - init scripts (which, what?)
# - default configs
# - review ucd-snmp-ia64.patch patch
# - security http://security.gentoo.org/glsa/glsa-200505-18.xml
# - security http://security.gentoo.org/glsa/glsa-200509-05.xml
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages only for deps resolving
#
%include	/usr/lib/rpm/macros.perl
Summary:	A collection of SNMP protocol tools
Summary(es):	Agente SNMP de la UCD
Summary(pl):	Kolekcja narzêdzi do obs³ugi protoko³u SNMP
Summary(pt_BR):	Agente SNMP da UCD
Summary(ru):	îÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÐÒÏÔÏËÏÌÁ SNMP ÏÔ UC-Davis
Summary(uk):	îÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ÐÒÏÔÏËÏÌÕ SNMP ×¦Ä UC-Davis
Name:		net-snmp
Version:	5.2.1.2
Release:	0.2
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/net-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	34159770a7fe418d99fdd416a75358b1
Source1:	%{name}d.init
Source2:	%{name}d.conf
Source3:	%{name}d.sysconfig
Source4:	%{name}trapd.init
Source5:	%{name}trapd.conf
Source6:	%{name}trapd.sysconfig
Source7:	ftp://ucd-snmp.ucdavis.edu/contrib/ucd-ipchains.tar.gz
# Source7-md5:	29949f1008f1a04d6efefd5b3ea607da
Source8:	http://juniper.net/techpubs/software/junos/junos71/juniper-mibs-7.1R1.3.tgz
# Source8-md5:	fa5b9a2a3b93c6c5a5994ac7f36b5bf9
Patch0:		%{name}-acinclude.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-rpm-implicit-libs.patch
Patch3:		%{name}-config-noflags.patch
Patch4:		%{name}-dlopen-fix.patch
Patch5:		%{name}-manpage.patch
Patch6:		%{name}-link.patch
Patch7:		%{name}-llinterfaces.patch
Patch8:		%{name}-usr_local_bin_perl.patch
Patch9:		%{name}-kernel_headers.patch
Patch10:	%{name}-syntax.patch
URL:		http://www.net-snmp.org/
BuildRequires:	autoconf >= 2.57-3
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	libtool >= 1.4
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_autodeps:BuildRequires:	perl-Term-ReadKey}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-devel >= 4.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.176
PreReq:		rc-scripts >= 0.2.0
PreReq:		%{name}-libs = %{version}-%{release}
Requires(post,preun):	/sbin/chkconfig
Requires:	/usr/bin/setsid
Provides:	snmpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	cmu-snmp
Obsoletes:	snmpd
Obsoletes:	ucd-snmp

%define		logfile		/var/log/snmpd.log

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management (hence the name). The net-snmp project includes
various SNMP tools: an extensible agent, an SNMP library, tools for
requesting or setting information from SNMP agents, tools for
generating and handling SNMP traps, a version of the netstat command
which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd daemon, documentation, etc.

%description -l es
Este paquete se deriva de la implementación del Protocolo Simple de
Gestión de Redes versión 2 (SNMPv2) de la Universidad Carnegie Mellon.
Útil para administrar redes y hacer contabilidad.

%description -l pl
SNMP (Simple Network Management Protocol) jest protoko³em u¿ywanym do
zarz±dzania sieciami. Pakiet zawiera narzêdzia: rozbudowywalnego
agenta, bibliotekê SNMP, narzêdzia do odpytywania oraz ustawiania
informacji poprzez agentów SNMP, narzêdzia do generowania i obs³ugi
pu³apek SNMP, wersjê komendy netstat u¿ywaj±c± SNMP, przegl±darkê mib
w Tk/Perl, demona, dokumentacjê itp.

%description -l pt_BR
Este pacote é derivado da implementação do Protocolo Simples de
Gerenciamento de Redes versão 2 (SNMPv2) da Universidade Carnegie
Mellon. Útil para gerenciar redes e fazer contabilidade.

%description -l ru
SNMP (Simple Network Management Protocol) - ÜÔÏ ÐÒÏÔÏËÏÌ, ÉÓÐÏÌØÚÕÅÍÙÊ
ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÓÅÔØÀ (ÏÔÓÀÄÁ É ÎÁÚ×ÁÎÉÅ). ðÒÏÅËÔ net-snmp ×ËÌÀÞÁÅÔ
ÒÁÚÎÏÏÂÒÁÚÎÙÅ SNMP-ÕÔÉÌÉÔÙ: ÒÁÓÛÉÒÑÅÍÙÊ ÁÇÅÎÔ, ÂÉÂÌÉÏÔÅËÁ SNMP,
ÕÔÉÌÉÔÙ ÄÌÑ ÚÁÐÒÏÓÁ ÉÌÉ ÕÓÔÁÎÏ×ËÉ ÉÎÆÏÒÍÁÃÉÉ ÏÔ SNMP-ÁÇÅÎÔÏ×, ÕÔÉÌÉÔÙ
ÄÌÑ ÇÅÎÅÒÁÃÉÉ É ÏÂÒÁÂÏÔËÉ SNMP-ÔÒÁÐÏ×, ×ÅÒÓÉÑ ËÏÍÁÎÄÙ netstat,
ÉÓÐÏÌØÚÕÀÝÅÊ SNMP, É mib-ÂÒÁÕÚÅÒ ÎÁ Tk/Perl. üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ
ÄÅÍÏÎÙ snmpd É snmptrapd, ÄÏËÕÍÅÎÔÁÃÉÀ É Ô.Ä.

%description -l uk
SNMP (Simple Network Management Protocol) - ÃÅ ÐÒÏÔÏËÏÌ, ÑËÉÊ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÍÅÒÅÖÅÀ (Ú×¦ÄÓÉ ¦ ÎÁÚ×Á). ðÒÏÅËÔ net-snmp
Í¦ÓÔÉÔØ Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ SNMP-ÕÔÉÌ¦ÔÉ: ÒÏÚÛÉÒÀ×ÁÎÉÊ ÁÇÅÎÔ, Â¦ÂÌ¦ÏÔÅËÁ
SNMP, ÕÔÉÌ¦ÔÉ ÄÌÑ ÚÁÐÒÏÓÕ ÔÁ ×ÓÔÁÎÏ×ÌÅÎÎÑ ¦ÎÆÏÒÍÁÃ¦§ ×¦Ä NMP-ÁÇÅÎÔ¦×,
ÕÔÉÌ¦ÔÉ ÄÌÑ ÇÅÎÅÒÁÃ¦§ ÔÁ ÏÂÒÏÂËÉ SNMP-ÔÒÁÐ¦×, ×ÅÒÓ¦Ñ ËÏÍÁÎÄÉ netstat,
ÑËÁ ×ÉËÏÒÉÓÔÏ×Õ¤ SNMP, ÔÁ mib-ÂÒÁÕÚÅÒ ÎÁ Tk/Perl. ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ
ÄÅÍÏÎÉ snmpd ÔÁ snmptrapd, ÄÏËÕÍÅÎÔÁÃ¦À ¦ Ô.¦.

%package libs
Summary:	NET SNMP libraries
Summary(pl):	Biblioteki SNMP
Group:		Libraries
Requires:	%{name}-mibs = %{version}-%{release}
Obsoletes:	net-snmp-compat-libs
Obsoletes:	ucd-snmp-libs

%description libs
NET SNMP libraries.

%description libs -l pl
Biblioteki SNMP.

%package devel
Summary:	The development environment for the net-snmp project
Summary(es):	Archivos de inclusión y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla programistów u¿ywaj±cych bibliotek net-snmp
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	óÒÅÄÁ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ ÐÒÏÅËÔÁ UCD-SNMP
Summary(uk):	óÅÒÅÄÏ×ÉÝÅ ÒÏÚÒÏÂËÉ ÄÌÑ ÐÒÏÅËÔÕ UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	elfutils-devel
Requires:	openssl-devel >= 0.9.7c
Obsoletes:	ucd-snmp-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the net-snmp project's network management
tools.

%description devel -l es
Estas son las bibliotecas y archivos de inclusión para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creación de
programas para uso en la gestión de redes.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe i biblioteki potrzebne do rozwoju
aplikacji u¿ywaj±cych protoko³u SNMP.

%description devel -l pt_BR
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
com o SNMP da UCD. Com este pacote é possível a criação de programas
para uso no gerenciamento de redes.

%description devel -l ru
ðÁËÅÔ ucd-snmp-devel ÓÏÄÅÒÖÉÔ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ É ÈÅÄÅÒÁ ÄÌÑ
ÉÓÐÏÌØÚÏ×ÁÎÉÑ Ó ÕÔÉÌÉÔÁÍÉ ÕÐÒÁ×ÌÅÎÉÑ ÓÅÔØÀ ÐÒÏÅËÔÁ net-snmp.

%description devel -l uk
ðÁËÅÔ ucd-snmp-devel Í¦ÓÔÉÔØ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÔÁ ÈÅÄÅÒÉ ÄÌÑ
×ÉËÏÒÉÓÔÁÎÎÑ Ú ÕÔÉÌ¦ÔÁÍÉ ËÅÒÕ×ÁÎÎÑ ÍÅÒÅÖÅÀ ÐÒÏÅËÔÕ net-snmp.

%package static
Summary:	Static net-snmp libraries
Summary(pl):	Statyczne biblioteki net-snmp
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com ucd-snmp
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÒÏÅËÔÁ net-snmp
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÒÏÅËÔÕ net-snmp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description static
Static net-snmp libraries.

%description static -l pl
Statyczne biblioteki net-snmp.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com net-snmp.

%package compat-devel
Summary:	The development environment for the UCD-SNMP project
Summary(es):	Archivos de inclusión y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla programistów u¿ywaj±cych bibliotek UCD-SNMP
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	óÒÅÄÁ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ ÐÒÏÅËÔÁ UCD-SNMP
Summary(uk):	óÅÒÅÄÏ×ÉÝÅ ÒÏÚÒÏÂËÉ ÄÌÑ ÐÒÏÅËÔÕ UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	openssl-devel >= 0.9.7d
Obsoletes:	cmu-snmp-devel
Obsoletes:	ucd-snmp-devel

%description compat-devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the UCD-SNMP project's network management
tools.

%description compat-devel -l es
Estas son las bibliotecas y archivos de inclusión para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creación de
programas para uso en la gestión de redes.

%description compat-devel -l pl
Pakiet zawiera pliki nag³ówkowe i biblioteki potrzebne do rozwoju
aplikacji u¿ywaj±cych protoko³u SNMP.

%description compat-devel -l pt_BR
Estas são as bibliotecas e arquivos de inclusão para desenvolvimento
com o SNMP da UCD. Com este pacote é possível a criação de programas
para uso no gerenciamento de redes.

%description compat-devel -l ru
ðÁËÅÔ ucd-snmp-devel ÓÏÄÅÒÖÉÔ ÂÉÂÌÉÏÔÅËÉ ÒÁÚÒÁÂÏÔÞÉËÁ É ÈÅÄÅÒÁ ÄÌÑ
ÉÓÐÏÌØÚÏ×ÁÎÉÑ Ó ÕÔÉÌÉÔÁÍÉ ÕÐÒÁ×ÌÅÎÉÑ ÓÅÔØÀ ÐÒÏÅËÔÁ UCD-SNMP.

%description compat-devel -l uk
ðÁËÅÔ ucd-snmp-devel Í¦ÓÔÉÔØ Â¦ÂÌ¦ÏÔÅËÉ ÐÒÏÇÒÁÍ¦ÓÔÁ ÔÁ ÈÅÄÅÒÉ ÄÌÑ
×ÉËÏÒÉÓÔÁÎÎÑ Ú ÕÔÉÌ¦ÔÁÍÉ ËÅÒÕ×ÁÎÎÑ ÍÅÒÅÖÅÀ ÐÒÏÅËÔÕ UCD-SNMP.

%package compat-static
Summary:	Static UCD-SNMP libraries
Summary(pl):	Statyczne biblioteki UCD-SNMP
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com ucd-snmp
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÐÒÏÅËÔÁ UCD-SNMP
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÐÒÏÅËÔÕ UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-compat-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description compat-static
Static UCD-SNMP libraries.

%description compat-static -l pl
Statyczne biblioteki UCD-SNMP.

%description compat-static -l pt_BR
Bibliotecas estáticas para desenvolvimento com ucd-snmp.

%package mibs
Summary:	MIB database
Summary(pl):	Baza danych MIB
Group:		Applications/System
Conflicts:	ucd-snmp-libs

%description mibs
MIB database.

%description mibs -l pl
Baza danych MIB.

%package snmptrapd
Summary:	SNMP trap daemon
Summary(pl):	Demon obs³uguj±cy pu³apki SNMP
Group:		Applications/System
PreReq:		%{name} = %{version}-%{release}
PreReq:		rc-scripts >= 0.2.0
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-snmptrapd

%description snmptrapd
The ucd-snmp-snmptrapd package contains snmp trap daemon.

%description snmptrapd -l pl
Pakiet zawiera demon obs³uguj±cy pu³apki SNMP.

%package utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Summary(es):	Utilitarios del SNMP de la UCD
Summary(pl):	Narzêdzia u¿ywaj±ce protoko³u SNMP
Summary(pt_BR):	Utilitários do SNMP da UCD
Summary(ru):	õÔÉÌÉÔÙ ÕÐÒÁ×ÌÅÎÉÑ ÓÅÔØÀ ÐÏ SNMP ÉÚ ÐÒÏÅËÔÁ NET-SNMP
Summary(uk):	õÔÉÌ¦ÔÉ ËÅÒÕ×ÁÎÎÑ ÍÅÒÅÖÅÀ ÐÏ SNMP Ú ÐÒÏÅËÔÕ NET-SNMP
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils

%description utils
This package contains various utilities for managing your network
using the SNMP protocol.

%description utils -l es
Varios utilitarios para uso con el SNMP de la UCD. Contiene
utilitarios como: snmpwalk, snmptest y otros.

%description utils -l pl
Ró¿nego rodzaju narzêdzia do zarz±dzania sieci± przy u¿yciu protoko³u
SNMP.

%description utils -l pt_BR
Vários utilitários para uso com o SNMP da UCD. Contém utilitários
como: snmpwalk, snmptest e outros.

%description utils -l ru
ðÁËÅÔ ucd-snmp-utils ÓÏÄÅÒÖÉÔ ÒÁÚÎÏÏÂÒÁÚÎÙÅ ÕÔÉÌÉÔÙ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ
× ÐÒÏÅËÔÅ ÕÐÒÁ×ÌÅÎÉÑ ÓÅÔØÀ net-snmp.

%description utils -l uk
ðÁËÅÔ ucd-snmp-utils Í¦ÓÔÉÔØ Ò¦ÚÎÏÍÁÎ¦ÔÎ¦ ÕÔÉÌ¦ÔÉ ÄÌÑ ×ÉËÏÒÉÓÔÁÎÎÑ ×
ÐÒÏÅËÔ¦ ËÅÒÕ×ÁÎÎÑ ÍÅÒÅÖÅÀ net-snmp.

%package -n perl-SNMP
Summary:	SNMP and NetSNMP::* Perl modules
Summary(pl):	Modu³y Perla SNMP oraz NetSNMP::*
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	ucd-snmp-utils-perl

%description -n perl-SNMP
SNMP and NetSNMP::* Perl modules - Perl interface to net-snmp.

%description -n perl-SNMP -l pl
Modu³y Perla SNMP oraz NetSNMP::* - perlowy interfejs do net-snmp.

%package utils-perl
Summary:	Perl utilities for network management using SNMP
Summary(pl):	Perlowe narzêdzia u¿ywaj±ce protoko³u SNMP
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils-perl

%description utils-perl
This package contains various Perl utilities for managing your network
using the SNMP protocol.

%description utils-perl -l pl
Perlowe narzêdzia do zarz±dzania sieci± przy u¿yciu protoko³u SNMP.

%package snmpconf
Summary:	snmpconf - creating and modifying SNMP configuration files
Summary(pl):	snmpconf - tworzenie i modyfikowanie plików konfiguracyjnych SNMP
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	perl-SNMP = %{version}-%{release}

%description snmpconf
snmpconf is a simple Perl script that walks you through setting up a
configuration file step by step. It should be fairly straight forward
to use.

%description snmpconf -l pl
snmpconf to prosty skrypt Perla pozwalaj±cy na tworzenie pliku
konfiguracyjnego krok po kroku. Powinien byæ w miarê prosty w u¿yciu.

%package tkmib
Summary:	MIB browser in Tk
Summary(pl):	Przegl±darka MIB-ów w Tk
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Requires:	perl-Tk

%description tkmib
MIB browser in Tk.

%description tkmib -l pl
Przegl±darka MIB-ów w Tk.

%prep
%setup -q -a7 -a8
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
	--with-libwrap \
	--with-openssl \
	--disable-debugging \
	--with-persistent-directory="/var/lib/net-snmp" \
	--enable-ipv6 \
	--with-sys-contact="root@localhost" \
	--enable-ucd-snmp-compatibility \
	--with-defaults \
	--with-default-snmp-version=3 \
	--enable-shared

#	--enable-reentrant is broken - snmpd deadlocks on send (tries to lock the same mutex twice):
#   #4  0xb760f54e in siglongjmp () from /lib/tls/libpthread.so.0
#   #5  0xb7e5e0cf in snmp_res_lock (groupID=0, resourceID=1) at mt_support.c:103
#   #6  0xb7e45698 in snmp_sess_pointer (session=0x80ff868) at snmp_api.c:6975
#   #7  0xb7e41aca in snmp_async_send (session=0x80ff868, pdu=0x8141848, callback=0, cb_data=0x0)
#       at snmp_api.c:4564
#   #8  0xb7e41a6d in snmp_send (session=0x80ff868, pdu=0x8141848) at snmp_api.c:4551
#   #9  0xb7ebf6fd in netsnmp_wrap_up_request (asp=0x812d828, status=0) at snmp_agent.c:1627
#   #10 0xb7ec12e3 in netsnmp_handle_request (asp=0x812d828, status=0) at snmp_agent.c:2996
#   #11 0xb7ebfa65 in handle_snmp_packet (op=1, session=0x80ff868, reqid=628270607, pdu=0x81419b8,
#       magic=0x0) at snmp_agent.c:1792
#   #12 0xb7e42b1c in _sess_process_packet (sessp=0x812c970, sp=0x80ff868, isp=0x812c698,
#       transport=0x8142028, opaque=0x812c1a0, olength=16,
#       packetptr=0x8145cb8 "0f\002\001\0030\021\002\004c [Ç\002\003", length=104) at snmp_api.c:5208
#   #13 0xb7e434e6 in _sess_read (sessp=0x812c970, fdset=0xbfffe0e0) at snmp_api.c:5606
#   #14 0xb7e43535 in snmp_sess_read (sessp=0x812c970, fdset=0xbfffe0e0) at snmp_api.c:5625
#   #15 0xb7e42c44 in snmp_read (fdset=0xbfffe0e0) at snmp_api.c:5260
#   #16 0x0804bbe5 in receive () at snmpd.c:1149
#   #17 0x0804b53d in main (argc=5, argv=0xbffff344) at snmpd.c:993
# [res mutex with groupID=0, resourceID=1 already locked in snmp_read() at snmp_api.c:5258]

%{__make}

TDIR="`pwd`"
cd perl
sed -e "s@-L/usr/lib@-L${TDIR}/snmplib/.libs -L${TDIR}/agent/.libs -L${TDIR}/agent/helpers/.libs@" \
	../net-snmp-config > net-snmp-config
chmod +x net-snmp-config

PATH=`pwd`:$PATH \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags} -I`pwd`/../include" \
	</dev/null
# avoid rpaths generated by MakeMaker
perl -pi -e 's@LD_RUN_PATH="\$\(LD_RUN_PATH\)" @@' */Makefile */*/Makefile

%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{snmp,rc.d/init.d,sysconfig},/var/log}

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.conf
:> $RPM_BUILD_ROOT%{_sysconfdir}/snmp/snmpd.local.conf
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

# Juniper MIBs:
install JuniperMibs/*.txt $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add snmpd
if [ -f /var/lock/subsys/snmpd ]; then
	/etc/rc.d/init.d/snmpd restart >&2
else
	%banner %{name} -e <<EOF
Run \"/etc/rc.d/init.d/snmpd start\" to start snmpd daemon.
EOF
#" vim
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
	%banner %{name}-snmptrapd -e <<EOF
Run \"/etc/rc.d/init.d/snmptrapd start\" to start snmp trap daemon.
EOF
#" vim
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
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmpd.conf
%attr(640,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmpd.local.conf

%attr(755,root,root) %{_sbindir}/snmpd

%{_mandir}/man5/snmpd.conf.5*
%{_mandir}/man5/variables.5*
%{_mandir}/man8/snmpd.8*

%attr(640,root,root) %ghost %{logfile}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnet*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mib2c
%attr(755,root,root) %{_bindir}/mib2c-update
%attr(755,root,root) %{_bindir}/net-snmp-config
%attr(755,root,root) %{_libdir}/libnet*[a-z].so
%{_libdir}/libnet*.la
%{_includedir}/net-snmp
%{_datadir}/snmp/mib2c*
%{_mandir}/man1/mib2c.1*
%{_mandir}/man3/[!NS]*
%{_mandir}/man5/mib2c.conf.5*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnet*.a

%files compat-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnmp.so
%{_libdir}/libsnmp.la
%{_includedir}/ucd-snmp

%files compat-static
%defattr(644,root,root,755)
%{_libdir}/libsnmp.a

%files mibs
%defattr(644,root,root,755)
%dir %{_datadir}/snmp
%{_datadir}/snmp/mibs

%files snmptrapd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/snmptrapd
%attr(754,root,root) /etc/rc.d/init.d/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/snmp/snmptrapd.conf
%attr(755,root,root) %{_datadir}/snmp/snmp_perl_trapd.pl
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

%files snmpconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/snmpconf
%{_mandir}/man1/snmpconf.1*
%{_datadir}/snmp/snmpconf-data

%files tkmib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tkmib
