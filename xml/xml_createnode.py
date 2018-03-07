import xml.dom.minidom

main_content = xml.dom.minidom.parse("something2.xml")


newlanguage = main_content.createElement("Language")
newlanguage.setAttribute("name", "Ruby")
main_content.firstChild.appendChild(newlanguage)

content2 = main_content.getElementsByTagName("Language")

for data in content2:
    print data.getAttribute("name") 
    
