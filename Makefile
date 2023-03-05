#! /usr/bin/make -f

DESTDIR=$(HOME)
CGI_DIR=$(DESTDIR)/public_html
TARGETS=check_perl_form.cgi

.PHONY: all install uninstall
all:
install:
	install -m 755 $(TARGETS) $(CGI_DIR)
uninstall:
	cd $(CGI_DIR) && rm -f $(TARGETS)
