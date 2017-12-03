# -*- coding: utf-8 -*- 

import zipfile

zFile = zipfile.ZipFile("evil.zip")
zFile.extractall(pwd="secret")