"""MarkItDown - Convert various file formats to Markdown.

A fork of microsoft/markitdown with additional features and improvements.

Original project: https://github.com/microsoft/markitdown
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__version__ = "0.1.0"
__author__ = "microsoft/markitdown contributors"
__all__ = ["MarkItDown", "DocumentConverter", "ConversionResult"]
