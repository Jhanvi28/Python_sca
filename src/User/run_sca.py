import subprocess
import os

def run_command(command):
    """Run a shell command and return its output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()

def write_to_html(filename, content):
    """Write content to an HTML file."""
    with open(filename, 'w') as f:
        f.write(content)

def generate_report():
    html_report = "<html><body>"

    # Run black
    html_report += "<h2>Black</h2><pre>"
    stdout, stderr = run_command("black . --check")
    html_report += stdout + stderr + "</pre>"

    # Run bandit
    html_report += "<h2>Bandit</h2><pre>"
    stdout, stderr = run_command("bandit -r . -f html")
    html_report += stdout + stderr + "</pre>"

    # Run mypy
    html_report += "<h2>Mypy</h2><pre>"
    stdout, stderr = run_command("mypy . --html-report mypy_report")
    if os.path.exists('mypy_report/index.html'):
        with open('mypy_report/index.html', 'r') as f:
            html_report += f.read()
    html_report += "</pre>"

    # Run pylint
    html_report += "<h2>Pylint</h2><pre>"
    stdout, stderr = run_command("pylint . --output-format=json > pylint_report.json")
    stdout, stderr = run_command("pylint-json2html -o pylint_report.html pylint_report.json")
    if os.path.exists('pylint_report.html'):
        with open('pylint_report.html', 'r') as f:
            html_report += f.read()
    html_report += "</pre>"

    # Run flake8
    html_report += "<h2>Flake8</h2><pre>"
    stdout, stderr = run_command("flake8 . --format=html --htmldir=flake8_report")
    if os.path.exists('flake8_report/index.html'):
        with open('flake8_report/index.html', 'r') as f:
            html_report += f.read()
    html_report += "</pre>"

    html_report += "</body></html>"
    html_report += "</body></html>"


    write_to_html("sca_report.html", html_report)

if __name__ == "__main__":
    generate_report()
