import os
import sys

def search_questions(search_term, base_path=None):
    if base_path is None:
        if os.path.isdir("AI"):
            ai_root = "AI"
            display_prefix = "AI/"
        else:
            ai_root = "."
            display_prefix = "AI/"
    else:
        ai_root = base_path
        display_prefix = "AI/"

    matching_folders = []
    terms = search_term.lower().split()

    if not os.path.exists(ai_root):
        print(f"Directory {ai_root} not found.")
        return

    items = sorted(os.listdir(ai_root))
    for item in items:
        folder_path = os.path.join(ai_root, item)
        if not os.path.isdir(folder_path):
            continue
        q_file = os.path.join(folder_path, "question.txt")
        if not os.path.isfile(q_file):
            continue

        with open(q_file, "r", encoding="utf-8") as f:
            content = f.read()

        folder_name_lower = item.lower()
        content_lower = content.lower()
        search_term_lower = search_term.lower()

        matches = False
        if search_term_lower in folder_name_lower or search_term_lower in content_lower:
            matches = True
        elif all(t in content_lower or t in folder_name_lower for t in terms):
            matches = True

        if matches:
            original_q = ""
            occurrences = []
            lines = content.splitlines()
            reading_q = False
            reading_occ = False
            for line in lines:
                sline = line.strip()
                if sline == "Original Question:":
                    reading_q = True
                    reading_occ = False
                    continue
                elif sline == "Keywords:":
                    reading_q = False
                    reading_occ = False
                    continue
                elif sline == "Occurrences:":
                    reading_q = False
                    reading_occ = True
                    continue

                if reading_q and sline:
                    if original_q:
                        original_q += " " + sline
                    else:
                        original_q = sline
                elif reading_occ and sline:
                    occurrences.append(sline)

            sol_path = f"{display_prefix}{item}/solution.py"
            matching_folders.append({
                "program": item,
                "question": original_q,
                "solution": sol_path,
                "occurrences": occurrences
            })

    print(f"SEARCH RESULTS FOR: {search_term}\n")
    print("-" * 40)
    if not matching_folders:
        print("No matching programs found.")
        print("-" * 40)
        return

    for res in matching_folders:
        print()
        print("Program:")
        print(res["program"])
        print()
        print("Question:")
        print(res["question"])
        print()
        print("Solution:")
        print(res["solution"])
        print()
        print("Occurrences:")
        for occ in res["occurrences"]:
            print(occ)
        print()
        print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        try:
            query = input("Enter search term: ").strip()
        except EOFError:
            query = "Map Coloring"
    if not query:
        query = "Map Coloring"
    search_questions(query)
