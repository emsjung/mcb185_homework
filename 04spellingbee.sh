gunzip -c dictionary.gz | grep -E '^[rozncia]*$' | grep -E .'{4,}' | grep -E "r"

