import yaml
import subprocess
import os


def read_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def get_commits(repo_path, target_file):
    os.chdir(repo_path)
    cmd = f"git log --pretty=format:'%h' -- {target_file}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Git error: {result.stderr}")
    return result.stdout.splitlines()


def generate_mermaid_graph(commits):
    graph_lines = ["graph TD"]
    for i in range(len(commits) - 1):
        graph_lines.append(f"    {commits[i]} --> {commits[i + 1]}")
    return "\n".join(graph_lines)


def save_mermaid_graph(graph, output_path):
    with open(output_path, 'w') as f:
        f.write(graph)


def visualize_graph(mermaid_file, output_image, visualizer_path):
    cmd = f"{visualizer_path} -i {mermaid_file} -o {output_image}"
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception("Failed to generate graph image")


def main(config_path):
    config = read_config(config_path)

    repo_path = config["repo_path"]
    visualizer_path = config["visualizer_path"]
    output_image = config["output_image"]
    target_file = config["target_file"]
    temp_mermaid_file = "temp_graph.mmd"

    commits = get_commits(repo_path, target_file)
    if not commits:
        print("No commits found for the specified file.")
        return

    graph = generate_mermaid_graph(commits)
    save_mermaid_graph(graph, temp_mermaid_file)
    visualize_graph(temp_mermaid_file, output_image, visualizer_path)
    os.remove(temp_mermaid_file)

    print("Dependency graph successfully created and saved as PNG.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Visualize dependency graph for Git commits.")
    parser.add_argument("config", help="Path to the YAML configuration file.")
    args = parser.parse_args()
    main(args.config)
