from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE

target_classes = [
  "http://www.w3.org/ns/dcat#Dataset",
  "http://www.w3.org/ns/dcat#Distribution",
  "http://www.w3.org/ns/prov#Organization"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://www.w3.org/2000/01/rdf-schema#": "rdfs", 
                   "http://example.com/": "",
                   "http://weso.es/shapes/": "ex",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "https://vocabs.dariah.eu/tadirah/": "tadirah",
                   "http://schema.org/": "schema",
                   "http://rdfs.org/ns/void#": "void",
                   "http://rdaregistry.info/Elements/u/": "rdau",
                   "http://purl.org/dc/terms/": "dcterms",
                   "http://www.w3.org/2004/02/skos/core#": "skos",
                   "http://www.w3.org/ns/prov#": "prov",
                   "http://xmlns.com/foaf/0.1/": "foaf",
                   "http://www.w3.org/2002/07/owl#": "owl",
                   "http://www.wikidata.org/entity/": "wd",
                   "http://www.wikidata.org/prop/direct/": "wdt"
                   }

input_nt_file = '../datasets/data-foundry-nls.ttl'

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                graph_file_input=input_nt_file,
                #url_endpoint=url_endpoint, 
                #input_format=NT,
                #all_classes_mode=True,
                input_format="turtle",
                limit_remote_instances=20,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_nls.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
