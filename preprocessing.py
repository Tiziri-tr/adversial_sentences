# -*- coding: utf-8 -*-
from lxml import etree
import os


def read_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def parse_xml(file):
    tree = etree.parse(file)
    for user in tree.xpath("/users/user/nom"):
        print(user.text)

