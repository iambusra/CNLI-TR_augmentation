import re
from scraper import get_link_content, get_links


def get_namepages_in(hyperlink):
	links = get_links(hyperlink)

	return ["https://isimbulamadim.com"+link for link in links if re.search("-isminin-anlami/$", link)]


def get_name_info(hyperlink):
	content = get_link_content(hyperlink)
	info = __extract_name_info(content)

	return info
	

def __extract_name_info(content):
	if(len(content.splitlines()) == 451):
		return None

	chunk = content[content.find(start:="İsmi İle İlgili Bilgiler")+len(start):content.find(" Kuran'da geçiyor mu")]
	lines = [line.replace(" ", r"") for line in chunk.splitlines()]

	name = lines[-1]

	gender = [element for element in lines if re.search("^(Erkek|Kız)$", element)]
	gender = '-'.join(gender)
	
	origin = [element for element in lines if re.search("^(Farsça|Türkçe|Arapça|Yunanca|Moğolca|Gürcüce|İbranice|Bilinmiyor)$", element)]
	origin = '-'.join(origin)

	return (name, gender, origin)


