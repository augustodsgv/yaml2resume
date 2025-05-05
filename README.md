# Yaml2Resume

The objective of this project is to generate a resume PDF or HTML file based on a YAML file.

## 📦 Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📝 Create your YAML resume

Follow the structure shown in [`example.yaml`](example.yaml):

```yaml
first_name: Augusto
last_name: Vaz
job_title: Site Reliability Engineer at Magalu Cloud
location: São Carlos, SP
phone: (16) 99321-8075
email: augustodsgv@gmail.com
github: https://github.com/augustodsgv
linkedin: https://www.linkedin.com/in/augustodsgv/

educations:
  - degree_level: B. Sc.
    instituition: Universidade Federal de São Carlos (UFSCar)
    field: Computer Science
    start_date: aug 2024
    end_date: february 2025

experiences:
  - title: Site Reliability
    company: Magalu Cloud
    start_date: aug 2024
    end_date: today
    items:
      - Site Reliability Engineer in the IaaS Team.
      - Cloud monitoring with Prometheus and Grafana.

projects:
  - title: Cloud research with Magalu Cloud and UFSCar
    start_date: dec 2023
    end_date: oct 2024
    items:
      - Administration of physical cluster infrastructure.
```

## 🚀 Usage

Generate a **PDF**:

```bash
python3 yaml2resume.py example.yaml --pdf
```

Generate an **HTML**:

```bash
python3 yaml2resume.py example.yaml --html
```

Specify the output file:

```bash
python3 yaml2resume.py example.yaml --pdf --output vaz_resume.pdf
```

Generate both formats at once:

```bash
python3 yaml2resume.py example.yaml --html --pdf
```

Specify a custom **Jinja2 template** or **CSS style**:

```bash
python3 yaml2resume.py example.yaml --pdf \
  --template ./templates/modern.html.j2 \
  --style ./styles/modern.css
```

> ℹ️ If no `--output` is provided, it will generate `resume.pdf` and/or `resume.html` by default.