# overridable variables
BUILDER := podman
IMAGES := $(wildcard *-image)

REGISTRY := registry.tf.local
REGISTRY_TLS_VERIFY := false

OSC_API_URL := https://api.opensuse.org
OSC_PROJECT := home:moio:Uyuni:Master:Containers
PRODUCT_REPO := https://download.opensuse.org/repositories/systemsmanagement:/Uyuni:/Master/images/repo/Uyuni-Proxy-POOL-x86_64-Media1/


# build
build_targets := $(patsubst %-image,%,$(IMAGES))

build: $(build_targets)

$(build_targets):
	cd $@-image ; ${BUILDER} build -t $@ --build-arg PRODUCT_REPO=${PRODUCT_REPO} .

# push (to registry)
push_targets := $(patsubst %-image,push-%,$(IMAGES))

push: $(push_targets)

$(push_targets): push-%: %
	@${BUILDER} tag $< ${REGISTRY}/$<
	@${BUILDER} image push --tls-verify=$(REGISTRY_TLS_VERIFY) ${REGISTRY}/$<


# init Build Service project
image_files := $(wildcard *-image/*)
osc_project_links := $(patsubst %,obs-project/%,$(image_files))

osc-init: obs-project $(osc_project_links)

obs-project:
	osc --apiurl ${OSC_API_URL} checkout --output-dir=obs-project ${OSC_PROJECT}

.PHONY: $(osc_project_links)
$(osc_project_links):
	ln -sf $(patsubst obs-project/%,../../%,$@) $@

# push sources to Build Service
osc-checkin: osc-init
	cd obs-project ; osc addremove -r
	cd obs-project ; osc --apiurl ${OSC_API_URL} checkin .
