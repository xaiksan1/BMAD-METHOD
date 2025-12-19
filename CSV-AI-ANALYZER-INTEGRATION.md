# CSV AI Analyzer ↔ BMAD-METHOD Integration

**Intelligent architecture visualization as a native BMAD workflow component**

---

## 🎯 What This Integration Does

Adds csv-ai-analyzer as a **first-class BMAD task** that:

1. **Generates** methods catalog via BMAD Dashboard
2. **Enriches** data with complexity & impact metrics
3. **Analyzes** using AI for insights
4. **Visualizes** interactively at http://localhost:3000
5. **Reports** findings back to Notion (optional)

---

## 📦 Files Added

```
BMAD-METHOD/
├── tasks/
│   └── analyze-methods-with-csv-analyzer.yaml    ← New BMAD Task
└── CSV-AI-ANALYZER-INTEGRATION.md               ← This file
```

---

## 🚀 Usage

### Option 1: Run as Standalone Task

```bash
cd /path/to/BMAD-METHOD
bmad run analyze-methods-with-csv-analyzer --mode=full
```

Interactive mode:
- Generates methods → Enriches CSV → Launches analyzer UI

### Option 2: Run in Batch Mode (No UI)

```bash
bmad run analyze-methods-with-csv-analyzer --mode=batch
```

Automated mode:
- Generates → Enriches → AI Analysis → Generates Reports
- No user interaction needed

### Option 3: Integrate into Existing Workflow

Add to your `workflow.yaml`:

```yaml
tasks:
  # ... your other tasks ...

  - id: analyze_methods
    name: Analyze Methods with CSV AI Analyzer
    action: include_task
    task_file: "tasks/analyze-methods-with-csv-analyzer.yaml"
    mode: "full"  # or "batch"
    next_task: your_next_task
```

Then run your workflow normally:
```bash
bmad run your-workflow
```

---

## 📊 What Gets Generated

| File | Purpose | Format |
|------|---------|--------|
| `bmad-methods.csv` | Raw catalog (from Dashboard) | CSV |
| `bmad-methods-enriched.csv` | With metrics | CSV |
| `bmad-analysis-report.json` | Architecture insights | JSON |
| `ai-insights.md` | LLM analysis | Markdown |
| `ANALYSIS_REPORT.html` | Interactive report | HTML |

---

## 🔌 Integration Points

### With BMAD Party Mode

Use csv-ai-analyzer as an **analysis agent**:

```yaml
analyze_party:
  action: agent_orchestration
  inputs:
    mode: party
    participants:
      - claude-3-opus
      - gpt-4-turbo
      - csv-analyzer  # ← New!
    goal: "Analyze methods and discover patterns"
```

### With Pattern Discovery

Analyzer output feeds **pattern discovery engine**:

```
CSV Analysis Results
    ↓
Pattern Discovery
    ↓
Agent Generation
    ↓
Notion Integration
```

### With Notion Integration

Results automatically sync to Notion:

```bash
export NOTION_API_KEY="your-key"
export NOTION_ANALYSIS_DB="database-id"
bmad run analyze-methods-with-csv-analyzer
```

---

## ⚙️ Configuration

### Environment Variables

```bash
# Analyzer
ANALYZER_PORT=3000

# AI Providers (any one)
ANTHROPIC_API_KEY="sk-..."
OPENAI_API_KEY="sk-..."

# Notion (optional)
NOTION_API_KEY="ntn_..."
NOTION_ANALYSIS_DB="database-id"
```

### Task Parameters

```bash
bmad run analyze-methods-with-csv-analyzer \
  --mode=full \
  --port=3001 \
  --ai-provider=claude \
  --skip-analyzer-ui \
  --output-dir=./analysis-results
```

---

## 🔄 Workflow Example

Complete BMAD workflow with CSV analysis:

```yaml
workflow:
  name: "BMAD with Architecture Analysis"

  tasks:
    # 1. Discover patterns with Party Mode
    - id: bmad_party
      action: party_mode
      next_task: analyze_methods

    # 2. Analyze discovered methods
    - id: analyze_methods
      action: include_task
      task_file: "tasks/analyze-methods-with-csv-analyzer.yaml"
      mode: batch
      next_task: generate_implementation

    # 3. Generate implementation based on insights
    - id: generate_implementation
      action: code_generation
      inputs:
        analysis_results: "{{ analyze_methods.outputs }}"
```

---

## 📈 Features

### Automatic Analysis

✅ **Complexity Scoring**
- Low/Medium/High assessment
- Identifies hotspots
- Recommends refactoring

✅ **Impact Assessment**
- Critical/High/Medium/Low ranking
- Dependency analysis
- Risk assessment

✅ **Architecture Insights**
- Pattern discovery
- Anti-pattern detection
- Best practices validation

### AI-Powered

✅ **LLM Analysis**
- Claude, OpenAI, Google Gemini, Mistral
- Local models (Ollama, LM Studio)
- Custom endpoints

✅ **Intelligent Recommendations**
- Refactoring priorities
- Optimization opportunities
- Documentation improvements

### Interactive Visualization

✅ **Web UI**
- Upload CSV
- Configure AI provider
- Run analysis
- Export charts & reports

---

## 🎓 Examples

### Example 1: Analyze Your BMAD System

```bash
cd /path/to/BMAD-METHOD
bmad run analyze-methods-with-csv-analyzer --mode=full
```

Result: Interactive analyzer at http://localhost:3000

### Example 2: Batch Analysis for CI/CD

```bash
# In your CI/CD pipeline
bmad run analyze-methods-with-csv-analyzer --mode=batch

# Results available in:
# - bmad-methods-enriched.csv
# - bmad-analysis-report.json
# - ai-insights.md
# - ANALYSIS_REPORT.html
```

### Example 3: Track Evolution Over Time

```bash
# Run monthly analysis
bmad run analyze-methods-with-csv-analyzer --mode=batch

# Results automatically pushed to Notion
# Create dashboard showing trends:
# - Method count growth
# - Complexity evolution
# - Documentation coverage
```

### Example 4: Party Mode Analysis

```yaml
# In workflow.yaml
- id: deep_analysis
  action: party_mode
  inputs:
    participants:
      - claude (Architecture Specialist)
      - gpt-4 (Implementation Specialist)
      - csv-analyzer (Architecture Analyzer)
    task: "Analyze methods and propose improvements"
```

---

## 🔍 Output Examples

### bmad-analysis-report.json

```json
{
  "total_methods": 247,
  "categories": {
    "STRUCT_PYTHON": 78,
    "CODE_PYTHON": 89,
    "CODE_SHELL": 67
  },
  "complexity_distribution": {
    "Low": 89,
    "Medium": 112,
    "High": 46
  },
  "impact_distribution": {
    "Critical": 23,
    "High": 67,
    "Medium": 109,
    "Low": 48
  },
  "insights": [
    "Most code: CLASS structures (78 methods)",
    "Critical functions: init, setup, run, deploy",
    "Documentation gaps: 12 methods need descriptions"
  ]
}
```

### ai-insights.md

```markdown
# Architecture Analysis

## Summary
The BMAD-METHOD system is well-structured with clear separation of concerns.

## Key Findings
- 247 methods across 3 primary categories
- 12 critical system functions identified
- 45% of code has high complexity (refactoring candidates)

## Recommendations
1. Add documentation to 12 undocumented critical functions
2. Refactor 5 high-complexity methods
3. Consolidate 8 utility functions into shared library

## Next Steps
- [ ] Document critical functions
- [ ] Refactor high-complexity methods
- [ ] Create utility library
```

---

## 🛠️ Troubleshooting

### "Task not found"

The task needs to be registered in BMAD:

```bash
bmad task register tasks/analyze-methods-with-csv-analyzer.yaml
```

### "Port 3000 already in use"

```bash
bmad run analyze-methods-with-csv-analyzer --port=3001
```

### "No AI provider configured"

Batch mode will skip AI analysis. To enable:

```bash
export ANTHROPIC_API_KEY="sk-..."
bmad run analyze-methods-with-csv-analyzer --mode=batch
```

### "CSV won't upload to analyzer"

Verify:
- File is UTF-8 encoded
- First row contains headers
- Delimiter is comma

Or use enriched version directly (includes all fixes).

---

## 📚 Integration with Alexandria Ecosystem

This integrates into the larger Alexandria system:

```
BMAD-METHOD (Workflow Engine)
    ↓
CSV-AI-ANALYZER (This Integration)
    ↓
Product-Spawner (Uses insights to generate variants)
    ↓
Filmmaker (Creates 3D assets based on analysis)
    ↓
JSON-MCP-Blower (Deploys as AI agents)
```

---

## 🚀 Next Steps

1. **Setup** (one-time):
   ```bash
   bmad task register tasks/analyze-methods-with-csv-analyzer.yaml
   export ANTHROPIC_API_KEY="your-key"
   ```

2. **Test**:
   ```bash
   bmad run analyze-methods-with-csv-analyzer --mode=quick
   ```

3. **Integrate** into your workflows by adding the task

4. **Monitor** results via Notion dashboard (optional)

---

## 📞 Support

For issues or questions:
- Check `tasks/analyze-methods-with-csv-analyzer.yaml` for full spec
- Review `/path/to/csv-ai-analyzer/README.md` for UI features
- Refer to BMAD-METHOD docs for workflow integration

---

**This integration makes csv-ai-analyzer a native BMAD component** ✨

Instead of being a standalone tool, it's now part of the BMAD workflow ecosystem,
with full support for automation, party mode analysis, and Notion integration.
