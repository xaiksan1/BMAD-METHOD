# BMAD-METHOD - Breakthrough Method of Agile AI Development

**Version**: 6.0.0-alpha.8  
**Status**: 🟢 Production Ready  
**Tech Stack**: Node.js, JavaScript, ESLint, Prettier, Jest, Husky  
**Distribution**: NPM package (`bmad-method`)  

## Quick Summary

BMAD is the **universal human-AI collaboration framework**. It:
- Enables breakthrough development with AI assistance
- Provides CLI tool for scaffolding projects
- Enforces code quality via pre-commit hooks
- Defines AI methodology for agile workflows
- Includes automated testing and validation

## Architecture

```
BMAD-METHOD/
├── src/                    # Core methodology
│   ├── ai-collaboration/   # AI integration patterns
│   ├── agile-workflows/    # Agile ceremony definitions
│   ├── validation/         # Schema validation
│   └── cli/                # CLI commands
├── test/                   # Jest test suite
├── tools/                  # Build tools
│   ├── cli/                # CLI implementation
│   ├── validate-bundles.js # Bundle validation
│   └── generate-docs.js    # Doc generation
├── docs/                   # Framework documentation
├── package.json
├── .eslintrc              # ESLint config
├── .prettierrc             # Code formatting
├── .pre-commit-config.yaml # Git hooks
└── jest.config.js          # Test config
```

## Installation & Usage

```bash
# Install (stable)
npm install -g bmad-method
# OR
npx bmad-method install

# Install (alpha)
npx bmad-method@alpha install

# Create new project
bmad init my-project
bmad scaffold --template=defense

# Run tests
npm test

# Validate bundle
npm run validate

# Run all checks
npm run check
```

## Pre-Commit Hooks

Configured via `.pre-commit-config.yaml` and Husky:
```
On git commit:
  1. ESLint (code quality)
  2. Prettier (formatting)
  3. Jest (tests)
  4. Ruff (Python, if applicable)
  5. Custom validation scripts
```

## CLI Commands

```bash
# Project scaffolding
bmad scaffold --template=<type>
  Templates: defense, web, api, ml, blockchain

# Validate BMAD compliance
bmad validate --strict
bmad validate --bundle=production

# Generate documentation
bmad docs --format=markdown
bmad docs --format=openapi

# AI collaboration setup
bmad ai-setup --llm=claude
bmad ai-setup --llm=openai
```

## Methodology Principles

```
Breakthrough Development (B)
  → Human-AI collaboration from day 1
  → Iterate with AI feedback loop

Method (M)
  → Structured approach to problem-solving
  → Clear problem → Solution → Validation

Agile (A)
  → Sprint-based workflow
  → Continuous integration/deployment

AI-Driven (D)
  → Leverage AI for code generation
  → AI-assisted testing
  → Automated documentation
```

## Quality Gates

```javascript
// jest.config.js enforces:
{
  collectCoverageFrom: ["src/**/*.js"],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
}
```

## Integration with Alexandria

```
BMAD enhances Alexandria services:
  ✓ All services follow BMAD scaffolding
  ✓ Pre-commit hooks enforce quality
  ✓ Jest tests for each module
  ✓ CI/CD pipeline integration
  ✓ AI-assisted code review
```

## Common Commands

```bash
# Run tests
npm test

# Run tests with coverage
npm test -- --coverage

# Lint code
npm run lint

# Format code
npm run format

# Run all checks
npm run check

# Build documentation
npm run docs

# Publish package
npm publish
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Pre-commit failing | Run: `npx husky install` then `npm run check` |
| Tests not found | Check test files: `src/**/*.test.js` |
| ESLint error | Run: `npm run lint -- --fix` |
| Coverage too low | Increase test coverage in jest.config.js |

---
**Full context**: See `/home/ichigo/alexandria/anima-mundi/defense/alexandria-core/CLAUDE.md`
