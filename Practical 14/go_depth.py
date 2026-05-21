from datetime import datetime
from pathlib import Path
from xml.dom import minidom
from xml.sax import ContentHandler, parse


ONTOLOGIES = ("molecular_function", "biological_process", "cellular_component")
XML_FILE = Path(__file__).with_name("go_obo.xml")


def empty_results():
    return {namespace: {"id": "", "name": "", "count": -1} for namespace in ONTOLOGIES}


def child_text(parent, tag_name):
    nodes = parent.getElementsByTagName(tag_name)
    if not nodes or not nodes[0].firstChild:
        return ""
    return nodes[0].firstChild.nodeValue.strip()


def count_direct_children(parent, tag_name):
    return sum(
        1
        for node in parent.childNodes
        if node.nodeType == node.ELEMENT_NODE and node.tagName == tag_name
    )


def update_result(results, namespace, term_id, name, is_a_count):
    if namespace in results and is_a_count > results[namespace]["count"]:
        results[namespace] = {
            "id": term_id,
            "name": name,
            "count": is_a_count,
        }


def analyse_with_dom(xml_path):
    results = empty_results()
    document = minidom.parse(str(xml_path))

    for term in document.getElementsByTagName("term"):
        namespace = child_text(term, "namespace")
        term_id = child_text(term, "id")
        name = child_text(term, "name")
        is_a_count = count_direct_children(term, "is_a")
        update_result(results, namespace, term_id, name, is_a_count)

    document.unlink()
    return results


class GOHandler(ContentHandler):
    def __init__(self):
        super().__init__()
        self.results = empty_results()
        self.current_element = ""
        self.in_term = False
        self.term_id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.in_term = True
            self.term_id = ""
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0
        elif self.in_term and name == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        if not self.in_term:
            return
        if self.current_element == "id":
            self.term_id += content
        elif self.current_element == "name":
            self.name += content
        elif self.current_element == "namespace":
            self.namespace += content

    def endElement(self, name):
        if name == "term":
            update_result(
                self.results,
                self.namespace.strip(),
                self.term_id.strip(),
                self.name.strip(),
                self.is_a_count,
            )
            self.in_term = False
        self.current_element = ""


def analyse_with_sax(xml_path):
    handler = GOHandler()
    parse(str(xml_path), handler)
    return handler.results


def timed_run(label, function, xml_path):
    start = datetime.now()
    results = function(xml_path)
    end = datetime.now()
    elapsed = end - start
    return label, results, elapsed


def print_results(label, results, elapsed):
    print(f"\n{label} results")
    print("-" * 40)
    for namespace in ONTOLOGIES:
        result = results[namespace]
        print(f"{namespace}:")
        print(f"  GO term: {result['id']} ({result['name']})")
        print(f"  Number of is_a elements: {result['count']}")
    print(f"Time taken: {elapsed}")


def main():
    if not XML_FILE.exists() or XML_FILE.stat().st_size == 0:
        print(f"Cannot find a usable XML file at {XML_FILE}")
        return

    dom_label, dom_results, dom_time = timed_run("DOM", analyse_with_dom, XML_FILE)
    sax_label, sax_results, sax_time = timed_run("SAX", analyse_with_sax, XML_FILE)

    print_results(dom_label, dom_results, dom_time)
    print_results(sax_label, sax_results, sax_time)

    if dom_results == sax_results:
        print("\nDOM and SAX returned the same results.")
    else:
        print("\nWarning: DOM and SAX returned different results.")

    fastest = "DOM" if dom_time < sax_time else "SAX"
    print(f"The fastest API in this run was: {fastest}")
    # On my test run, SAX was the fastest API.


if __name__ == "__main__":
    main()
