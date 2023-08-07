import ghapi.all as ghapi
import json

if __name__ == "__main__":
    g = ghapi.GhApi()

    # Get all repos for the authenticated user
    g = ghapi.GhApi()
    searchStr = f"org:jmoney topic:mkdocs topic:github-site"

    # TODO - Add Pagination. Right now it assumes that each search will return less than 100 results
    repos = g.search.repos(searchStr, order="asc", sort="name", per_page=100)

    output = []
    for repo in repos['items']:
        output.append(repo['full_name'])

    print(json.dumps(output))

