#!/usr/bin/env python2.7

from __future__ import (division, absolute_import, print_function, unicode_literals)
import sys
import re
import unicodedata


def joinCjkLine( text ):
	eaw = unicodedata.east_asian_width
	
	def subst( m ):
		if eaw( m.group( 1 ) ) == "W" and eaw( m.group( 2 ) ) == "W":
			return m.group( 1 ) + m.group( 2 )
		else:
			return m.group( 0 )

	text = re.sub( r"([\S])[^\S\n]*\n[^\S\n]*([\S])", subst, text )

	def subst( m ):
		if eaw( m.group( 1 )[:+1] ) == "W":
			prefix = "_"
		else:
			prefix = " _"

		if eaw( m.group( 1 )[-1:] ) == "W":
			suffix = "_"
		else:
			suffix = "_ "

		return prefix + m.group( 1 ) + suffix

	text = re.sub( r"[\s]+_([^_]+)_[\s]+", subst, text )

	return text


if __name__ == "__main__":
	src = unicode( sys.stdin.read(), "utf-8" )
	dst = joinCjkLine( src )
	sys.stdout.write( dst.encode( "utf-8" ) )
