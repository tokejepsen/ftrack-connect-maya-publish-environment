import os

from conda_git_deployment import utils


repo_root = os.path.join(os.path.dirname(__file__))
env = {}

# PYTHONPATH
env["PYTHONPATH"] = [
    os.path.join(repo_root, "environment", "PYTHONPATH"),
]

# Setting environment.
for variable in env:
    path = ""
    for item in env[variable]:
        path += os.pathsep + item

    try:
        os.environ[variable] += path
    except:
        os.environ[variable] = path[1:]


utils.write_environment(os.environ)
