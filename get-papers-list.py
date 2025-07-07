import argparse
from get_papers.fetch import fetch_papers, fetch_details
from get_papers.utils import parse_article_data, write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="PubMed query")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug info")
    args = parser.parse_args()

    if args.debug:
        print("Fetching papers for query:", args.query)

    ids = fetch_papers(args.query)
    details = fetch_details(ids)
    parsed = parse_article_data(details)

    if args.file:
        write_to_csv(parsed, args.file)
    else:
        print(parsed)

if __name__ == "__main__":
    main()