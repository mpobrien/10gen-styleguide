BOOTSTRAP = ./styleguide/styleguide/static/css/bootstrap.css
BOOTSTRAP_LESS = ./less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ./styleguide/styleguide/static/css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ./less/responsive.less
LESS_COMPRESSOR ?= `which lessc`
WATCHR ?= `which watchr`

docs: bootstrap
	lessc ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	lessc ${BOOTSTRAP_RESPONSIVE_LESS} > ${BOOTSTRAP_RESPONSIVE}
	cp img/* ./styleguide/styleguide/static/img/
	cp js/*.js ./styleguide/styleguide/static/js/
	cp js/tests/vendor/jquery.js ./styleguide/styleguide/static/js/

bootstrap:
	mkdir -p bootstrap-10gen/img
	mkdir -p bootstrap-10gen/css
	mkdir -p bootstrap-10gen/js
	cp img/* bootstrap-10gen/img/
	lessc ${BOOTSTRAP_LESS} > bootstrap-10gen/css/bootstrap.css
	lessc --compress ${BOOTSTRAP_LESS} > bootstrap-10gen/css/bootstrap.min.css
	lessc ${BOOTSTRAP_RESPONSIVE_LESS} > bootstrap-10gen/css/bootstrap-responsive.css
	lessc --compress ${BOOTSTRAP_RESPONSIVE_LESS} > bootstrap-10gen/css/bootstrap-responsive.min.css
	cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js > bootstrap-10gen/js/bootstrap.js


.PHONY: dist docs watch gh-pages
