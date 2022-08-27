from typing import Optional
import re
from bs4 import BeautifulSoup, PageElement, ResultSet, Tag
from pyparsing import And
from selenium import webdriver
import logic

units_pattern = re.compile(r"(?:(\d+) to )?(\d+) units")

def units_str_to_minmax(units: str) -> Optional[tuple[int, int]]:
    result = re.search(units_pattern, units)
    if result is None:
        return None
    max = result.group(2)
    min = max if result.group(1) is None else result.group(1)
    return int(min), int(max)

def url_to_soup(url: str) -> BeautifulSoup:
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options) 
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def parse_program_rules_description(desc_div: Tag, data: logic.Module) -> None:
    """
    Parses a program-rules__description div and populates the given module.
    data.rec is overwritten.
    """
    units = desc_div.p.find(string=units_pattern)
    min, max = units_str_to_minmax(units.string)
    data.rec = logic.And(min, max, [])
    
    prev_indentlevel = 0
    indentitems = [data.rec]  # keep a stack of indent items

    for li in desc_div.ul.children:
        indentlevel = int(li["class"][0].partition("ql-indent-")[2]) - 1
        if indentlevel < prev_indentlevel:
            indentitems.pop()
        
        s = "".join(li.strings).lower()
        if "either" in s or "one of" in s or "one from" in s:
            newitem = logic.Or([])
            indentitems[-1].ll.append(newitem)
            indentitems.append(newitem)
            continue
        
        li_min, li_max = units_str_to_minmax(s)
        li_name = li.find_all("strong")[-1].string
        
        # we'll just make this a placeholder to hold min and max
        # this should be changed from And if necessary in later stages.
        rec = logic.And(li_min, li_max, [])

        indentitems[-1].ll.append(logic.Module(li_name, rec))

        prev_indentlevel = indentlevel

def parse_course_button(a: Tag, jc: logic.JoinedCourse) -> None:
    """
    Parses a course button.
    I don't know if this works with majors.
    """
    course_code = a.find(class_="curriculum-reference__code").string
    unit_int = int(a.find(class_="curriculum-reference__units").string.split()[0])
    course_name = a.find(class_="curriculum-reference__name").string
    course = logic.Course(course_code, unit_int, course_name)
    jc.add_course(course)

def parse_selection_list(rows: ResultSet[PageElement], data: logic.Module) -> None:
    """
    Parses a list of elements with the selection-list__row class.
    data.rec is assumed to be Leaf.
    """
    for row in rows:
        jc = logic.JoinedCourse()
        if row.name == "div":
            for a in row.children:
                parse_course_button(a, jc)
        elif row.name == "a":
            parse_course_button(row, jc)
        data.rec.ll = jc

def recursive_descent(pos: Tag, data: logic.Module) -> None:
    """
    Does the recursive descent step.
    We assume we've just matched the header title with a module,
    which got passed in as data, and our position is at pos.
    """
    immediate_child = pos.contents[0]  # possibly optimise using next(pos.children)
    
    if "program-rules__description" in immediate_child["class"]:
        # we've reached a description list, not a course list yet
        # use helper function with this specific node
        desc_div = pos.find(class_="program-rules__description")
        parse_program_rules_description(desc_div, data)
        
        # then go to program-rules__parts (we skip over part__rule--auxiliary)
        # and iterate over children. do the matching and then recurse
        parts_div = desc_div.find_next_sibling("div", class_="program-rules__parts")
        for part in parts_div.children:
            # each of these has a "part__header" div, containing the part title,
            # and a "part__content" div, containing subrequirements and subparts.
            # we first need to find which module this part corresponds to.
            title = part.find("div", class_="part__header").string
            
            ### THIS IS JUST TO MAKE THINGS EASIER FOR US NOW
            if "major" in title.lower() or "minor" in title.lower():
                continue
            ### DELETE ABOVE IF NECESSARY
            
            for module in data.rec.ll:
                if title.strip() == module.name:
                    part_module = module
                    break
            else:
                raise ValueError("part present that isn't in initial program-rules__description")
            # now that we now the relevant module, we recurse,
            # with our pos set to program-rules__content.
            content = part.find("div", class_="part__content")
            recursive_descent(content, part_module)
        
    elif "part__rule--selection" in immediate_child["class"]:
        # we've reached a course/major list
        # iterate over children with selection-list__row
        min, max = units_str_to_minmax(immediate_child.string)
        assert min == data.rec.min and max == data.rec.max
        # replace rec with Leaf
        new_rec = logic.Leaf(min, max, [])
        data.rec = new_rec
        
        rows = immediate_child.find_next_siblings(class_="selection-list__row")
        parse_selection_list(rows, data)

    else:
        raise ValueError(f"edge case, {immediate_child['class']}")

def soup_to_structure(soup: BeautifulSoup):
    data = logic.Module("root", None)
    root = soup.find("div", class_="program-rules")
    recursive_descent(root, data)
    return data

if __name__ == "__main__":
    url = "https://my.uq.edu.au/programs-courses/requirements/program/2460/2023"
    soup = url_to_soup(url)
    data = soup_to_structure(soup)
    print(data)