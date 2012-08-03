tutorial-ja.html: tutorial-ja.md rust.css prep-cjk.py
	cat $< | ./prep-cjk.py | node prep.js --highlight | pandoc \
		--standalone --toc \
		--section-divs --number-sections \
		--from=markdown --to=html --css=rust.css \
		--output=$@
