---
layout: page
title: ris2bib
description: convert .ris to .bib files from the command line
img: 
importance: 2
category: tools
giscus_comments: true
---

Convert .ris formatted citation files into .bib format from the command line. A GoLang command line tool.

## Build

```bash
go get github.com:harrisonlabollita/ris-2-bib.git
```

From there build the exectubale. You can use the ``Makefile``, but make sure the build is appropriate for your architecture.

## Example
Given an RIS formatted file ``example.ris``
```
AU  - LastName1, FirstName1
AU  - LastName2, FirstName2
AU  - LastName3, FirstName3
AU  - LastName4, FirstName4
PY  - 2023
DA  - 2023/01/01
TI  - An interesting title would be here
JO  - Journal Name
SP  - 123
EP  - 123
VL  - 123
IS  - 1234
AB  - The quick brown fox jumped over the lazy sheep dog.
SN  - 1234-2468
UR  - https://doi.org/10.0000/journal0000
DO  - 10.0000/journal0000`
```

Calling ``ris2bib`` generates the BibTeX formatted file ``example.bib``

```
@article{LastName12023interesting,
author = {LastName1, FirstName1  and  LastName2, FirstName2  and  LastName3, FirstName3  and  LastName4, FirstName4},
title = {An interesting title would be here},
journal = {Journal Name},
year  = {2023},
volume  = {123},
issue = {1234},
pages = {123-123},
doi  = {10.0000/journal0000},
url  = {https://doi.org/10.0000/journal0000}
}
```
