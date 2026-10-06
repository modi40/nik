import os
import sys
import ast

EXPECTED_FOLDERS = [
    "bfs-monkey-banana",
    "astar-shortest-path",
    "map-coloring-csp",
    "bfs-water-jug",
    "backtracking-csp",
    "game-tree",
    "bfs-graph",
    "alpha-beta-pruning",
    "propositional-logic",
    "state-space-bfs",
    "predicate-logic",
    "gaussian-naive-bayes",
    "tic-tac-toe-minimax",
    "four-puzzle-astar",
    "minimax-alpha-beta-comparison",
    "rule-based-expert-system",
    "hill-climbing",
    "forward-chaining",
    "decision-tree-classifier",
    "backward-chaining",
    "random-forest-classifier",
    "dfs-state-space",
    "clustering-objective-functions",
    "knowledge-base",
    "depth-limited-search",
    "kmeans-clustering",
    "best-first-search",
    "euclidean-distance",
    "tower-of-hanoi",
    "n-queens",
    "supervised-vs-unsupervised",
    "ao-star",
    "minimax"
]

def check_balanced_brackets(filepath, content):
    pairs = {')': '(', '}': '{', ']': '['}
    openers = set(pairs.values())
    stack = []
    
    in_single_quote = False
    in_double_quote = False
    in_triple_single = False
    in_triple_double = False
    escape = False
    
    i = 0
    length = len(content)
    line_num = 1
    
    while i < length:
        ch = content[i]
        
        if ch == '\n':
            line_num += 1
            escape = False
            i += 1
            continue
            
        if escape:
            escape = False
            i += 1
            continue
            
        if ch == '\\':
            escape = True
            i += 1
            continue
            
        if in_triple_single:
            if content[i:i+3] == ("'" * 3):
                in_triple_single = False
                i += 3
            else:
                i += 1
            continue
            
        if in_triple_double:
            if content[i:i+3] == ('"' * 3):
                in_triple_double = False
                i += 3
            else:
                i += 1
            continue
            
        if not in_single_quote and not in_double_quote:
            if content[i:i+3] == ("'" * 3):
                in_triple_single = True
                i += 3
                continue
            if content[i:i+3] == ('"' * 3):
                in_triple_double = True
                i += 3
                continue
                
        if ch == "'" and not in_double_quote:
            in_single_quote = not in_single_quote
            i += 1
            continue
            
        if ch == '"' and not in_single_quote:
            in_double_quote = not in_double_quote
            i += 1
            continue
            
        if in_single_quote or in_double_quote:
            i += 1
            continue
            
        if ch in openers:
            stack.append((ch, line_num))
        elif ch in pairs:
            if not stack:
                return False, f"Unmatched closing '{ch}' at line {line_num}"
            top_char, top_line = stack.pop()
            if top_char != pairs[ch]:
                return False, f"Mismatched bracket '{top_char}' (line {top_line}) closed by '{ch}' (line {line_num})"
                
        i += 1
        
    if stack:
        top_char, top_line = stack[-1]
        return False, f"Unclosed bracket '{top_char}' opened at line {top_line}"
        
    return True, None

def check_python_source(filepath, display_path):
    errors = []
    
    if not os.path.exists(filepath):
        return [f"{display_path} : File not found"]
        
    if os.path.getsize(filepath) == 0:
        return [f"{display_path} : Empty file"]
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if not content.strip():
        errors.append(f"{display_path} : File contains only whitespace")
        
    for line_idx, line in enumerate(content.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith('#') or stripped.startswith('//') or stripped.startswith('/*'):
            errors.append(f"{display_path} : Prohibited comment found at line {line_idx}")
            
    try:
        ast.parse(content, filename=filepath)
    except SyntaxError as e:
        errors.append(f"{display_path} : Syntax error at line {e.lineno}: {e.msg}")
        
    balanced, balance_err = check_balanced_brackets(filepath, content)
    if not balanced:
        errors.append(f"{display_path} : Bracket balance error: {balance_err}")
        
    return errors

def verify_all():
    errors = []
    syntax_ok = True
    comment_ok = True
    empty_ok = True
    mapping_ok = True
    duplicate_ok = True

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.isdir(os.path.join(base_dir, "AI")):
        ai_dir = os.path.join(base_dir, "AI")
        display_prefix = "AI"
    elif os.path.isdir(os.path.join(base_dir, "bfs-monkey-banana")):
        ai_dir = base_dir
        display_prefix = "AI"
    else:
        errors.append("Directory AI/ does not exist")
        ai_dir = None

    if ai_dir is None:
        print(f"Found {len(errors)} error(s):")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)

    search_script = os.path.join(base_dir, "search.py")
    if not os.path.exists(search_script):
        search_script_ai = os.path.join(ai_dir, "search.py")
        if not os.path.exists(search_script_ai):
            errors.append("search.py is missing")

    readme_file = os.path.join(base_dir, "README.md")
    if not os.path.exists(readme_file):
        readme_file_ai = os.path.join(ai_dir, "README.md")
        if not os.path.exists(readme_file_ai):
            errors.append("README.md is missing")

    index_file = os.path.join(base_dir, "QUESTION_INDEX.md")
    if not os.path.exists(index_file):
        index_file_ai = os.path.join(ai_dir, "QUESTION_INDEX.md")
        if not os.path.exists(index_file_ai):
            errors.append("QUESTION_INDEX.md is missing")

    total_folders_checked = 0
    total_source_files_checked = 0
    total_question_files_checked = 0

    seen_folders = set()
    for folder_name in EXPECTED_FOLDERS:
        if folder_name in seen_folders:
            duplicate_ok = False
            errors.append(f"Duplicate expected folder: {folder_name}")
        seen_folders.add(folder_name)

        folder_path = os.path.join(ai_dir, folder_name)
        if not os.path.isdir(folder_path):
            mapping_ok = False
            errors.append(f"Missing program folder: {display_prefix}/{folder_name}")
            continue

        total_folders_checked += 1

        sol_file = os.path.join(folder_path, "solution.py")
        disp_sol = f"{display_prefix}/{folder_name}/solution.py"
        sol_errors = check_python_source(sol_file, disp_sol)
        if sol_errors:
            for err in sol_errors:
                if "Syntax error" in err or "Bracket" in err:
                    syntax_ok = False
                if "Prohibited comment" in err:
                    comment_ok = False
                if "Empty file" in err:
                    empty_ok = False
            errors.extend(sol_errors)
        else:
            total_source_files_checked += 1

        q_file = os.path.join(folder_path, "question.txt")
        disp_q = f"{display_prefix}/{folder_name}/question.txt"
        if not os.path.exists(q_file):
            mapping_ok = False
            errors.append(f"{disp_q} : Missing question file")
        elif os.path.getsize(q_file) == 0:
            empty_ok = False
            errors.append(f"{disp_q} : Empty question file")
        else:
            with open(q_file, 'r', encoding='utf-8') as qf:
                q_text = qf.read()
            if "Original Question:" not in q_text or "Occurrences:" not in q_text:
                mapping_ok = False
                errors.append(f"{disp_q} : Invalid question format (missing sections)")
            else:
                total_question_files_checked += 1

    print("========================================")
    print("AI PRACTICAL VERIFICATION")
    print("========================================")
    print(f"Total program folders checked: {total_folders_checked}")
    print(f"Total source files checked: {total_source_files_checked}")
    print(f"Total question files checked: {total_question_files_checked}")
    print()
    print(f"Syntax validation: {'PASS' if syntax_ok and not [e for e in errors if 'Syntax' in e] else 'FAIL'}")
    print(f"Comment validation: {'PASS' if comment_ok and not [e for e in errors if 'Prohibited comment' in e] else 'FAIL'}")
    print(f"Empty-file validation: {'PASS' if empty_ok and not [e for e in errors if 'Empty' in e] else 'FAIL'}")
    print(f"Question mapping: {'PASS' if mapping_ok and not [e for e in errors if 'Missing' in e] else 'FAIL'}")
    print(f"Duplicate handling: {'PASS' if duplicate_ok else 'FAIL'}")
    print()

    if errors:
        print(f"Found {len(errors)} error(s):")
        for err in errors:
            print(f"- {err}")
        sys.exit(1)
    else:
        print("ALL FILES PASSED VERIFICATION!")
        sys.exit(0)

if __name__ == "__main__":
    verify_all()
