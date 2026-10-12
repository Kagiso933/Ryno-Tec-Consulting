"""
Invoice & Quote Generator Module for Ryno-Tec Consulting

This module provides professional invoice, quote, and bid costing functionality
integrated with Ryno-Tec Consulting's service offerings.

Features:
- Professional quote generation with Ryno-Tec service templates
- Invoice management with automatic VAT calculation
- Bid costing analysis with contingency and margin calculations
- SA compliance (VAT, B-BBEE, POPIA, CIPC)
- PDF export with branded letterhead
- Template management and reuse

Usage:
    from modules.invoice_quote_generator import QuoteGenerator, InvoiceGenerator, BidCostingGenerator

    # Create a quote
    quote = QuoteGenerator(client_name="Enterprise Client")
    quote.add_service_line_item("Platform Engineering", "IaC Implementation", 1, 1500000)
    quote.generate_pdf("quote.pdf")
"""

from .generator import (
    DocumentType,
    ServiceLine,
    BBBEELevel,
    CompanyInfo,
    ClientInfo,
    LineItem,
    Quote,
    Invoice,
    BidCostItem,
    BidCosting,
    DocumentGenerator,
    QuoteGenerator,
    InvoiceGenerator,
    BidCostingGenerator,
)

__version__ = "1.0.0"
__author__ = "Ryno-Tec Consulting"
__all__ = [
    "DocumentType",
    "ServiceLine",
    "BBBEELevel",
    "CompanyInfo",
    "ClientInfo",
    "LineItem",
    "Quote",
    "Invoice",
    "BidCostItem",
    "BidCosting",
    "DocumentGenerator",
    "QuoteGenerator",
    "InvoiceGenerator",
    "BidCostingGenerator",
]
