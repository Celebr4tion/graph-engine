"""
Analyzer package for parsing and analyzing code files.
"""

import os
import logging
from typing import Optional, Union

from graph_core.analyzer.python_parser import PythonParser
from graph_core.analyzer.treesitter_parser import TreeSitterParser

__all__ = ['TreeSitterParser', 'PythonParser', 'get_parser_for_file']

logger = logging.getLogger(__name__)


def get_parser_for_file(file_path: str) -> Optional[Union[TreeSitterParser, PythonParser]]:
    """
    Get the appropriate parser for a given file based on its extension.
    
    Args:
        file_path: Path to the file to be parsed
        
    Returns:
        A parser instance appropriate for the file type, or None if no suitable parser is available
        
    Examples:
        >>> parser = get_parser_for_file('example.py')
        >>> isinstance(parser, TreeSitterParser) or isinstance(parser, PythonParser)
        True
        >>> parser = get_parser_for_file('example.js')
        >>> isinstance(parser, TreeSitterParser)
        True
        >>> get_parser_for_file('example.txt') is None
        True
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    # Map file extensions to languages supported by TreeSitterParser
    extensions_to_language = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript', 
        '.tsx': 'typescript'
    }
    
    if ext in extensions_to_language:
        try:
            # Try to use TreeSitterParser first
            return TreeSitterParser(extensions_to_language[ext])
        except Exception as e:
            logger.warning(f"Failed to create TreeSitterParser for {file_path}: {str(e)}")
            
            # Fall back to PythonParser for Python files
            if ext == '.py':
                logger.info(f"Falling back to PythonParser for {file_path}")
                return PythonParser()
            
            logger.error(f"No fallback parser available for {ext} files")
            return None
    
    # Return None for unsupported file types
    return None 