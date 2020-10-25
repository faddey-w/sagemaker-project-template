import argparse
from my_project import infrastructure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wait", action="store_true")
    args = parser.parse_args()

    model_name = "test8"  # name for experiment, something descriptive

    src_pkg_path = infrastructure.build_source_distribution(suppress_stdout=True)
    src_pkg_s3_path = infrastructure.upload_source_distribution(model_name, src_pkg_path)

    infrastructure.run_job(
        src_s3_path=src_pkg_s3_path,
        entry_point_module="my_project.jobs.something_checkpointable",
        instance_count=1,
        instance_type="ml.m5.large",
        job_base_name=model_name,
        max_run_time=3 * 3600,
        s3_output_path="models/" + model_name,
        wait=args.wait,
    )


if __name__ == "__main__":
    main()
