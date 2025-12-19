#!/usr/bin/env python3

"""
BMAD METHODS CONSOLIDATOR

Consolidates all bmad-methods.csv files from across the codebase
into a single centralized library with integrated modes.

Usage:
  python3 consolidate-methods.py --scan
  python3 consolidate-methods.py --consolidate
  python3 consolidate-methods.py --report
"""

import os
import sys
import json
import csv
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Set
import argparse
from datetime import datetime

class MethodsConsolidator:
    def __init__(self, root_path: str = "/home/ichigo/alexandria"):
        self.root = Path(root_path)
        self.method_files: List[Path] = []
        self.methods_data: Dict = defaultdict(list)
        self.library_path = Path("/home/ichigo/alexandria/anima-mundi/defense/alexandria-core/_ARCHIVE_CHAOS/BMAD-METHOD/library")
        self.consolidated_csv = self.library_path / "bmad-methods-consolidated.csv"
        self.consolidated_json = self.library_path / "bmad-methods-consolidated.json"

    def scan_for_methods(self):
        """Scan entire codebase for bmad-methods.csv files"""
        print("\n" + "="*70)
        print("SCANNING FOR bmad-methods.csv FILES")
        print("="*70 + "\n")

        for root, dirs, files in os.walk(self.root):
            # Skip certain directories
            dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '.next', '__pycache__', '.venv']]

            for file in files:
                if file == "bmad-methods.csv":
                    file_path = Path(root) / file
                    self.method_files.append(file_path)
                    print(f"  ✓ Found: {file_path.relative_to(self.root)}")

        print(f"\n✓ Total files found: {len(self.method_files)}\n")
        return self.method_files

    def load_and_consolidate(self):
        """Load all CSV files and consolidate into single library"""
        print("\n" + "="*70)
        print("CONSOLIDATING METHODS")
        print("="*70 + "\n")

        all_methods = []
        method_ids_seen = set()

        for csv_file in self.method_files:
            try:
                print(f"  Loading: {csv_file.relative_to(self.root)}")

                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        method_id = row.get('method_id', '')

                        # Avoid duplicates
                        if method_id not in method_ids_seen:
                            # Add source file info
                            row['_source_file'] = str(csv_file.relative_to(self.root))

                            # Add modes if not present
                            if 'execution_modes' not in row:
                                row['execution_modes'] = self._get_default_modes(row)

                            # Add execution_mode column if missing
                            if 'execution_mode' not in row:
                                row['execution_mode'] = 'full'

                            all_methods.append(row)
                            method_ids_seen.add(method_id)

            except Exception as e:
                print(f"    ❌ Error reading {csv_file}: {str(e)}")
                continue

        print(f"\n✓ Consolidated {len(all_methods)} unique methods\n")
        self.methods_data = all_methods
        return all_methods

    def _get_default_modes(self, method: Dict) -> str:
        """Determine default modes for a method based on its type"""
        category = method.get('category', '').lower()

        if 'analysis' in category:
            return "quick,full,batch,party,interactive,debug"
        elif 'generation' in category:
            return "full,batch,party"
        elif 'utility' in category or 'helper' in category:
            return "quick,batch"
        else:
            return "full,batch"

    def save_consolidated(self):
        """Save consolidated methods to CSV and JSON"""
        print("\n" + "="*70)
        print("SAVING CONSOLIDATED LIBRARY")
        print("="*70 + "\n")

        # Ensure library directory exists
        self.library_path.mkdir(parents=True, exist_ok=True)

        # Save as CSV
        if self.methods_data:
            fieldnames = list(self.methods_data[0].keys())

            with open(self.consolidated_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.methods_data)

            print(f"  ✓ CSV saved: {self.consolidated_csv.relative_to(self.root)}")
            print(f"    Total methods: {len(self.methods_data)}")

        # Save as JSON
        json_data = {
            "metadata": {
                "consolidation_date": datetime.now().isoformat(),
                "total_methods": len(self.methods_data),
                "source_files": len(self.method_files)
            },
            "methods": self.methods_data
        }

        with open(self.consolidated_json, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)

        print(f"  ✓ JSON saved: {self.consolidated_json.relative_to(self.root)}")

    def generate_report(self):
        """Generate consolidation report"""
        print("\n" + "="*70)
        print("CONSOLIDATION REPORT")
        print("="*70 + "\n")

        print(f"Source Files: {len(self.method_files)}")
        print(f"Total Methods: {len(self.methods_data)}")

        # Category breakdown
        categories = defaultdict(int)
        modes = defaultdict(int)

        for method in self.methods_data:
            category = method.get('category', 'unknown')
            categories[category] += 1

            mode_str = method.get('execution_modes', 'full')
            for mode in mode_str.split(','):
                modes[mode.strip()] += 1

        print(f"\nCategories ({len(categories)}):")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {cat}: {count}")

        print(f"\nExecution Modes Used:")
        for mode, count in sorted(modes.items(), key=lambda x: x[1], reverse=True):
            print(f"  • {mode}: {count} methods")

        print(f"\nLibrary Locations:")
        print(f"  CSV: {self.consolidated_csv}")
        print(f"  JSON: {self.consolidated_json}")
        print(f"  YAML: {self.library_path / 'bmad-methods-library.yaml'}")

        return {
            "source_files": len(self.method_files),
            "total_methods": len(self.methods_data),
            "categories": dict(categories),
            "modes": dict(modes)
        }

    def create_index(self):
        """Create searchable index for quick lookup"""
        print("\n" + "="*70)
        print("CREATING INDEX")
        print("="*70 + "\n")

        index = {
            "by_id": {},
            "by_category": defaultdict(list),
            "by_module": defaultdict(list),
            "by_mode": defaultdict(list)
        }

        for method in self.methods_data:
            mid = method.get('method_id', '')
            category = method.get('category', '')
            module = method.get('file_path', '').split('/')[0] if method.get('file_path') else 'unknown'
            modes = method.get('execution_modes', '').split(',')

            if mid:
                index["by_id"][mid] = method

            if category:
                index["by_category"][category].append(mid)

            if module:
                index["by_module"][module].append(mid)

            for mode in modes:
                mode = mode.strip()
                if mode:
                    index["by_mode"][mode].append(mid)

        # Save index
        index_path = self.library_path / "bmad-methods-index.json"
        with open(index_path, 'w', encoding='utf-8') as f:
            # Convert defaultdict to regular dict for JSON serialization
            json.dump({
                "by_id": index["by_id"],
                "by_category": dict(index["by_category"]),
                "by_module": dict(index["by_module"]),
                "by_mode": dict(index["by_mode"])
            }, f, indent=2)

        print(f"  ✓ Index created: {index_path}")
        print(f"    Methods indexed by ID: {len(index['by_id'])}")
        print(f"    Categories: {len(index['by_category'])}")
        print(f"    Modules: {len(index['by_module'])}")
        print(f"    Modes: {len(index['by_mode'])}\n")

        return index

    def run_full_consolidation(self):
        """Run complete consolidation pipeline"""
        print("\n" + "╔" + "="*68 + "╗")
        print("║" + " "*20 + "BMAD METHODS CONSOLIDATOR" + " "*23 + "║")
        print("╚" + "="*68 + "╝")

        self.scan_for_methods()
        self.load_and_consolidate()
        self.save_consolidated()
        self.create_index()
        report = self.generate_report()

        print("\n" + "="*70)
        print("✅ CONSOLIDATION COMPLETE")
        print("="*70 + "\n")

        print("Next steps:")
        print("  1. Review consolidated library:")
        print(f"     cat {self.consolidated_csv.relative_to(self.root)}")
        print("  2. Search methods:")
        print("     bmad find-methods '<keyword>'")
        print("  3. Run a method:")
        print("     bmad run <method-name> --mode=<mode>")
        print()

        return report

def main():
    parser = argparse.ArgumentParser(description="Consolidate BMAD methods library")
    parser.add_argument("--scan", action="store_true", help="Scan for method files")
    parser.add_argument("--consolidate", action="store_true", help="Consolidate all methods")
    parser.add_argument("--report", action="store_true", help="Generate report only")
    parser.add_argument("--full", action="store_true", help="Run complete consolidation")
    parser.add_argument("--root", default="/home/ichigo/alexandria", help="Root directory to scan")

    args = parser.parse_args()

    consolidator = MethodsConsolidator(args.root)

    if args.scan:
        consolidator.scan_for_methods()
    elif args.report:
        consolidator.scan_for_methods()
        consolidator.load_and_consolidate()
        consolidator.generate_report()
    elif args.full or (not args.scan and not args.report):
        consolidator.run_full_consolidation()

if __name__ == '__main__':
    main()
