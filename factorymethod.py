# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import json


class JSONConnector(object):

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode = "r", encoding = "utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(object):

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if (filepath.endswith("json")):
        connector = JSONConnector
    elif (filepath.endswith("xml")):
        connector = XMLConnector
    else:
        raise ValueError("Cannot connect to {0}".format(filepath))
    return connector(filepath)



def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as error:
        print(error)
    return factory



def main():
    sqlite_factory = connect_to("data/person.sq3")
    xml_factory = connect_to("person.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//person[lastName='{}']".format('Liar'))
    print("found : {0} persons".format(len(liars)))
    for liar in liars:
        print("first name : {0}".format(liar.find("firstName").text))
        print("last name : {0}".format(liar.find("lastName").text))
        [print("phone number : ({0})".format(phone.attrib["type"]), phone.text) for phone in liar.find("phoneNumbers")]

    json_factory = connect_to("donut.json")
    json_data = json_factory.parsed_data
    print("found : {0} donuts".format(len(json_data)))
    for donut in json_data:
        print("NAME : {0}".format(donut["name"]))
        print("PRICE : {0:.2f}".format(donut["ppu"]))
        [print("TOPPING : {0} {1}".format(topping["id"], topping["type"])) for topping in donut["topping"]]

if (__name__ == "__main__"):
    main()
