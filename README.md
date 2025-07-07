# get-papers-list

This tool fetches PubMed research papers based on a query, filters for pharmaceutical/biotech author affiliations, and outputs a CSV file.

## Usage

```bash
poetry run get-papers-list "cancer immunotherapy" -f results.csv
```

## Flags
- `-h, --help`: Show usage
- `-f, --file`: Output filename
- `-d, --debug`: Enable debug logs

## Setup

```bash
poetry install
```

## Organization

- `fetch.py`: Handles PubMed API requests
- `utils.py`: Filters and formats results
- `get-papers-list.py`: CLI entry point