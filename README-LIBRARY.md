# BMAD Methods Library

**Your Single Source of Truth for 206,902 Methods**

✅ **Complete** | 🔍 **Searchable** | ⚡ **Fast** | 🎯 **Integrated**

---

## What Is This?

The BMAD Methods Library consolidates every `bmad-methods.csv` file scattered across the Alexandria ecosystem into **one unified, searchable library**. No more hunting through 200+ files to find a method.

**What You Get**:
- 206,902 methods indexed and searchable
- 6 programming language categories (Python, JavaScript, Solidity, Shell)
- 15,628 unique modules/files tracked
- 6 execution modes (quick, full, batch, party, interactive, debug)
- Fast O(1) lookup by ID, category, module, or mode
- Complete metadata for every method

---

## Getting Started (30 seconds)

### View Library Statistics

```bash
cd /home/ichigo/alexandria/anima-mundi/defense/alexandria-core/_ARCHIVE_CHAOS/BMAD-METHOD
./bmad-methods stats
```

### Search for Methods

```bash
# Find methods by keyword
./bmad-methods search "analyze"
./bmad-methods search "deploy" --limit 100

# Show full details
./bmad-methods search "router" --full
```

### Filter by Category

```bash
# Find all Python methods
./bmad-methods category CODE_PYTHON

# Find all JavaScript structures
./bmad-methods category STRUCT_JAVASCRIPT --limit 20
```

### Filter by Execution Mode

```bash
# Find quick execution methods (CI/CD friendly)
./bmad-methods mode quick

# Find batch-compatible methods
./bmad-methods mode batch --full
```

### Get Specific Method

```bash
./bmad-methods get MTH-F7E621F8 --full
```

---

## Library Structure

```
BMAD-METHOD/
├── library/
│   ├── bmad-methods-consolidated.csv      # Main data (206K methods, 49MB)
│   ├── bmad-methods-consolidated.json     # JSON format (97MB)
│   ├── bmad-methods-index.json            # Fast lookup index (118MB)
│   └── bmad-methods-library.yaml          # Library definition & modes
│
├── tools/
│   ├── query-methods.py                   # Query engine (Python)
│   └── consolidate-methods.py             # Consolidation script
│
├── bmad-methods                           # CLI wrapper (this script)
├── LIBRARY-DISCOVERY.md                   # Complete discovery guide
├── README-LIBRARY.md                      # This file
└── CSV-AI-ANALYZER-INTEGRATION.md         # CSV analyzer integration
```

---

## Key Files

### `bmad-methods-consolidated.csv`

Main library file with all methods:

```csv
method_id,method_name,description,category,file_path,line_number,type,_source_file,execution_modes
MTH-F7E621F8,RustAnalyzer,Rust code analyzer,STRUCT_PYTHON,rust_analyzer.py,42,CLASS,json-mcp-blower/bmad-methods.csv,"quick,batch"
MTH-3E8FCAD5,index,Package indexer,CODE_PYTHON,app.py,14,FUNCTION,anima-mundi/bmad-methods.csv,"full,batch"
```

**206,903 lines** | Fully deduplicated by method_id

### `bmad-methods-index.json`

Fast lookup indices:

- **by_id**: Method ID → full method object (206,902 entries)
- **by_category**: Category → [method IDs] (6 categories)
- **by_module**: Module → [method IDs] (15,628 modules)
- **by_mode**: Mode → [method IDs] (6 execution modes)

Perfect for programmatic access and fast filtering.

### `bmad-methods-library.yaml`

Library configuration with mode definitions:

```yaml
execution_modes:
  quick:
    timeout: 60
    parallelizable: true
    use_cases: [CI/CD, pre-commit hooks]
  full:
    timeout: 600
    parallelizable: false
    use_cases: [initial analysis, reports]
  batch:
    timeout: 3600
    parallelizable: true
    use_cases: [scheduled jobs, automation]
  # ... 3 more modes (party, interactive, debug)
```

---

## Execution Modes Explained

Every method supports multiple execution modes with different characteristics:

| Mode | Timeout | Parallel | Best For |
|------|---------|----------|----------|
| **quick** ⚡ | 60s | ✅ | Pre-commit hooks, CI/CD checks, rapid feedback |
| **full** 🎯 | 600s | ❌ | Initial analysis, comprehensive reports, team presentations |
| **batch** 📦 | 3600s | ✅ | Scheduled jobs, CI/CD pipelines, bulk processing |
| **party** 🎭 | 1800s | ✅ | Multi-LLM consensus, pattern synthesis |
| **interactive** 💬 | user-paced | ❌ | Exploratory analysis, interactive debugging |
| **debug** 🐛 | user-paced | ❌ | Troubleshooting, performance profiling |

---

## Library Statistics

**Last Updated**: 2025-12-19

### By Category

| Category | Count | Percentage | Language |
|----------|-------|------------|----------|
| CODE_PYTHON | 108,010 | 52% | Python functions/procedures |
| CODE_JAVASCRIPT | 53,898 | 26% | JavaScript functions |
| STRUCT_PYTHON | 27,701 | 13% | Python classes |
| CODE_SOLIDITY | 16,031 | 8% | Smart contracts |
| STRUCT_JAVASCRIPT | 768 | <1% | JS classes/components |
| CODE_SHELL | 494 | <1% | Shell scripts |

### Top 10 Modules (by method count)

1. `__init__.py` - 6,754 methods
2. `swagger-ui-bundle.js` - 2,646 methods
3. `base.py` - 2,502 methods
4. `index.ts` - 1,780 methods
5. `Vm.sol` - 1,349 methods
6. `util.py` - 1,303 methods
7. `utils.py` - 1,252 methods
8. `index.tsx` - 1,054 methods
9. `utils.ts` - 973 methods
10. `core.py` - 867 methods

### Execution Mode Coverage

- **full + batch**: 206,902 methods (100%)
- **quick**: ~40,000+ methods (analysis-focused)
- **party**: ~30,000+ methods (multi-LLM capable)
- **interactive**: ~20,000+ methods (exploration-friendly)
- **debug**: Available on all methods

---

## Query Examples

### Find Analysis Methods

```bash
./bmad-methods search "analysis"
./bmad-methods search "analyze" --limit 200 --full
```

### Find All Deployment Methods

```bash
./bmad-methods search "deploy"
./bmad-methods search "deploy" --limit 500
```

### Find Class Definitions

```bash
./bmad-methods category STRUCT_PYTHON --limit 100
./bmad-methods category STRUCT_JAVASCRIPT
```

### Find Quick Execution Methods

```bash
./bmad-methods mode quick --limit 50
./bmad-methods mode quick --full
```

### Find All Methods in a File

```bash
./bmad-methods module "utils.py"
./bmad-methods module "index.ts" --full
```

### Get Method Details

```bash
./bmad-methods get MTH-F7E621F8 --full
```

---

## Integration Patterns

### Use in BMAD Workflows

```yaml
tasks:
  - id: find_methods
    action: query_library
    inputs:
      search: "analyze"
      mode: "batch"
    outputs:
      method_ids: "{{ query.results }}"
```

### Use in Shell Scripts

```bash
#!/bin/bash
# Find and execute all Python analysis methods
./bmad-methods search "analysis" --category CODE_PYTHON | while read method; do
  echo "Processing: $method"
  bmad run "$method" --mode=quick
done
```

### Use in Python Scripts

```python
import json
from pathlib import Path

# Load library index
index_file = Path("library/bmad-methods-index.json")
with open(index_file) as f:
    index = json.load(f)

# Find methods by category
python_methods = index["by_category"]["CODE_PYTHON"]

# Find methods by mode
quick_methods = index["by_mode"]["quick"]

# Get full method details
method = index["by_id"]["MTH-F7E621F8"]
```

### Use with BMAD Party Mode

```yaml
party_analysis:
  action: party_mode
  participants:
    - claude-3-opus
    - gpt-4-turbo
    - methods-analyzer  # Query library for insights
  task: "Analyze methods and find patterns"
```

---

## CLI Wrapper Reference

The `bmad-methods` script provides a convenient interface:

```bash
./bmad-methods [command] [options]

Commands:
  search <keyword>     Search methods by keyword
  category <name>      Filter by category
  mode <mode>         Filter by execution mode
  module <name>       Filter by module/file
  get <method-id>     Get specific method details
  stats               Show library statistics
  help                Show help

Options:
  --limit <n>         Limit results (default: 50)
  --full              Show full method details
```

---

## Advanced Usage

### Export Methods to File

```bash
# Export search results
./bmad-methods search "deploy" > deploy_methods.txt

# Export by category
./bmad-methods category CODE_SOLIDITY --full > solidity_methods.txt
```

### Count Methods by Category

```bash
./bmad-methods category CODE_PYTHON | grep "ID:" | wc -l
```

### Find Methods by Complexity

```bash
# Methods in larger files (likely more complex)
./bmad-methods category STRUCT_PYTHON --full \
  | grep -E "line_number|method_name" | sort -n | tail -20
```

### Pipeline with Other Tools

```bash
# Find methods matching pattern and extract IDs
./bmad-methods search "router" --full | grep "ID:" | awk '{print $2}'

# Convert results to JSON (with jq)
./bmad-methods module "utils.py" \
  | jq -R 'split(":") | {key: .[0], value: .[1]}'
```

---

## Data Formats

### CSV Format

```
method_id,method_name,description,category,file_path,line_number,type,_source_file,execution_modes,execution_mode
MTH-...,FunctionName,Description,CODE_PYTHON,path/file.py,42,FUNCTION,source.csv,"full,batch",full
```

### JSON Format

```json
{
  "generated_at": "2025-12-19T14:40:18",
  "total_methods": 206902,
  "methods": [
    {
      "method_id": "MTH-...",
      "method_name": "FunctionName",
      "description": "What it does",
      "category": "CODE_PYTHON",
      "file_path": "path/file.py",
      "line_number": 42,
      "type": "FUNCTION",
      "_source_file": "source.csv",
      "execution_modes": "full,batch",
      "execution_mode": "full"
    }
  ]
}
```

### Index Format

```json
{
  "by_id": {
    "MTH-ABC123": { /* full method object */ }
  },
  "by_category": {
    "CODE_PYTHON": ["MTH-ABC123", "MTH-DEF456"]
  },
  "by_module": {
    "utils.py": ["MTH-ABC123"]
  },
  "by_mode": {
    "quick": ["MTH-ABC123"]
  }
}
```

---

## Maintenance

### Refresh the Library

When new methods are added to your codebase:

```bash
cd tools
python3 consolidate-methods.py --full
# Regenerates CSV, JSON, and index files
```

### Migrate from Old Systems

If you have methods in scattered files:

1. Ensure all `bmad-methods.csv` files are in discoverable locations
2. Run consolidation: `python3 tools/consolidate-methods.py --full`
3. Start using the unified library: `./bmad-methods search "..."`
4. Retire old CSV files once library is in use

---

## Performance Characteristics

### Query Performance

| Query Type | Time | Index Type |
|-----------|------|-----------|
| By ID | <1ms | by_id |
| By category | <10ms | by_category |
| By module | <10ms | by_module |
| By mode | <10ms | by_mode |
| Keyword search | 50-200ms | Full scan |

### File Sizes

| File | Size | Format | Use |
|------|------|--------|-----|
| consolidated.csv | 49MB | CSV | Direct access, spreadsheets |
| consolidated.json | 97MB | JSON | REST APIs, web apps |
| index.json | 118MB | JSON | Fast programmatic lookups |

---

## FAQ

**Q: Can I modify the library?**
A: Yes, edit `bmad-methods-consolidated.csv` directly. Re-run consolidation to update the index.

**Q: How often is the library updated?**
A: Manually via `consolidate-methods.py`. BMAD will support auto-refresh every 3600 seconds.

**Q: What if I have methods in new files?**
A: Place them in discoverable locations and re-run consolidation.

**Q: Can I export the library?**
A: Yes, use the CSV or JSON files directly. They're standard formats.

**Q: How do I use methods in my workflow?**
A: Query the library with `./bmad-methods search`, then execute with `bmad run <method-id> --mode=<mode>`.

**Q: What's the difference between execution modes?**
A: Timeout, parallelization, and verbosity. Quick = fast + minimal output. Full = comprehensive + detailed. Batch = automated + structured.

---

## Next Steps

1. **Explore the library**: `./bmad-methods stats`
2. **Search for methods**: `./bmad-methods search "<your-keyword>"`
3. **Integrate into workflows**: Add queries to your BMAD tasks
4. **Use programmatically**: Load and parse CSV/JSON in your scripts
5. **Refresh when needed**: `python3 tools/consolidate-methods.py --full`

---

## Documentation

- **Quick Reference**: This README
- **Complete Guide**: `LIBRARY-DISCOVERY.md`
- **Consolidation Script**: `tools/consolidate-methods.py`
- **Query Tool**: `tools/query-methods.py`
- **Library Definition**: `library/bmad-methods-library.yaml`

---

## Summary

✅ **206,902 methods** consolidated into one library
✅ **6 execution modes** for different use cases
✅ **Fast lookups** via intelligent indexing
✅ **Easy discovery** with CLI wrapper
✅ **Full integration** with BMAD ecosystem

**Your methods library is ready to use!**

```bash
./bmad-methods stats
./bmad-methods search "your-keyword"
./bmad-methods help
```

---

**Last Updated**: December 19, 2025
**Status**: Production Ready ✅
**Location**: `/home/ichigo/alexandria/anima-mundi/defense/alexandria-core/_ARCHIVE_CHAOS/BMAD-METHOD/`
