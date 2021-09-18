COMPONENT_GENERATION_DIR=component-generation
COMPONENT_GENERATION_FILES=$(shell find $(COMPONENT_GENERATION_DIR)/ -name '*.json' -o -name '*.ts' -o -name '*.js')
DEPS_DIR=deps
DIST_DIR=dist
INST_DIR=inst
MAN_DIR=man
NODE_MODULES_DIR=node_modules
PACKAGE_FILE=package.json
PACKAGE_LOCK_FILE=package-lock.json
PY_SRC_DIR=materialdashboard
PY_MODULE_FILE_NAME=__init__.py
PY_MODULE_FILE=$(PY_SRC_DIR)/$(PY_MODULE_FILE_NAME)
EGG_DIR=$(PY_SRC_DIR).egg-info
REQUIREMENTS_FILE=requirements.txt
R_DIR=R
SRC_DIR=src
SRC_JL_DIR=$(SRC_DIR)/jl
SRC_JL_MODULE_FILE=$(SRC_DIR)/Materialdashboard.jl
SRC_LIB_DIR=$(SRC_DIR)/lib
VENV_DIR=venv

ACTIVATE_FILE=$(VENV_DIR)/bin/activate

.DEFAULT_GOAL := $(DIST_DIR)

$(NODE_MODULES_DIR): $(PACKAGE_FILE) $(PACKAGE_LOCK_FILE)
	npm install
	touch $(NODE_MODULES_DIR)

$(VENV_DIR): $(REQUIREMENTS_FILE)
	python3 -m venv $(VENV_DIR)
	. $(ACTIVATE_FILE) &&\
		python -m pip install --upgrade pip wheel &&\
		pip install -r $(REQUIREMENTS_FILE)
	touch $(VENV_DIR)

.PHONY: lint
lint: $(NODE_MODULES_DIR)
	npm run lint

.PHONY: generate
generate: $(SRC_LIB_DIR)

$(SRC_LIB_DIR): $(NODE_MODULES_DIR) $(COMPONENT_GENERATION_FILES)
	rm -rf $(SRC_DIR)
	npm run generate
	touch $(SRC_LIB_DIR)

$(DEPS_DIR) $(INST_DIR) $(MAN_DIR) $(R_DIR) $(SRC_JL_DIR) $(SRC_JL_MODULE_FILE) $(PY_SRC_DIR): $(VENV_DIR) $(NODE_MODULES_DIR) $(SRC_LIB_DIR)
	. $(ACTIVATE_FILE) &&\
		npm run build
	touch $(PY_SRC_DIR)

$(DIST_DIR) $(EGG_DIR): $(PY_SRC_DIR) $(PY_MODULE_FILE)
	. $(ACTIVATE_FILE) &&\
		python setup.py sdist bdist_wheel
	touch $(DIST_DIR)

.PHONY: upload
upload: $(DIST_DIR)
	. $(ACTIVATE_FILE) &&\
		pip install --upgrade twine &&\
		twine upload $(DIST_DIR)/*

.PHONY: clean_node
clean_node:
	rm -rf $(NODE_MODULES_DIR)

.PHONY: clean_venv
clean_venv:
	rm -rf $(VENV_DIR)

.PHONY: clean_src
clean_src:
	rm -rf $(SRC_DIR)

.PHONY: clean_build
clean_build:
	rm -rf $(DEPS_DIR) $(INST_DIR) $(MAN_DIR) $(R_DIR) $(SRC_JL_DIR) $(SRC_JL_MODULE_FILE)
	find $(PY_SRC_DIR) ! -name '$(PY_MODULE_FILE_NAME)' ! -name '$(PY_SRC_DIR)' -exec rm -rf {} +

.PHONY: clean_dist
clean_dist:
	rm -rf $(DIST_DIR) $(EGG_DIR)

.PHONY: clean
clean: clean_node clean_venv clean_src clean_build clean_dist
