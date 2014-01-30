#!/usr/bin/env python

import sys

"""
Initialize requirements for OpenCalais
"""

from calais import Calais
CALAIS_API_KEY = 'ed42bg3ku3g3k98kv9kee78s'
calais = Calais(CALAIS_API_KEY, submitter = "pagea1 tester")

def body2entities(body):
    """
    Given an article (STRING body), use the Open Calais named entity recognizer to return
    all entities therein.
    """
    names, companies, orgs, terms = [], [], [], []
    result = calais.analyze(body)
    for entity in result.entities:
        if (entity["_type"] == "Person"):
            names.append(entity["name"])
        if (entity["_type"] == "Company"):
            companies.append(entity["name"])
        if (entity["_type"] == "Organization"):
            orgs.append(entity["name"])
        if (entity["_type"] == "IndustryTerm"):
            terms.append(entity["name"])
    return names, companies, orgs, terms