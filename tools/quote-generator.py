#!/usr/bin/env python3
"""
Ryno-Tec Quote Generator CLI

Standalone tool to generate professional, SA-compliant quotes for tenders.
Works offline—no Claude subscription required.

Usage:
    python quote-generator.py --client "Client Name" --tender "TENDER-123" \\
        --service "Platform Engineering" --amount 1500000 --output quotes/

    # Interactive mode:
    python quote-generator.py --interactive
"""

import sys
import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Add modules to path so we can import the invoice generator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.invoice_quote_generator import (
    QuoteGenerator,
    CompanyInfo,
    ClientInfo,
    ServiceLine,
)


# ============================================================================
# COMPANY INFO (Ryno-Tec Consulting)
# ============================================================================

COMPANY_INFO = CompanyInfo(
    name="Ryno-Tec Consulting (Pty) Ltd",
    registration_number="TBD",  # Update when CIPC registration complete
    tax_reference="TBD",
    vat_registration="TBD",
    address="Johannesburg, South Africa",
    email="kagiso@ryno-tec.co.za",
    phone="+27 (XXX) XXX XXXX",
    website="ryno-tec.co.za",
    bbbee_level=1,
    bbbee_scorecard="Generic",
    professional_indemnity_cover=5000000.0,
)

# Service line mapping
SERVICE_LINES = {
    "platform": "Platform Engineering",
    "azure": "Azure Modern Workplace Management",
    "ai": "AI Infrastructure & MLOps",
}


# ============================================================================
# QUOTE GENERATION
# ============================================================================

def create_quote(
    client_name: str,
    client_email: str,
    service: str,
    amount: float,
    quantity: int = 1,
    tender_ref: str = None,
    due_date_days: int = 30,
    notes: str = None,
) -> tuple:
    """
    Create a professional quote.

    Returns: (quote_object, output_filename)
    """

    # Validate service
    if service.lower() not in SERVICE_LINES:
        raise ValueError(
            f"Unknown service: {service}\n"
            f"Available: {', '.join(SERVICE_LINES.keys())}"
        )

    service_name = SERVICE_LINES[service.lower()]

    # Create client
    client = ClientInfo(
        name=client_name,
        email=client_email,
        reference=tender_ref,
    )

    # Create quote
    quote = QuoteGenerator(
        client_name=client.name,
        client_email=client.email,
        quote_date=datetime.now().strftime("%Y-%m-%d"),
    )

    # Set client reference if tender provided
    if tender_ref:
        quote.client_reference = tender_ref

    # Add service line item
    quote.add_service_line_item(
        service=service_name,
        description=f"{service_name} - {tender_ref if tender_ref else 'Consulting Services'}",
        quantity=quantity,
        unit_price=amount,
        unit="project"
    )

    # Set due date
    quote.due_date = (datetime.now() + timedelta(days=due_date_days)).strftime("%Y-%m-%d")

    # Add notes if provided
    if notes:
        quote.notes = notes

    # Generate filename
    date_str = datetime.now().strftime("%Y%m%d")
    client_slug = client_name.replace(" ", "").replace(".", "")
    tender_slug = tender_ref.replace("/", "").replace(" ", "") if tender_ref else "Quote"

    output_filename = f"Quote_{client_slug}_{tender_slug}_{date_str}.pdf"

    return quote, output_filename


def generate_pdf(quote, output_path: str) -> str:
    """Generate PDF and return full path."""
    os.makedirs(output_path, exist_ok=True)

    # Generate PDF using the module's method
    output_file = os.path.join(output_path, quote.output_filename)
    quote.generate_pdf(output_file)

    return output_file


def interactive_mode():
    """Interactive quote generation."""
    print("\n" + "="*70)
    print("RYNO-TEC QUOTE GENERATOR - Interactive Mode")
    print("="*70 + "\n")

    # Get client details
    print("CLIENT DETAILS")
    print("-" * 70)
    client_name = input("Client Name: ").strip()
    if not client_name:
        print("Error: Client name required")
        return

    client_email = input("Client Email: ").strip()
    if not client_email:
        print("Error: Client email required")
        return

    tender_ref = input("Tender Reference (optional): ").strip() or None

    # Get service details
    print("\nSERVICE DETAILS")
    print("-" * 70)
    print("Available services:")
    for key, name in SERVICE_LINES.items():
        print(f"  {key}: {name}")

    service = input("Service (platform/azure/ai): ").strip()
    if service.lower() not in SERVICE_LINES:
        print(f"Error: Unknown service '{service}'")
        return

    # Get pricing
    print("\nPRICING")
    print("-" * 70)
    try:
        amount = float(input("Amount (ZAR): "))
    except ValueError:
        print("Error: Invalid amount")
        return

    quantity = 1
    qty_input = input("Quantity (default 1): ").strip()
    if qty_input:
        try:
            quantity = int(qty_input)
        except ValueError:
            print("Warning: Invalid quantity, using 1")

    due_date_days = 30
    due_input = input("Due date (days from today, default 30): ").strip()
    if due_input:
        try:
            due_date_days = int(due_input)
        except ValueError:
            print("Warning: Invalid days, using 30")

    notes = input("Additional notes (optional): ").strip() or None

    # Output path
    output_path = input("Output directory (default 'quotes'): ").strip() or "quotes"

    # Generate
    print("\nGENERATING QUOTE...")
    print("-" * 70)

    try:
        quote, filename = create_quote(
            client_name=client_name,
            client_email=client_email,
            service=service,
            amount=amount,
            quantity=quantity,
            tender_ref=tender_ref,
            due_date_days=due_date_days,
            notes=notes,
        )

        output_file = os.path.join(output_path, filename)
        os.makedirs(output_path, exist_ok=True)
        quote.generate_pdf(output_file)

        print(f"✓ Quote generated successfully!")
        print(f"✓ Saved to: {os.path.abspath(output_file)}")
        print(f"\nQuote Details:")
        print(f"  Client: {client_name}")
        print(f"  Amount: ZAR {amount:,.2f}")
        print(f"  Service: {SERVICE_LINES[service.lower()]}")
        if tender_ref:
            print(f"  Tender: {tender_ref}")
        print()

    except Exception as e:
        print(f"✗ Error generating quote: {e}")
        return False

    return True


def cli_mode(args):
    """Command-line argument mode."""
    print("\n" + "="*70)
    print("RYNO-TEC QUOTE GENERATOR")
    print("="*70 + "\n")

    # Validate required arguments
    if not all([args.client, args.service, args.amount]):
        print("Error: --client, --service, and --amount are required")
        print("Use --help for usage information")
        return False

    try:
        quote, filename = create_quote(
            client_name=args.client,
            client_email=args.email,
            service=args.service,
            amount=args.amount,
            quantity=args.quantity,
            tender_ref=args.tender,
            due_date_days=args.due_days,
            notes=args.notes,
        )

        output_path = args.output
        os.makedirs(output_path, exist_ok=True)
        output_file = os.path.join(output_path, filename)
        quote.generate_pdf(output_file)

        print(f"✓ Quote generated successfully!")
        print(f"✓ Saved to: {os.path.abspath(output_file)}")
        print(f"\nQuote Summary:")
        print(f"  Client: {args.client}")
        print(f"  Amount: ZAR {args.amount:,.2f}")
        print(f"  Service: {SERVICE_LINES[args.service.lower()]}")
        if args.tender:
            print(f"  Tender: {args.tender}")
        print()

        return True

    except Exception as e:
        print(f"✗ Error generating quote: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate professional, SA-compliant quotes for Ryno-Tec Consulting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python quote-generator.py --interactive

  # Command-line mode
  python quote-generator.py \\
    --client "Department of Finance" \\
    --service platform \\
    --amount 1500000 \\
    --tender "RFQ-2026-001" \\
    --output quotes/

Services:
  platform  - Platform Engineering & DevOps
  azure     - Azure Modern Workplace Management
  ai        - AI Infrastructure & MLOps
        """
    )

    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Interactive mode (prompts for all details)"
    )

    # Command-line arguments
    parser.add_argument(
        "--client", "-c",
        help="Client name"
    )
    parser.add_argument(
        "--email", "-e",
        default="procurement@client.co.za",
        help="Client email (default: procurement@client.co.za)"
    )
    parser.add_argument(
        "--service", "-s",
        help="Service line: platform, azure, or ai"
    )
    parser.add_argument(
        "--amount", "-a",
        type=float,
        help="Quote amount (ZAR)"
    )
    parser.add_argument(
        "--quantity", "-q",
        type=int,
        default=1,
        help="Quantity (default: 1)"
    )
    parser.add_argument(
        "--tender", "-t",
        help="Tender reference number"
    )
    parser.add_argument(
        "--due-days", "-d",
        type=int,
        default=30,
        help="Days until due date (default: 30)"
    )
    parser.add_argument(
        "--notes", "-n",
        help="Additional notes for the quote"
    )
    parser.add_argument(
        "--output", "-o",
        default="quotes",
        help="Output directory (default: quotes)"
    )

    args = parser.parse_args()

    # Determine mode
    if args.interactive:
        success = interactive_mode()
    else:
        success = cli_mode(args)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
