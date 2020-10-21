"""Tag replacer."""
# Standard Python Libraries
import glob
import json
import os
import re
import shutil


def replace_tags(source_directory, profile_json):
    """Replace tags."""
    target = re.sub("_Template", "_Website", source_directory)
    if not os.path.exists(profile_json):
        raise NameError("profile does not exist")
    if os.path.exists(target):
        shutil.rmtree(target)
    if not os.path.exists(target):
        shutil.copytree(
            source_directory,
            target,
        )

    files = glob.glob(target + "/**/*.html", recursive=True)

    for filename in files:
        j = open(profile_json)
        tags = json.load(j)
        update_file(filename, tags)
        j.close()


def update_file(template, tags):
    """Update file."""
    with open(template, "r") as t:
        html = t.read()
        for tag in tags:
            html = html.replace(tag["tag"], tag["value"])
    t.close()

    with open(template, "w") as t:
        t.write(html)
    t.close()


replace_tags(
    "./src/template/templates/Family_Lawyer_Template",
    "./src/template/templates/Family_Lawyer_Template/profile.json",
)