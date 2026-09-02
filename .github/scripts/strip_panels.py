# 3D contrib SVG からレーダーと言語円グラフを除く。
# この2つは public repo しか集計されず、private 中心の活動実態と食い違うため。
import sys
import xml.etree.ElementTree as ET

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)
for path in sys.argv[1:]:
    tree = ET.parse(path)
    root = tree.getroot()
    for g in [c for c in list(root) if c.tag == f"{{{SVG_NS}}}g" and c.get("transform")]:
        root.remove(g)
    tree.write(path, encoding="unicode", xml_declaration=False)
