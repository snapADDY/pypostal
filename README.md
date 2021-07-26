# pylibpostal

Parse street addresses around the world.

This is a Python binding for [`libpostal`](https://github.com/openvenues/libpostal), a C library for parsing/normalizing street addresses around the world using statistical NLP and open data. The goal of this project is to understand location-based strings in every language, everywhere.

## Installation

You can install the latest stable version via:

```
$ pip install pylibpostal
```

### Data

`libpostal` needs to download some data files and models from S3. The basic files are on-disk representations of the data structures necessary to perform expansion. Please refer to the [documentation](https://github.com/openvenues/libpostal#data-files) how to download the files.

Export the path to the data folder as environment variable:

```sh
export LIBPOSTAL_DATA_DIR="data-folder"
```

## Usage

```python
>>> from pylibpostal.expand import expand_address
>>> expand_address('Quatre vingt douze Ave des Champs-Élysées')
['92 avenue des champs-elysees',
 '92 avenue des champs elysees',
 '92 avenue des champselysees']
>>> from pylibpostal.parser import parse_address
>>> parse_address('The Book Club 100-106 Leonard St, Shoreditch, London,EC2A 4RH, UK')
[('the book club', 'house'),
 ('100-106', 'house_number'),
 ('leonard st', 'road'),
 ('shoreditch', 'suburb'),
 ('london', 'city'),
 ('ec2a 4rh', 'postcode'),
 ('uk', 'country')]
```
