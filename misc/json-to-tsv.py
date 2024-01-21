import json
import sys

# Convert specified json to tsv (to paste spreadsheets directly).
# > python summary.py out.json
def process_json_data(json_data):
    data = json.loads(json_data)
    author_counts = {}

    for date, authors in data.items():
        for author_data in authors:
            author = author_data['author']
            count = author_data['count']
            if author not in author_counts:
                author_counts[author] = {}
            author_counts[author][date] = count

    dates = sorted(data.keys())
    header = "\t" + "\t".join(dates)
    lines = [header]
    for author, counts in author_counts.items():
        counts_str = [str(counts.get(date, "")) for date in dates]
        line = f"{author}\t" + "\t".join(counts_str)
        lines.append(line)

    return "\n".join(lines)

def main():
    # Check if a file path is provided
    if len(sys.argv) < 2:
        print("Usage: python json-to-tsv.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    with open(json_file, 'r') as file:
        json_data = file.read()

    result = process_json_data(json_data)
    print(result)

if __name__ == "__main__":
    main()
