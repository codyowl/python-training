import xml.dom.minidom

main_content = xml.dom.minidom.parse("something2.xml")

# print main_content.nodeName
# print main_content.firstChild.tagName

# content2 = main_content.getElementsByTagName("Language")

# print content2

# for data in content2:
#     print data.getAttribute("name") 

newlanguage = main_content.createElement("Language")
newlanguage.setAttribute("name", "Ruby")
main_content.firstChild.appendChild(newlanguage)

content2 = main_content.getElementsByTagName("Language")

for data in content2:
    print data.getAttribute("name") 
    
