import wikipediaapi
import re
import json
from termcolor import colored
import calendar

def get_notable_deaths(starting_year, ending_year):

    wiki_wiki = wikipediaapi.Wikipedia(user_agent='NotableDeaths1990-2024 (elia9605@hotmail.it)', language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)

    pattern = r"(?:,|(?<!\w)c\.?|(?<!\w)appr?\.?|(?<!\w)abo?u?t?\.?) ?(?P<age>\d{1,4}(?:-\d{1,4})?)"

    db = []
    for year in range(starting_year, ending_year + 1):
        # create year dict
        new_year = {"year": year, "months": []}

        for month in calendar.month_name[1:]:
            # get month's deaths page and check if it exists
            deaths_month = wiki_wiki.page(f"Deaths_in_{month}_{year}")
            if not deaths_month.exists():
                print(colored(f"Skipping {month} {year}"), "yellow", attrs="bold")
                continue
            print(f"Processing {month} {year}")
            # create month dict
            new_month = {"month": month, "days": []}

            # get days sections
            deaths_days = deaths_month.section_by_title(f"{month} {year}")
            # for each day section, get text and split it in single lines
            for day in deaths_days.sections:
                lines = day.text.split("\n")
                if not lines:
                    continue
                # create day dict
                new_day = {"day": day.title, "deaths": []}
                
                # parse every line retrieving corresponding death's information
                for line in lines:
                    # skip 'References' lines and introductory lines to groups of deaths
                    if line == "== References ==" or line.startswith("Notable") or not line:
                        continue
                    # usually age of death is reported; search for it and split line in name and info
                    if match := re.search(pattern, line):
                        age = match.group("age")
                        line = re.split(match.group(), line, maxsplit=1)
                        name = line[0].rstrip(", ")
                        info = line[1].lstrip(" ,")
                    # if no age found, try splitting line to retrieve name and info
                    else:
                        line = re.split(r", (?!Jr.?|Sr.?)", line, maxsplit=1)
                        if len(line) != 1:
                            age = None
                            name = line[0].rstrip(", ")
                            info = line[1].lstrip(" ,")
                        # if line can't be splitted, check if it is an introductory line to a group of deaths and skip it
                        elif not re.search(r"(?:killed|victims|shot|died)", line[0], re.I):
                            age = None
                            name = line[0]
                            info = None
                        else:
                            continue

                    # create person dict and and append nested dicts to db
                    person = {"Name": name, "Age": age, "Info": info}
                    new_day["deaths"].append(person)
                new_month["days"].append(new_day)
            new_year["months"].append(new_month)
        db.append(new_year)

    # write db in file.json
    with open("wiki_deaths.json", "w") as f:
        json.dump(db, f, indent=3)

if __name__ == "__main__":
    get_notable_deaths(1990, 2024)