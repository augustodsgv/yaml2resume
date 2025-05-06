"""
Script for generating resumes based YAML files.
"""

import sys
from typing import List, Dict
from dataclasses import dataclass
import argparse
import yaml
import jinja2
import pdfkit


@dataclass
class ResumeData:
    """
    Stores the resume data.
    """

    first_name: str
    last_name: str
    job_title: str
    location: str
    phone: str
    email: str
    linkedin: str
    github: str
    experiences: List[Dict]
    educations: List[Dict]
    projects: List[Dict]
    hard_skills: List[str]
    soft_skills: List[str]


class Yaml2Resume:
    """
    Parses the yaml and provides html and pdf output.
    """

    def __init__(
        self,
        data: str,
        template_file: str,
        style_file: str,
    ):
        self.data = data
        self.template_file = template_file
        self.style_file = style_file

    @property
    def _html(self) -> str:
        """
        Uses the jinja template to create the html resume and returns the generated string.
        """
        # Embbeds the css style inside the html
        with open(self.style_file, encoding='utf-8') as sf:
            style = sf.read()

        env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
        template = env.get_template(self.template_file)
        return template.render(
            first_name=self.data.first_name,
            last_name=self.data.last_name,
            job_title=self.data.job_title,
            location=self.data.location,
            phone=self.data.phone,
            email=self.data.email,
            linkedin=self.data.linkedin,
            github=self.data.github,
            experiences=self.data.experiences,
            educations=self.data.educations,
            projects=self.data.projects,
            hard_skills=self.data.hard_skills,
            soft_skills=self.data.soft_skills,
            style=style
        )

    def gen_html(self, output_file: str) -> None:
        """
        Generates a html resume.
        """
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self._html)
        print("HTML resume generated!")

    def gen_pdf(self, output_file: str) -> None:
        """
        Generates a pdf resume.
        """
        pdfkit.from_string(
            self._html,
            output_file,
            options={
                'margin-top': '0in',
                'margin-right': '0in',
                'margin-bottom': '0in',
                'margin-left': '0in',
                'page-size': 'A4'  # Optional: control page size
            }
        )

        # pdfkit.from_string(, output_file)
        print("PDF resume generated!")

    @classmethod
    def from_yaml(cls, file_name: str, template_file: str, style_file: str) -> "Yaml2Resume":
        """
        Creates a Resume object from a YAML file
        """
        with open(file_name, encoding="utf-8") as yaml_file:
            yaml_dict = dict(yaml.safe_load(yaml_file))

        resume_data = ResumeData(
            first_name=yaml_dict["first_name"],
            last_name=yaml_dict["last_name"],
            job_title=yaml_dict["job_title"],
            location=yaml_dict["location"],
            phone=yaml_dict["phone"],
            email=yaml_dict["email"],
            github=yaml_dict["github"],
            linkedin=yaml_dict["linkedin"],
            experiences=yaml_dict["experiences"],
            educations=yaml_dict["educations"],
            projects=yaml_dict["projects"],
            hard_skills=yaml_dict["hard_skills"],
            soft_skills=yaml_dict["soft_skills"],
        )
        return Yaml2Resume(
            resume_data,
            template_file=template_file,
            style_file=style_file,
        )


def main():
    """Handles the CLI."""
    parser = argparse.ArgumentParser(
        prog="resume", description="Script for creating a resume based on a yaml file"
    )

    parser.add_argument("yaml", help="Path of the YAML file")
    parser.add_argument("--output", help="Path to output file")
    parser.add_argument("--html", help="Generates an HTML output", action="store_true")
    parser.add_argument("--pdf", help="Generates an PDF output", action="store_true")
    parser.add_argument(
        "--template",
        help="Path to Jinja2 template file",
        default="./templates/basic.html.j2",
    )
    parser.add_argument(
        "--style", help="Path to css style file", default="./styles/basic.css"
    )
    args = parser.parse_args()

    if not args.html and not args.pdf:
        print(
            "Error: missing output file type. Use --html or --pdf to generate output."
        )
        sys.exit(1)

    y2r = Yaml2Resume.from_yaml(args.yaml, args.template, args.style)

    if args.html:
        if not args.output:
           y2r.gen_html("resume.html")
        else:
           y2r.gen_html(args.output)

    if args.pdf:
        if not args.output:
           y2r.gen_pdf("resume.pdf")
        else:
           y2r.gen_pdf(args.output)


if __name__ == "__main__":
    main()
