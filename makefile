.PHONY: all clean

all: tutorial-ja.html

clean:
	rm -f tutorial-ja.html


tutorial-ja.html: tutorial-ja.md rust.css prep-cjk.py prep.js
	cat $< | ./prep-cjk.py | node prep.js --highlight | pandoc \
		--standalone \
		--toc \
		--number-sections \
		--from=markdown \
		--to=html5 \
		--css=rust.css \
		--variable lang:ja \
		--output=$@
