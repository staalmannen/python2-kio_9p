# developer & mantainer : Jens Staal <staal1978@gmail.com>

pkgname=python2-kio-9p
pkgver=0.0.1
pkgrel=1
pkgdesc="A 9P2000 network protocol/file system KIO slave written in python"
arch=('any')
license=('MIT')
url=""
depends=('kdebindings-python2' 'python2-py9p-hg')
makedepends=('python2')
sources=()
md5sums=()

#locations and such info for installing a KIO slave was gleaned by inspections of the kio_gopher package
# 9p.protocol should be installed in /usr/share/kde4/services/
#The script has to reside in <kde prefix>/share/apps/kio_<protocol name>.
#The .protocol file itself should be installed to <kde prefix>/share/kde4/services.

package() {

mkdir -p $pkgdir/usr/share/kde4/services
mkdir -p $pkgdir/usr/share/apps/kio_9p
install -m0755 kio_9p.py $pkgdir/usr/share/apps/kio_9p/kio_9p.py
install -m0755 9p.protocol $pkgdir/usr/share/kde4/services/9p.protocol

}


