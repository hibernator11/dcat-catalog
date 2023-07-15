from pyshex.evaluate import evaluate
from rdflib import Graph, Namespace, XSD

# ShEx Expression
shex = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://example.com/>
PREFIX weso-s: <http://weso.es/shapes/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX tadirah: <https://vocabs.dariah.eu/tadirah/>
PREFIX schema: <http://schema.org/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX rdau: <http://rdaregistry.info/Elements/u/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

start = @weso-s:Dataset

weso-s:Dataset
{
   dcterms:language  IRI  ;                                    # 100.0 %
   dcat:contactPoint  IRI  ;                                   # 100.0 %
   dcterms:publisher  @weso-s:Organization  ;                  # 100.0 %
   dcterms:title  rdf:langString  ;                            # 100.0 %
   wdt:P7014  IRI  ;                                           # 100.0 %
   dcat:keyword  rdf:langString  +;                            # 100.0 %
   rdf:type  [dcat:Dataset]  ;                                 # 100.0 %
   dcat:landingPage  IRI  ;                                    # 100.0 %
   wdt:P366  IRI  ;                                            # 100.0 %
   rdau:P60222  IRI  ;                                         # 100.0 %
   dcterms:description  xsd:string  ;                          # 100.0 %
   prov:wasGeneratedBy  IRI  {2};                              # 100.0 %
   rdau:P60521  IRI  ;                                         # 100.0 %
   dcterms:license  IRI                                        # 100.0 %
}


weso-s:Distribution
{
   rdf:type  [dcat:Distribution]  ;                            # 100.0 %
   dcat:downloadURL  IRI  ;                                    # 100.0 %
   dcat:byteSize  xsd:nonNegativeInteger  ;                    # 100.0 %
   dcat:mediaType  IRI  ;                                      # 100.0 %
   dcat:compressFormat  IRI                                    # 100.0 %
}


weso-s:Organization
{
   foaf:mbox  IRI  ;                                           # 100.0 %
   rdfs:label  rdf:langString  {2};                            # 100.0 %
   owl:sameAs  IRI  {2};                                       # 100.0 %
   rdf:type  [prov:Organization]  ;                            # 100.0 %
   rdf:type  [prov:Agent]  ;                                   # 100.0 %
   rdf:type  [foaf:Organization]  ;                            # 100.0 %
   foaf:homePage  IRI  ;                                       # 100.0 %
   foaf:givenName  xsd:string                                  # 100.0 %
}
"""


g = Graph()
g.parse("../datasets/data-foundry-nls.ttl")

rslt, reason = evaluate(g, shex, focus="http://example.com/dataset-nls-mia")
if rslt:
    print("CONFORMS")
else:
    print(f"{reason if reason else 'DOES NOT CONFORM'}")


