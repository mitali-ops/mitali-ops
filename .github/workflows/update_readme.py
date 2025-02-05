import requests
import datetime

# Load the existing README
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.readlines()

# Fetch the latest public GitHub repositories
GITHUB_USERNAME = "your-github-username"
response = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated")
repos = response.json()

# Format the latest repos
latest_repos = "\n".join([f"- [{repo['name']}]({repo['html_url']}) - ⭐ {repo['stargazers_count']}" for repo in repos[:5]])

# Inject latest repositories into README
for i, line in enumerate(readme):
    if "<!-- AUTO-UPDATE-START -->" in line:
        start_index = i + 1
    if "<!-- AUTO-UPDATE-END -->" in line:
        end_index = i
        break

# Update README content
new_readme = readme[:start_index] + [latest_repos + "\n"] + readme[end_index:]

# Write back to README
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(new_readme)

print("README updated successfully!")
