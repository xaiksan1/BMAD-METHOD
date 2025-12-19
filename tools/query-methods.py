#!/usr/bin/env python3

"""
BMAD METHODS QUERY TOOL

Fast query interface for the consolidated methods library.
Supports searching by keyword, category, module, or execution mode.

Usage:
  python3 query-methods.py --search "analysis"
  python3 query-methods.py --category "CODE_PYTHON"
  python3 query-methods.py --mode "quick"
  python3 query-methods.py --method-id "MTH-ABC123"
  python3 query-methods.py --stats
"""

import json
import csv
import sys
from pathlib import Path
from typing import List, Dict
import argparse
from collections import defaultdict

class MethodsQuery:
    def __init__(self, library_path: str = "/home/ichigo/alexandria/anima-mundi/defense/alexandria-core/_ARCHIVE_CHAOS/BMAD-METHOD/library"):
        self.library_path = Path(library_path)
        self.index_file = self.library_path / "bmad-methods-index.json"
        self.csv_file = self.library_path / "bmad-methods-consolidated.csv"
        self.index = None
        self.csv_methods = None
        self._load_index()

    def _load_index(self):
        """Load the methods index for fast lookups"""
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                self.index = json.load(f)
        except FileNotFoundError:
            print(f"Error: Index file not found at {self.index_file}")
            sys.exit(1)

    def search_by_keyword(self, keyword: str, limit: int = 50) -> List[Dict]:
        """Search methods by keyword in name and description"""
        keyword_lower = keyword.lower()
        results = []

        # Search in index (by_id contains full method objects)
        for method_id, method in self.index.get("by_id", {}).items():
            if keyword_lower in method.get("method_name", "").lower() or \
               keyword_lower in method.get("description", "").lower():
                results.append(method)
                if len(results) >= limit:
                    break

        return results

    def search_by_category(self, category: str, limit: int = 50) -> List[Dict]:
        """Search methods by category"""
        method_ids = self.index.get("by_category", {}).get(category, [])[:limit]
        by_id = self.index.get("by_id", {})
        return [by_id[mid] for mid in method_ids if mid in by_id]

    def search_by_mode(self, mode: str, limit: int = 50) -> List[Dict]:
        """Search methods by execution mode"""
        method_ids = self.index.get("by_mode", {}).get(mode, [])[:limit]
        by_id = self.index.get("by_id", {})
        return [by_id[mid] for mid in method_ids if mid in by_id]

    def search_by_module(self, module: str, limit: int = 50) -> List[Dict]:
        """Search methods by module"""
        method_ids = self.index.get("by_module", {}).get(module, [])[:limit]
        by_id = self.index.get("by_id", {})
        return [by_id[mid] for mid in method_ids if mid in by_id]

    def get_method_by_id(self, method_id: str) -> Dict:
        """Get method by exact ID"""
        return self.index.get("by_id", {}).get(method_id)

    def get_stats(self) -> Dict:
        """Get library statistics"""
        return {
            "total_methods": len(self.index.get("by_id", {})),
            "total_categories": len(self.index.get("by_category", {})),
            "total_modules": len(self.index.get("by_module", {})),
            "total_modes": len(self.index.get("by_mode", {})),
            "categories": {cat: len(ids) for cat, ids in self.index.get("by_category", {}).items()},
            "modes": {mode: len(ids) for mode, ids in self.index.get("by_mode", {}).items()},
            "modules": {mod: len(ids) for mod, ids in self.index.get("by_module", {}).items()}
        }

    def print_results(self, methods: List[Dict], show_full: bool = False):
        """Pretty print search results"""
        if not methods:
            print("No methods found.")
            return

        print(f"\n{'='*80}")
        print(f"Found {len(methods)} method(s)")
        print(f"{'='*80}\n")

        for method in methods:
            print(f"ID: {method.get('method_id', 'N/A')}")
            print(f"Name: {method.get('method_name', 'N/A')}")
            print(f"Category: {method.get('category', 'N/A')}")
            print(f"Module: {method.get('file_path', 'N/A').split('/')[0] if method.get('file_path') else 'N/A'}")
            print(f"Modes: {method.get('execution_modes', 'N/A')}")

            if show_full:
                print(f"Description: {method.get('description', 'N/A')}")
                print(f"Source: {method.get('_source_file', 'N/A')}")
                print(f"Line: {method.get('line_number', 'N/A')}")

            print()

def main():
    parser = argparse.ArgumentParser(description="Query BMAD consolidated methods library")
    parser.add_argument("--search", help="Search by keyword")
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--mode", help="Filter by execution mode")
    parser.add_argument("--module", help="Filter by module")
    parser.add_argument("--method-id", help="Get specific method by ID")
    parser.add_argument("--stats", action="store_true", help="Show library statistics")
    parser.add_argument("--limit", type=int, default=50, help="Limit results (default: 50)")
    parser.add_argument("--full", action="store_true", help="Show full method details")

    args = parser.parse_args()

    query = MethodsQuery()

    if args.stats:
        stats = query.get_stats()
        print("\n" + "="*70)
        print("BMAD METHODS LIBRARY STATISTICS")
        print("="*70 + "\n")
        print(f"Total Methods: {stats['total_methods']:,}")
        print(f"Categories: {stats['total_categories']}")
        print(f"Modules: {stats['total_modules']}")
        print(f"Execution Modes: {stats['total_modes']}")

        print(f"\nTop Categories:")
        for cat, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {cat}: {count:,} methods")

        print(f"\nExecution Modes:")
        for mode, count in sorted(stats['modes'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {mode}: {count:,} methods")

        print(f"\nTop Modules:")
        for mod, count in sorted(stats['modules'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {mod}: {count:,} methods")
        print()

    elif args.method_id:
        method = query.get_method_by_id(args.method_id)
        if method:
            query.print_results([method], show_full=True)
        else:
            print(f"Method not found: {args.method_id}")

    elif args.search:
        results = query.search_by_keyword(args.search, limit=args.limit)
        query.print_results(results, show_full=args.full)

    elif args.category:
        results = query.search_by_category(args.category, limit=args.limit)
        query.print_results(results, show_full=args.full)

    elif args.mode:
        results = query.search_by_mode(args.mode, limit=args.limit)
        query.print_results(results, show_full=args.full)

    elif args.module:
        results = query.search_by_module(args.module, limit=args.limit)
        query.print_results(results, show_full=args.full)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
