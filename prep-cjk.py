#!/usr/bin/env python2.7

from __future__ import (division, absolute_import, print_function, unicode_literals)
import sys
import re
import unicodedata


def joinCjkLine( src ):
	def subst( m ):
		if(
			unicodedata.east_asian_width( m.group( 1 ) ) == "W" and
			unicodedata.east_asian_width( m.group( 2 ) ) == "W"
		):
			return m.group( 1 ) + m.group( 2 )
		else:
			return m.group( 0 )

	return re.sub( r"([\S])[^\S\n]*\n[^\S\n]*([\S])", subst, src )


if __name__ == "__main__":
	src = unicode( sys.stdin.read(), "utf-8" )
	dst = joinCjkLine( src )
	sys.stdout.write( dst.encode( "utf-8" ) )
