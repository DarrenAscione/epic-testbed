# EPIC Testbed Detection Mechanism

[![Build Status](https://travis-ci.org/DarrenAscione/epic-testbed.svg?branch=master)](https://travis-ci.org/DarrenAscione/epic-testbed)
[![Coverage Status](https://coveralls.io/repos/github/DarrenAscione/epic-testbed/badge.svg?branch=master)](https://coveralls.io/github/DarrenAscione/epic-testbed?branch=master)

## Contents

- [Setup](#setup)
- [Structure](#structure)

## Setup

```bash
pip install requirements.txt
```

## Structure

```bash
.
├── data
│   ├── 40test.txt
│   └── cipKiller40-50.pcap
├── readme.md
├── requirements.txt
└── src
    ├── main
    │   └── common
    │       ├── pcaptxt.py
    │       └── util.py
    ├── setup.py
    └── test
        └── common
            ├── test_pcaptxt.py
            └── test_util.py
```



