[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=Shitcode&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)
[![Python CI](https://github.com/shitcoding/python-project-lvl2/actions/workflows/pyci.yml/badge.svg)](https://github.com/shitcoding/python-project-lvl2/actions/workflows/pyci.yml)
[![Actions Status](https://github.com/shitcoding/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/shitcoding/python-project-lvl2/actions)
---
# `gendiff` package
Generates diff between plain and nested json and yaml files.

---
## Installation

```sh
cd ~/Downloads
git clone https://github.com/shitcoding/python-project-lvl2
cd python-project-lvl2
python3 -m pip install .
```

[![asciicast](https://asciinema.org/a/pvIiwMpNWbkjgGaZQ1SEHljHv.svg)](https://asciinema.org/a/pvIiwMpNWbkjgGaZQ1SEHljHv)

---
## Usage examples
### `stylish` output formatter (default)
#### Generating diff between plain json files with `stylish` output formatter
[![asciicast](https://asciinema.org/a/cIUjY8AHs4XfPRDEms5CAGw3Q.svg)](https://asciinema.org/a/cIUjY8AHs4XfPRDEms5CAGw3Q)

#### Generating diff between plain yaml files with `stylish` output formatter
(Supported extensions: `yaml` and `yml`)
[![asciicast](https://asciinema.org/a/DlX2MKX6RdWGJTNwH3giTr5Mn.svg)](https://asciinema.org/a/DlX2MKX6RdWGJTNwH3giTr5Mn)

#### Generating diff between nested json and files with `stylish` output formatter
(Supports `yaml-yaml`, `json-json`, `json-yaml`, `yaml-json` diffs)
[![asciicast](https://asciinema.org/a/8hOMJP4LujnAXNbg2zrbOmt9e.svg)](https://asciinema.org/a/8hOMJP4LujnAXNbg2zrbOmt9e)

### `plain` output formatter
Usage:
```sh
gendiff -f plain file1.json file2.json
gendiff --format plain file1.yaml file2.yaml
```
#### Generating diff between nested json and files with `plain` output formatter
[![asciicast](https://asciinema.org/a/faDbPvZWK6CnBEVushXxkZ8Hm.svg)](https://asciinema.org/a/faDbPvZWK6CnBEVushXxkZ8Hm)
