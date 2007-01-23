#
# Conditional build:
%bcond_without	autodeps	# don't BR packages only for deps resolving
#
%include	/usr/lib/rpm/macros.perl
Summary:	A collection of SNMP protocol tools
Summary(es):	Agente SNMP de la UCD
Summary(pl):	Kolekcja narzÍdzi do obs≥ugi protoko≥u SNMP
Summary(pt_BR):	Agente SNMP da UCD
Summary(ru):	Ó¡¬œ“ ’‘…Ã…‘ ƒÃ— –“œ‘œÀœÃ¡ SNMP œ‘ UC-Davis
Summary(uk):	Ó¡¬¶“ ’‘…Ã¶‘ ƒÃ— –“œ‘œÀœÃ’ SNMP ◊¶ƒ UC-Davis
Name:		net-snmp
Version:	5.4
Release:	2
License:	BSD-like
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/net-snmp/%{name}-%{version}.tar.gz
# Source0-md5:	46d893281056ff476e597659cb91574d
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
Patch3:		%{name}-dlopen-fix.patch
Patch4:		%{name}-manpage.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-llinterfaces.patch
Patch7:		%{name}-kernel_headers.patch
Patch8:		%{name}-rpmpath.patch
Patch9:		%{name}-snmpksm.patch
Patch10:	%{name}-python.patch
Patch11:	%{name}-python-includes.patch
URL:		http://www.net-snmp.org/
BuildRequires:	autoconf >= 2.57-3
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	heimdal-devel
BuildRequires:	libtool >= 1.4
BuildRequires:	libwrap-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_autodeps:BuildRequires:	perl-Term-ReadKey}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-devel >= 4.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.176
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	/usr/bin/setsid
Requires:	rc-scripts >= 0.2.0
Provides:	snmpd
Obsoletes:	cmu-snmp
Obsoletes:	snmpd
Obsoletes:	ucd-snmp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		logfile		/var/log/snmpd.log
%define		filterout_ld	-Wl,--as-needed

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management (hence the name). The net-snmp project includes
various SNMP tools: an extensible agent, an SNMP library, tools for
requesting or setting information from SNMP agents, tools for
generating and handling SNMP traps, a version of the netstat command
which uses SNMP, and a Tk/Perl mib browser. This package contains the
snmpd daemon, documentation, etc.

%description -l es
Este paquete se deriva de la implementaciÛn del Protocolo Simple de
GestiÛn de Redes versiÛn 2 (SNMPv2) de la Universidad Carnegie Mellon.
⁄til para administrar redes y hacer contabilidad.

%description -l pl
SNMP (Simple Network Management Protocol) jest protoko≥em uøywanym do
zarz±dzania sieciami. Pakiet zawiera narzÍdzia: rozbudowywalnego
agenta, bibliotekÍ SNMP, narzÍdzia do odpytywania oraz ustawiania
informacji poprzez agentÛw SNMP, narzÍdzia do generowania i obs≥ugi
pu≥apek SNMP, wersjÍ komendy netstat uøywaj±c± SNMP, przegl±darkÍ mib
w Tk/Perl, demona, dokumentacjÍ itp.

%description -l pt_BR
Este pacote È derivado da implementaÁ„o do Protocolo Simples de
Gerenciamento de Redes vers„o 2 (SNMPv2) da Universidade Carnegie
Mellon. ⁄til para gerenciar redes e fazer contabilidade.

%description -l ru
SNMP (Simple Network Management Protocol) - ‹‘œ –“œ‘œÀœÃ, …”–œÃÿ⁄’≈ÕŸ 
ƒÃ— ’–“¡◊Ã≈Œ…— ”≈‘ÿ¿ (œ‘”¿ƒ¡ … Œ¡⁄◊¡Œ…≈). “œ≈À‘ net-snmp ◊ÀÃ¿ﬁ¡≈‘
“¡⁄Œœœ¬“¡⁄ŒŸ≈ SNMP-’‘…Ã…‘Ÿ: “¡”€…“—≈ÕŸ  ¡«≈Œ‘, ¬…¬Ã…œ‘≈À¡ SNMP,
’‘…Ã…‘Ÿ ƒÃ— ⁄¡–“œ”¡ …Ã… ’”‘¡Œœ◊À… …Œ∆œ“Õ¡√…… œ‘ SNMP-¡«≈Œ‘œ◊, ’‘…Ã…‘Ÿ
ƒÃ— «≈Œ≈“¡√…… … œ¬“¡¬œ‘À… SNMP-‘“¡–œ◊, ◊≈“”…— ÀœÕ¡ŒƒŸ netstat,
…”–œÃÿ⁄’¿›≈  SNMP, … mib-¬“¡’⁄≈“ Œ¡ Tk/Perl. ¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘
ƒ≈ÕœŒŸ snmpd … snmptrapd, ƒœÀ’Õ≈Œ‘¡√…¿ … ‘.ƒ.

%description -l uk
SNMP (Simple Network Management Protocol) - √≈ –“œ‘œÀœÃ, —À… 
◊…Àœ“…”‘œ◊’¿‘ÿ ƒÃ— À≈“’◊¡ŒŒ— Õ≈“≈÷≈¿ (⁄◊¶ƒ”… ¶ Œ¡⁄◊¡). “œ≈À‘ net-snmp
Õ¶”‘…‘ÿ “¶⁄ŒœÕ¡Œ¶‘Œ¶ SNMP-’‘…Ã¶‘…: “œ⁄€…“¿◊¡Œ…  ¡«≈Œ‘, ¬¶¬Ã¶œ‘≈À¡
SNMP, ’‘…Ã¶‘… ƒÃ— ⁄¡–“œ”’ ‘¡ ◊”‘¡Œœ◊Ã≈ŒŒ— ¶Œ∆œ“Õ¡√¶ß ◊¶ƒ NMP-¡«≈Œ‘¶◊,
’‘…Ã¶‘… ƒÃ— «≈Œ≈“¡√¶ß ‘¡ œ¬“œ¬À… SNMP-‘“¡–¶◊, ◊≈“”¶— ÀœÕ¡Œƒ… netstat,
—À¡ ◊…Àœ“…”‘œ◊’§ SNMP, ‘¡ mib-¬“¡’⁄≈“ Œ¡ Tk/Perl. „≈  –¡À≈‘ Õ¶”‘…‘ÿ
ƒ≈ÕœŒ… snmpd ‘¡ snmptrapd, ƒœÀ’Õ≈Œ‘¡√¶¿ ¶ ‘.¶.

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
Summary(es):	Archivos de inclusiÛn y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla programistÛw uøywaj±cych bibliotek net-snmp
Summary(pt_BR):	Arquivos de inclus„o e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	Û“≈ƒ¡ “¡⁄“¡¬œ‘À… ƒÃ— –“œ≈À‘¡ UCD-SNMP
Summary(uk):	Û≈“≈ƒœ◊…›≈ “œ⁄“œ¬À… ƒÃ— –“œ≈À‘’ UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	elfutils-devel
Requires:	libwrap-devel
Requires:	openssl-devel >= 0.9.7c
Requires:	rpm-devel
Obsoletes:	ucd-snmp-devel

%description devel
The ucd-snmp-devel package contains the development libraries and
header files for use with the net-snmp project's network management
tools.

%description devel -l es
Estas son las bibliotecas y archivos de inclusiÛn para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creaciÛn de
programas para uso en la gestiÛn de redes.

%description devel -l pl
Pakiet zawiera pliki nag≥Ûwkowe i biblioteki potrzebne do rozwoju
aplikacji uøywaj±cych protoko≥u SNMP.

%description devel -l pt_BR
Estas s„o as bibliotecas e arquivos de inclus„o para desenvolvimento
com o SNMP da UCD. Com este pacote È possÌvel a criaÁ„o de programas
para uso no gerenciamento de redes.

%description devel -l ru
¡À≈‘ ucd-snmp-devel ”œƒ≈“÷…‘ ¬…¬Ã…œ‘≈À… “¡⁄“¡¬œ‘ﬁ…À¡ … »≈ƒ≈“¡ ƒÃ—
…”–œÃÿ⁄œ◊¡Œ…— ” ’‘…Ã…‘¡Õ… ’–“¡◊Ã≈Œ…— ”≈‘ÿ¿ –“œ≈À‘¡ net-snmp.

%description devel -l uk
¡À≈‘ ucd-snmp-devel Õ¶”‘…‘ÿ ¬¶¬Ã¶œ‘≈À… –“œ«“¡Õ¶”‘¡ ‘¡ »≈ƒ≈“… ƒÃ—
◊…Àœ“…”‘¡ŒŒ— ⁄ ’‘…Ã¶‘¡Õ… À≈“’◊¡ŒŒ— Õ≈“≈÷≈¿ –“œ≈À‘’ net-snmp.

%package static
Summary:	Static net-snmp libraries
Summary(pl):	Statyczne biblioteki net-snmp
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com ucd-snmp
Summary(ru):	Û‘¡‘…ﬁ≈”À…≈ ¬…¬Ã…œ‘≈À… ƒÃ— –“œ≈À‘¡ net-snmp
Summary(uk):	Û‘¡‘…ﬁŒ¶ ¬¶¬Ã¶œ‘≈À… ƒÃ— –“œ≈À‘’ net-snmp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description static
Static net-snmp libraries.

%description static -l pl
Statyczne biblioteki net-snmp.

%description static -l pt_BR
Bibliotecas est·ticas para desenvolvimento com net-snmp.

%package compat-devel
Summary:	The development environment for the UCD-SNMP project
Summary(es):	Archivos de inclusiÛn y bibliotecas para desarrollo en el SNMP de la UCD
Summary(pl):	Pliki dla programistÛw uøywaj±cych bibliotek UCD-SNMP
Summary(pt_BR):	Arquivos de inclus„o e bibliotecas para desenvolvimento no SNMP da UCD
Summary(ru):	Û“≈ƒ¡ “¡⁄“¡¬œ‘À… ƒÃ— –“œ≈À‘¡ UCD-SNMP
Summary(uk):	Û≈“≈ƒœ◊…›≈ “œ⁄“œ¬À… ƒÃ— –“œ≈À‘’ UCD-SNMP
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
Estas son las bibliotecas y archivos de inclusiÛn para desarrollo con
el SNMP de la UCD. Con este paquete es posible la creaciÛn de
programas para uso en la gestiÛn de redes.

%description compat-devel -l pl
Pakiet zawiera pliki nag≥Ûwkowe i biblioteki potrzebne do rozwoju
aplikacji uøywaj±cych protoko≥u SNMP.

%description compat-devel -l pt_BR
Estas s„o as bibliotecas e arquivos de inclus„o para desenvolvimento
com o SNMP da UCD. Com este pacote È possÌvel a criaÁ„o de programas
para uso no gerenciamento de redes.

%description compat-devel -l ru
¡À≈‘ ucd-snmp-devel ”œƒ≈“÷…‘ ¬…¬Ã…œ‘≈À… “¡⁄“¡¬œ‘ﬁ…À¡ … »≈ƒ≈“¡ ƒÃ—
…”–œÃÿ⁄œ◊¡Œ…— ” ’‘…Ã…‘¡Õ… ’–“¡◊Ã≈Œ…— ”≈‘ÿ¿ –“œ≈À‘¡ UCD-SNMP.

%description compat-devel -l uk
¡À≈‘ ucd-snmp-devel Õ¶”‘…‘ÿ ¬¶¬Ã¶œ‘≈À… –“œ«“¡Õ¶”‘¡ ‘¡ »≈ƒ≈“… ƒÃ—
◊…Àœ“…”‘¡ŒŒ— ⁄ ’‘…Ã¶‘¡Õ… À≈“’◊¡ŒŒ— Õ≈“≈÷≈¿ –“œ≈À‘’ UCD-SNMP.

%package compat-static
Summary:	Static UCD-SNMP libraries
Summary(pl):	Statyczne biblioteki UCD-SNMP
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com ucd-snmp
Summary(ru):	Û‘¡‘…ﬁ≈”À…≈ ¬…¬Ã…œ‘≈À… ƒÃ— –“œ≈À‘¡ UCD-SNMP
Summary(uk):	Û‘¡‘…ﬁŒ¶ ¬¶¬Ã¶œ‘≈À… ƒÃ— –“œ≈À‘’ UCD-SNMP
Group:		Development/Libraries
Requires:	%{name}-compat-devel = %{version}-%{release}
Obsoletes:	ucd-snmp-static

%description compat-static
Static UCD-SNMP libraries.

%description compat-static -l pl
Statyczne biblioteki UCD-SNMP.

%description compat-static -l pt_BR
Bibliotecas est·ticas para desenvolvimento com ucd-snmp.

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
Summary(pl):	Demon obs≥uguj±cy pu≥apki SNMP
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts >= 0.2.0
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-snmptrapd

%description snmptrapd
The ucd-snmp-snmptrapd package contains snmp trap daemon.

%description snmptrapd -l pl
Pakiet zawiera demon obs≥uguj±cy pu≥apki SNMP.

%package utils
Summary:	Network management utilities using SNMP, from the NET-SNMP project
Summary(es):	Utilitarios del SNMP de la UCD
Summary(pl):	NarzÍdzia uøywaj±ce protoko≥u SNMP
Summary(pt_BR):	Utilit·rios do SNMP da UCD
Summary(ru):	ı‘…Ã…‘Ÿ ’–“¡◊Ã≈Œ…— ”≈‘ÿ¿ –œ SNMP …⁄ –“œ≈À‘¡ NET-SNMP
Summary(uk):	ı‘…Ã¶‘… À≈“’◊¡ŒŒ— Õ≈“≈÷≈¿ –œ SNMP ⁄ –“œ≈À‘’ NET-SNMP
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
RÛønego rodzaju narzÍdzia do zarz±dzania sieci± przy uøyciu protoko≥u
SNMP.

%description utils -l pt_BR
V·rios utilit·rios para uso com o SNMP da UCD. ContÈm utilit·rios
como: snmpwalk, snmptest e outros.

%description utils -l ru
¡À≈‘ ucd-snmp-utils ”œƒ≈“÷…‘ “¡⁄Œœœ¬“¡⁄ŒŸ≈ ’‘…Ã…‘Ÿ ƒÃ— …”–œÃÿ⁄œ◊¡Œ…—
◊ –“œ≈À‘≈ ’–“¡◊Ã≈Œ…— ”≈‘ÿ¿ net-snmp.

%description utils -l uk
¡À≈‘ ucd-snmp-utils Õ¶”‘…‘ÿ “¶⁄ŒœÕ¡Œ¶‘Œ¶ ’‘…Ã¶‘… ƒÃ— ◊…Àœ“…”‘¡ŒŒ— ◊
–“œ≈À‘¶ À≈“’◊¡ŒŒ— Õ≈“≈÷≈¿ net-snmp.

%package -n perl-SNMP
Summary:	SNMP and NetSNMP::* Perl modules
Summary(pl):	Modu≥y Perla SNMP oraz NetSNMP::*
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}-%{release}
Conflicts:	ucd-snmp-utils-perl

%description -n perl-SNMP
SNMP and NetSNMP::* Perl modules - Perl interface to net-snmp.

%description -n perl-SNMP -l pl
Modu≥y Perla SNMP oraz NetSNMP::* - perlowy interfejs do net-snmp.

%package utils-perl
Summary:	Perl utilities for network management using SNMP
Summary(pl):	Perlowe narzÍdzia uøywaj±ce protoko≥u SNMP
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Obsoletes:	cmu-snmp-utils
Obsoletes:	ucd-snmp-utils-perl

%description utils-perl
This package contains various Perl utilities for managing your network
using the SNMP protocol.

%description utils-perl -l pl
Perlowe narzÍdzia do zarz±dzania sieci± przy uøyciu protoko≥u SNMP.

%package snmpconf
Summary:	snmpconf - creating and modifying SNMP configuration files
Summary(pl):	snmpconf - tworzenie i modyfikowanie plikÛw konfiguracyjnych SNMP
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	perl-SNMP = %{version}-%{release}

%description snmpconf
snmpconf is a simple Perl script that walks you through setting up a
configuration file step by step. It should be fairly straight forward
to use.

%description snmpconf -l pl
snmpconf to prosty skrypt Perla pozwalaj±cy na tworzenie pliku
konfiguracyjnego krok po kroku. Powinien byÊ w miarÍ prosty w uøyciu.

%package tkmib
Summary:	MIB browser in Tk
Summary(pl):	Przegl±darka MIB-Ûw w Tk
Group:		Applications/System
Requires:	perl-SNMP = %{version}-%{release}
Requires:	perl-Tk

%description tkmib
MIB browser in Tk.

%description tkmib -l pl
Przegl±darka MIB-Ûw w Tk.

%package -n python-netsnmp
Summary:	Python netsnmp extension module
Summary(pl):	Modu≥ rozszerzenia netsnmp dla Pythona
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-netsnmp
The 'netsnmp' Python extension module provides a full featured,
tri-lingual SNMP (SNMPv3, SNMPv2c, SNMPv1) client API.

%description -n python-netsnmp -l pl
Modu≥ rozszerzenia netsnmp dla Pythona udostÍpnia pe≥ne API klienckie
SNMP dla trzech wersji tego protoko≥u (SNMPv3, SNMPv2c, SNMPv1).

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-cflags="%{rpmcflags} -I/usr/include/et" \
	--with-ldflags="%{rpmldflags}" \
	--with-defaults \
	--with-default-snmp-version=3 \
	--with-krb5 \
	--with-libwrap \
	--with-logfile="%{logfile}" \
	--with-mib-modules="host disman/event-mib smux mibII/mta_sendmail \
%ifarch %{ix86} %{x8664}
		ucd-snmp/lmSensors ucd-snmp/diskio \
%endif
		agentx target misc/ipfwacc" \
	--with-openssl \
	--with-perl-modules \
	--with-persistent-directory="/var/lib/net-snmp" \
	--with-python-modules \
	--with-security-modules="ksm" \
	--with-sys-contact="root@localhost" \
	--with-sys-location="Unknown" \
	--with-transports="UDP UDPIPv6 TCP TCPIPv6 Unix Callback " \
	--disable-debugging \
	--enable-as-needed \
	--enable-ipv6 \
	--enable-ucd-snmp-compatibility

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
#       packetptr=0x8145cb8 "0f\002\001\0030\021\002\004c [«\002\003", length=104) at snmp_api.c:5208
#   #13 0xb7e434e6 in _sess_read (sessp=0x812c970, fdset=0xbfffe0e0) at snmp_api.c:5606
#   #14 0xb7e43535 in snmp_sess_read (sessp=0x812c970, fdset=0xbfffe0e0) at snmp_api.c:5625
#   #15 0xb7e42c44 in snmp_read (fdset=0xbfffe0e0) at snmp_api.c:5260
#   #16 0x0804bbe5 in receive () at snmpd.c:1149
#   #17 0x0804b53d in main (argc=5, argv=0xbffff344) at snmpd.c:993
# [res mutex with groupID=0, resourceID=1 already locked in snmp_read() at snmp_api.c:5258]

# build this subdir first. it's causing STRANGE compile failures # otherwise (for me at least). glen
%{__make} -C agent/mibgroup
%{__make}

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
%{_mandir}/man1/mib2c-update.1*
%{_mandir}/man1/net-snmp-config.1*
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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/snmptrapd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/snmptrapd.conf
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

%files snmpconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/snmpconf
%{_mandir}/man1/snmpconf.1*
%{_datadir}/snmp/snmpconf-data

%files tkmib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tkmib
%{_mandir}/man1/tkmib.1*

%files -n python-netsnmp
%defattr(644,root,root,755)
%dir %{py_sitedir}/netsnmp
%attr(755,root,root) %{py_sitedir}/netsnmp/*.so
%{py_sitedir}/netsnmp/*.py[co]
%{py_sitedir}/netsnmp_python-*.egg-info
