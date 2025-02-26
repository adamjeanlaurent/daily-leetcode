#!/bin/bash


# Define allowed problem types
VALID_TYPES=(
    "array" "two-pointer" "sliding-window" "stack" "binary-search" "linked-list" \
    "tree" "heap" "backtracking" "trie" "graph" "greedy" "1d-dynamic" "2d-dynamic"
)

# Function to display help
function show_help {
    echo "Usage: $0 --problem=<problem-name> --type=<problem-type>"
    echo "\nValid problem types:"
    for type in "${VALID_TYPES[@]}"; do
        echo "  - $type"
    done
    exit 0
}

# Parse arguments
for arg in "$@"; do
    case $arg in
        --problem=*)
            PROBLEM_NAME="${arg#*=}"
            ;;
        --type=*)
            PROBLEM_TYPE="${arg#*=}"
            ;;
        --help)
            show_help
            ;;
        *)
            echo "Invalid argument: $arg"
            show_help
            ;;
    esac
done

# Validate inputs
if [[ -z "$PROBLEM_NAME" || -z "$PROBLEM_TYPE" ]]; then
    echo "Error: Both --problem and --type are required."
    show_help
fi

# Check if problem type is valid
if [[ ! " ${VALID_TYPES[@]} " =~ " $PROBLEM_TYPE " ]]; then
    echo "Error: Invalid problem type '$PROBLEM_TYPE'."
    show_help
fi

# Get today's date in MM/DD/YYYY format
TODAYS_DATE=$(date +"%m/%d/%Y")

# Define file path
FILE_PATH="./src/leetcode/neetcode-150/$PROBLEM_TYPE/$PROBLEM_NAME.py"

# Create directories if they don't exist
mkdir -p "$(dirname "$FILE_PATH")"

# Write content to the file
cat > "$FILE_PATH" <<EOF
'''
    Link: https://leetcode.com/problems/$PROBLEM_NAME/

    Time Took: 

    Time Complexity:

    Space Complexity:

    Date: $TODAYS_DATE

    Problem Type: $PROBLEM_TYPE

    Solution Explained:

    Notes:
'''
EOF

# Confirm file creation
echo "Created file: $FILE_PATH"
