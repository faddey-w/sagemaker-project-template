import os
import sys
import subprocess
import boto3
from . import paths


SOURCE_DIST_DIR = os.path.join(paths.TMP, "dist")


def build_source_distribution(output_dir=None, suppress_stdout=False):
    """
    Creates pip-installable .tar.gz archive by running python setup.py sdist over the project.
    Returns path to the created file.
    """
    if output_dir is None:
        output_dir = SOURCE_DIST_DIR
    subprocess.check_call(
        [
            sys.executable,
            os.path.join(paths.REPO_ROOT, "setup.py"),
            "sdist",
            "--dist-dir",
            output_dir,
        ],
        stdout=subprocess.DEVNULL if suppress_stdout else None,
        stderr=subprocess.STDOUT,
    )
    dist_filename = max(os.listdir(output_dir), key=_get_version)
    return os.path.join(output_dir, dist_filename)


def _get_version(dist_name):
    try:
        version_part = dist_name.rstrip(".tar.gz").rpartition("-")[2]
        return tuple(map(int, version_part.split(".")))
    except (ValueError, IndexError):
        return (-1,)


def get_source_distribution_s3_path(name):
    return os.path.join(paths.S3_SRC_BUILDS_ROOT, name + ".tar.gz")


def upload_source_distribution(name, local_path):
    boto3.Session(profile_name=paths.AWS_PROFILE).client("s3").upload_file(
        local_path, paths.S3_BUCKET, get_source_distribution_s3_path(name)
    )
