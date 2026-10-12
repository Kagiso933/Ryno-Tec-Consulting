"""
eTender Pro: Invoice & Quote Generator Module
SA-compliant invoice, quote, and bid costing tool for Ryno-Tec Consulting

Author: Kagiso Tshukudu
Version: 1.0.0
Created: 2026-10-12
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime, timedelta
from enum import Enum
import json
from abc import ABC, abstractmethod


# ============================================================================
# ENUMS & CONSTANTS
# ============================================================================

class DocumentType(Enum):
    """Types of documents that can be generated"""
    QUOTE = "quote"
    INVOICE = "invoice"
    BID_COSTING = "bid_costing"


class ServiceLine(Enum):
    """Ryno-Tec service lines"""
    PLATFORM_ENGINEERING = "Platform Engineering"
    AZURE_MODERN_WORKPLACE = "Azure Modern Workplace Management"
    AI_INFRASTRUCTURE = "AI Infrastructure & MLOps"


class BBBEELevel(Enum):
    """B-BBEE Classification Levels"""
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6
    LEVEL_7 = 7
    LEVEL_8 = 8


# South Africa constants
VAT_RATE = 0.15
CURRENCY = "ZAR"


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class CompanyInfo:
    """Company details for Ryno-Tec Consulting"""
    name: str = "Ryno-Tec Consulting (Pty) Ltd"
    registration_number: str = ""
    tax_reference: str = ""
    vat_registration: str = ""
    address: str = "Johannesburg, South Africa"
    email: str = "kagiso@ryno-tec.co.za"
    phone: str = "+27 (XXX) XXX XXXX"
    website: str = "ryno-tec.co.za"
    logo_path: Optional[str] = None

    bbbee_level: int = 1
    bbbee_scorecard: str = "Generic"
    bbbee_certificate: str = ""

    professional_indemnity_provider: str = ""
    professional_indemnity_policy: str = ""
    professional_indemnity_cover: float = 5000000.0


@dataclass
class ClientInfo:
    """Client details"""
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    contact_person: Optional[str] = None
    reference: Optional[str] = None


@dataclass
class LineItem:
    """Individual line item in quote/invoice"""
    description: str
    quantity: float
    unit_price: float
    unit: str = "project"
    vat_applicable: bool = True
    service_line: Optional[ServiceLine] = None

    @property
    def subtotal(self) -> float:
        """Calculate subtotal (quantity * unit_price)"""
        return self.quantity * self.unit_price

    @property
    def vat_amount(self) -> float:
        """Calculate VAT amount"""
        if self.vat_applicable:
            return self.subtotal * VAT_RATE
        return 0.0

    @property
    def total(self) -> float:
        """Calculate total (subtotal + VAT)"""
        return self.subtotal + self.vat_amount


@dataclass
class Quote:
    """Quote document"""
    quote_number: int
    client: ClientInfo
    date: datetime = field(default_factory=datetime.now)
    valid_until: datetime = field(default_factory=lambda: datetime.now() + timedelta(days=30))
    company: CompanyInfo = field(default_factory=CompanyInfo)
    line_items: List[LineItem] = field(default_factory=list)
    notes: Optional[str] = None
    terms: Optional[str] = None

    @property
    def subtotal(self) -> float:
        """Total before VAT"""
        return sum(item.subtotal for item in self.line_items)

    @property
    def total_vat(self) -> float:
        """Total VAT amount"""
        return sum(item.vat_amount for item in self.line_items)

    @property
    def total(self) -> float:
        """Total amount (subtotal + VAT)"""
        return self.subtotal + self.total_vat

    def add_line_item(self, line_item: LineItem):
        """Add a line item to the quote"""
        self.line_items.append(line_item)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "quote_number": self.quote_number,
            "date": self.date.isoformat(),
            "valid_until": self.valid_until.isoformat(),
            "client": {
                "name": self.client.name,
                "email": self.client.email,
                "phone": self.client.phone,
                "address": self.client.address,
            },
            "line_items": [
                {
                    "description": item.description,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "unit": item.unit,
                    "subtotal": item.subtotal,
                    "vat": item.vat_amount,
                    "total": item.total,
                }
                for item in self.line_items
            ],
            "subtotal": self.subtotal,
            "vat": self.total_vat,
            "total": self.total,
            "notes": self.notes,
            "terms": self.terms,
        }


@dataclass
class Invoice:
    """Invoice document"""
    invoice_number: int
    client: ClientInfo
    date: datetime = field(default_factory=datetime.now)
    due_date: datetime = field(default_factory=lambda: datetime.now() + timedelta(days=30))
    company: CompanyInfo = field(default_factory=CompanyInfo)
    line_items: List[LineItem] = field(default_factory=list)

    # Payment details
    bank_name: Optional[str] = None
    account_holder: str = "Ryno-Tec Consulting (Pty) Ltd"
    account_number: Optional[str] = None
    branch_code: Optional[str] = None
    reference: Optional[str] = None

    notes: Optional[str] = None

    @property
    def subtotal(self) -> float:
        """Total before VAT"""
        return sum(item.subtotal for item in self.line_items)

    @property
    def total_vat(self) -> float:
        """Total VAT amount"""
        return sum(item.vat_amount for item in self.line_items)

    @property
    def total(self) -> float:
        """Total amount (subtotal + VAT)"""
        return self.subtotal + self.total_vat

    @property
    def is_overdue(self) -> bool:
        """Check if invoice is overdue"""
        return datetime.now() > self.due_date

    @property
    def days_until_due(self) -> int:
        """Days until invoice is due"""
        delta = self.due_date - datetime.now()
        return max(0, delta.days)

    def add_line_item(self, line_item: LineItem):
        """Add a line item to the invoice"""
        self.line_items.append(line_item)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "invoice_number": self.invoice_number,
            "date": self.date.isoformat(),
            "due_date": self.due_date.isoformat(),
            "client": {
                "name": self.client.name,
                "email": self.client.email,
                "phone": self.client.phone,
                "address": self.client.address,
            },
            "line_items": [
                {
                    "description": item.description,
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "unit": item.unit,
                    "subtotal": item.subtotal,
                    "vat": item.vat_amount,
                    "total": item.total,
                }
                for item in self.line_items
            ],
            "subtotal": self.subtotal,
            "vat": self.total_vat,
            "total": self.total,
            "payment": {
                "bank": self.bank_name,
                "account_holder": self.account_holder,
                "account_number": self.account_number,
                "branch_code": self.branch_code,
                "reference": self.reference,
            },
            "notes": self.notes,
            "is_overdue": self.is_overdue,
            "days_until_due": self.days_until_due,
        }


@dataclass
class BidCostItem:
    """Individual cost item for bid costing"""
    service_line: ServiceLine
    description: str
    cost: float
    contingency_percent: float = 0.0
    margin_percent: float = 0.0

    @property
    def contingency_amount(self) -> float:
        """Calculate contingency amount"""
        return self.cost * (self.contingency_percent / 100.0)

    @property
    def cost_with_contingency(self) -> float:
        """Cost + contingency"""
        return self.cost + self.contingency_amount

    @property
    def margin_amount(self) -> float:
        """Calculate margin amount"""
        return self.cost_with_contingency * (self.margin_percent / 100.0)

    @property
    def bid_price(self) -> float:
        """Final bid price (cost + contingency + margin)"""
        return self.cost_with_contingency + self.margin_amount


@dataclass
class BidCosting:
    """Bid costing document for tender response"""
    tender_name: str
    company: CompanyInfo = field(default_factory=CompanyInfo)
    date: datetime = field(default_factory=datetime.now)
    cost_items: List[BidCostItem] = field(default_factory=list)
    tender_budget: Optional[float] = None

    @property
    def total_cost(self) -> float:
        """Sum of all costs"""
        return sum(item.cost for item in self.cost_items)

    @property
    def total_contingency(self) -> float:
        """Sum of all contingencies"""
        return sum(item.contingency_amount for item in self.cost_items)

    @property
    def total_cost_with_contingency(self) -> float:
        """Total cost with contingency"""
        return sum(item.cost_with_contingency for item in self.cost_items)

    @property
    def total_margin(self) -> float:
        """Sum of all margins"""
        return sum(item.margin_amount for item in self.cost_items)

    @property
    def total_bid_price(self) -> float:
        """Total bid price (all costs + contingencies + margins)"""
        return sum(item.bid_price for item in self.cost_items)

    @property
    def budget_variance(self) -> Optional[float]:
        """Variance from tender budget (positive = over budget)"""
        if self.tender_budget is None:
            return None
        return self.total_bid_price - self.tender_budget

    @property
    def within_budget(self) -> Optional[bool]:
        """Check if bid is within tender budget"""
        if self.tender_budget is None:
            return None
        return self.total_bid_price <= self.tender_budget

    def add_cost_item(self, item: BidCostItem):
        """Add a cost item"""
        self.cost_items.append(item)

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "tender_name": self.tender_name,
            "date": self.date.isoformat(),
            "cost_items": [
                {
                    "service_line": item.service_line.value,
                    "description": item.description,
                    "cost": item.cost,
                    "contingency_percent": item.contingency_percent,
                    "contingency_amount": item.contingency_amount,
                    "margin_percent": item.margin_percent,
                    "margin_amount": item.margin_amount,
                    "bid_price": item.bid_price,
                }
                for item in self.cost_items
            ],
            "summary": {
                "total_cost": self.total_cost,
                "total_contingency": self.total_contingency,
                "total_cost_with_contingency": self.total_cost_with_contingency,
                "total_margin": self.total_margin,
                "total_bid_price": self.total_bid_price,
                "tender_budget": self.tender_budget,
                "budget_variance": self.budget_variance,
                "within_budget": self.within_budget,
            }
        }


# ============================================================================
# GENERATORS
# ============================================================================

class DocumentGenerator(ABC):
    """Abstract base class for document generators"""

    @abstractmethod
    def generate_pdf(self, filename: str):
        """Generate PDF output"""
        pass

    @abstractmethod
    def generate_html(self) -> str:
        """Generate HTML output"""
        pass

    def save_json(self, filename: str, data: Dict):
        """Save document data as JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)


class QuoteGenerator(DocumentGenerator):
    """Generate professional quotes"""

    def __init__(self, quote: Quote):
        self.quote = quote

    def generate_html(self) -> str:
        """Generate HTML representation of quote"""
        company = self.quote.company
        client = self.quote.client

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Quote {self.quote.quote_number}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .header {{ margin-bottom: 30px; border-bottom: 2px solid #003366; padding-bottom: 20px; }}
                .company-name {{ font-size: 24px; font-weight: bold; color: #003366; }}
                .document-title {{ font-size: 18px; font-weight: bold; margin-top: 20px; }}
                .info-section {{ display: flex; justify-content: space-between; margin: 20px 0; }}
                .info-block {{ flex: 1; }}
                .info-block strong {{ display: block; font-weight: bold; margin-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th {{ background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; text-align: left; }}
                td {{ border: 1px solid #ddd; padding: 10px; }}
                .amount {{ text-align: right; }}
                .total-section {{ margin-top: 20px; }}
                .total-row {{ display: flex; justify-content: flex-end; margin: 5px 0; }}
                .total-row span:first-child {{ min-width: 150px; }}
                .total-row span:last-child {{ min-width: 100px; text-align: right; font-weight: bold; }}
                .grand-total {{ font-size: 18px; border-top: 2px solid #003366; padding-top: 10px; margin-top: 10px; }}
                .footer {{ margin-top: 40px; font-size: 11px; color: #666; }}
                .vat-notice {{ background-color: #fff3cd; padding: 10px; margin: 20px 0; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <div class="company-name">{company.name}</div>
                <p>{company.address}</p>
                <p>Email: {company.email} | Phone: {company.phone}</p>
                <p>Website: {company.website}</p>
                <div class="document-title">QUOTATION</div>
                <p>Quote #: {self.quote.quote_number} | Date: {self.quote.date.strftime('%Y-%m-%d')}</p>
                <p>Valid until: {self.quote.valid_until.strftime('%Y-%m-%d')}</p>
            </div>

            <div class="info-section">
                <div class="info-block">
                    <strong>Bill To:</strong>
                    <p>{client.name}</p>
                    {f'<p>{client.address}</p>' if client.address else ''}
                    {f'<p>Email: {client.email}</p>' if client.email else ''}
                    {f'<p>Phone: {client.phone}</p>' if client.phone else ''}
                </div>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th class="amount">Quantity</th>
                        <th class="amount">Unit Price</th>
                        <th class="amount">Amount</th>
                    </tr>
                </thead>
                <tbody>
        """

        for item in self.quote.line_items:
            html += f"""
                    <tr>
                        <td>{item.description}</td>
                        <td class="amount">{item.quantity}</td>
                        <td class="amount">R {item.unit_price:,.2f}</td>
                        <td class="amount">R {item.subtotal:,.2f}</td>
                    </tr>
            """

        html += """
                </tbody>
            </table>

            <div class="total-section">
                <div class="total-row">
                    <span>Subtotal:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="total-row">
                    <span>VAT (15%):</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="total-row grand-total">
                    <span>TOTAL:</span>
                    <span>R {:.2f}</span>
                </div>
            </div>
        """.format(self.quote.subtotal, self.quote.total_vat, self.quote.total)

        if self.quote.terms:
            html += f"""
            <div class="vat-notice">
                <strong>Terms & Conditions:</strong>
                <p>{self.quote.terms}</p>
            </div>
            """

        html += f"""
            <div class="vat-notice">
                <strong>B-BBEE Information:</strong>
                <p>Level: {company.bbbee_level} | Scorecard: {company.bbbee_scorecard}</p>
                <p><strong>VAT Registration:</strong> {company.vat_registration or 'See letterhead'}</p>
                <p><strong>POPIA Notice:</strong> Personal information collected is processed in accordance with POPIA.</p>
            </div>

            <div class="footer">
                <p><strong>{company.name}</strong></p>
                <p>Registration: {company.registration_number} | Tax Reference: {company.tax_reference}</p>
                <p>Professional Indemnity Insurance: {company.professional_indemnity_policy}</p>
                <p>This quote is valid until {self.quote.valid_until.strftime('%Y-%m-%d')} and subject to the terms above.</p>
            </div>
        </body>
        </html>
        """

        return html

    def generate_pdf(self, filename: str):
        """Generate PDF (requires reportlab)"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.lib import colors

            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()

            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                textColor=colors.HexColor('#003366'),
                spaceAfter=10
            )
            elements.append(Paragraph(f"{self.quote.company.name}", title_style))
            elements.append(Paragraph(f"QUOTATION #{self.quote.quote_number}", styles['Heading2']))
            elements.append(Spacer(1, 0.3*inch))

            # Build table
            data = [['Description', 'Qty', 'Unit Price', 'Amount']]
            for item in self.quote.line_items:
                data.append([
                    item.description,
                    str(item.quantity),
                    f"R {item.unit_price:,.2f}",
                    f"R {item.subtotal:,.2f}"
                ])

            # Add totals
            data.append(['', '', 'Subtotal:', f"R {self.quote.subtotal:,.2f}"])
            data.append(['', '', 'VAT (15%):', f"R {self.quote.total_vat:,.2f}"])
            data.append(['', '', 'TOTAL:', f"R {self.quote.total:,.2f}"])

            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            elements.append(table)
            doc.build(elements)
            print(f"Quote saved to {filename}")

        except ImportError:
            print("reportlab not installed. Saving HTML instead...")
            html_filename = filename.replace('.pdf', '.html')
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(self.generate_html())
            print(f"HTML quote saved to {html_filename}")

    def save_json(self, filename: str):
        """Save quote data as JSON"""
        super().save_json(filename, self.quote.to_dict())


class InvoiceGenerator(DocumentGenerator):
    """Generate professional invoices"""

    def __init__(self, invoice: Invoice):
        self.invoice = invoice

    def generate_html(self) -> str:
        """Generate HTML representation of invoice"""
        company = self.invoice.company
        client = self.invoice.client

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Invoice {self.invoice.invoice_number}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .header {{ margin-bottom: 30px; border-bottom: 2px solid #003366; padding-bottom: 20px; }}
                .company-name {{ font-size: 24px; font-weight: bold; color: #003366; }}
                .document-title {{ font-size: 18px; font-weight: bold; margin-top: 20px; color: #003366; }}
                .invoice-details {{ display: flex; justify-content: space-between; margin: 20px 0; }}
                .invoice-info {{ flex: 0 1 40%; }}
                .invoice-info strong {{ display: block; font-weight: bold; margin-bottom: 5px; }}
                .bill-to {{ flex: 0 1 40%; }}
                .bill-to strong {{ display: block; font-weight: bold; margin-bottom: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th {{ background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; text-align: left; }}
                td {{ border: 1px solid #ddd; padding: 10px; }}
                .amount {{ text-align: right; }}
                .total-section {{ margin-top: 20px; }}
                .total-row {{ display: flex; justify-content: flex-end; margin: 5px 0; }}
                .total-row span:first-child {{ min-width: 150px; }}
                .total-row span:last-child {{ min-width: 100px; text-align: right; font-weight: bold; }}
                .grand-total {{ font-size: 18px; border-top: 2px solid #003366; padding-top: 10px; margin-top: 10px; }}
                .payment-details {{ background-color: #e8f4f8; padding: 15px; margin: 20px 0; border-radius: 5px; }}
                .footer {{ margin-top: 40px; font-size: 11px; color: #666; border-top: 1px solid #ddd; padding-top: 20px; }}
                .status {{ margin-top: 20px; padding: 10px; background-color: #fff3cd; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <div class="company-name">{company.name}</div>
                <p>{company.address}</p>
                <p>Email: {company.email} | Phone: {company.phone}</p>
                <p>VAT Reg: {company.vat_registration or 'N/A'} | Tax Ref: {company.tax_reference or 'N/A'}</p>
                <div class="document-title">INVOICE</div>
            </div>

            <div class="invoice-details">
                <div class="invoice-info">
                    <strong>Invoice Number:</strong> {self.invoice.invoice_number}
                    <strong>Invoice Date:</strong> {self.invoice.date.strftime('%Y-%m-%d')}
                    <strong>Due Date:</strong> {self.invoice.due_date.strftime('%Y-%m-%d')}
                </div>
                <div class="bill-to">
                    <strong>Bill To:</strong>
                    <p>{client.name}</p>
                    {f'<p>{client.address}</p>' if client.address else ''}
                    {f'<p>Email: {client.email}</p>' if client.email else ''}
                    {f'<p>Phone: {client.phone}</p>' if client.phone else ''}
                </div>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Description</th>
                        <th class="amount">Quantity</th>
                        <th class="amount">Unit Price</th>
                        <th class="amount">Amount</th>
                    </tr>
                </thead>
                <tbody>
        """

        for item in self.invoice.line_items:
            html += f"""
                    <tr>
                        <td>{item.description}</td>
                        <td class="amount">{item.quantity}</td>
                        <td class="amount">R {item.unit_price:,.2f}</td>
                        <td class="amount">R {item.subtotal:,.2f}</td>
                    </tr>
            """

        html += """
                </tbody>
            </table>

            <div class="total-section">
                <div class="total-row">
                    <span>Subtotal:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="total-row">
                    <span>VAT (15%):</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="total-row grand-total">
                    <span>TOTAL DUE:</span>
                    <span>R {:.2f}</span>
                </div>
            </div>
        """.format(self.invoice.subtotal, self.invoice.total_vat, self.invoice.total)

        # Payment details
        if self.invoice.account_number:
            html += f"""
            <div class="payment-details">
                <strong>Payment Details:</strong>
                <p><strong>Bank:</strong> {self.invoice.bank_name}</p>
                <p><strong>Account Holder:</strong> {self.invoice.account_holder}</p>
                <p><strong>Account Number:</strong> {self.invoice.account_number}</p>
                <p><strong>Branch Code:</strong> {self.invoice.branch_code}</p>
                {f'<p><strong>Reference:</strong> {self.invoice.reference}</p>' if self.invoice.reference else ''}
            </div>
            """

        # Status
        if self.invoice.is_overdue:
            html += f"""
            <div class="status" style="background-color: #f8d7da;">
                <strong>⚠️ OVERDUE</strong> - Invoice was due on {self.invoice.due_date.strftime('%Y-%m-%d')}
            </div>
            """

        html += f"""
            <div class="footer">
                <p><strong>{company.name}</strong></p>
                <p>Registration: {company.registration_number}</p>
                <p>B-BBEE Level: {company.bbbee_level} | Professional Indemnity: {company.professional_indemnity_policy}</p>
                <p style="margin-top: 15px; font-style: italic;">Thank you for your business. POPIA Compliant.</p>
            </div>
        </body>
        </html>
        """

        return html

    def generate_pdf(self, filename: str):
        """Generate PDF invoice"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.lib import colors

            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()

            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=20,
                textColor=colors.HexColor('#003366'),
                spaceAfter=10
            )
            elements.append(Paragraph(f"{self.invoice.company.name}", title_style))
            elements.append(Paragraph(f"INVOICE #{self.invoice.invoice_number}", styles['Heading2']))
            elements.append(Spacer(1, 0.3*inch))

            # Build table
            data = [['Description', 'Qty', 'Unit Price', 'Amount']]
            for item in self.invoice.line_items:
                data.append([
                    item.description,
                    str(item.quantity),
                    f"R {item.unit_price:,.2f}",
                    f"R {item.subtotal:,.2f}"
                ])

            # Add totals
            data.append(['', '', 'Subtotal:', f"R {self.invoice.subtotal:,.2f}"])
            data.append(['', '', 'VAT (15%):', f"R {self.invoice.total_vat:,.2f}"])
            data.append(['', '', 'TOTAL DUE:', f"R {self.invoice.total:,.2f}"])

            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            elements.append(table)
            doc.build(elements)
            print(f"Invoice saved to {filename}")

        except ImportError:
            print("reportlab not installed. Saving HTML instead...")
            html_filename = filename.replace('.pdf', '.html')
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(self.generate_html())
            print(f"HTML invoice saved to {html_filename}")

    def save_json(self, filename: str):
        """Save invoice data as JSON"""
        super().save_json(filename, self.invoice.to_dict())


class BidCostingGenerator(DocumentGenerator):
    """Generate bid costing documents"""

    def __init__(self, bid_costing: BidCosting):
        self.bid_costing = bid_costing

    def generate_html(self) -> str:
        """Generate HTML representation"""
        company = self.bid_costing.company

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Bid Costing - {self.bid_costing.tender_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .header {{ margin-bottom: 30px; border-bottom: 2px solid #003366; padding-bottom: 20px; }}
                .company-name {{ font-size: 24px; font-weight: bold; color: #003366; }}
                .document-title {{ font-size: 18px; font-weight: bold; margin-top: 20px; color: #003366; }}
                .tender-info {{ background-color: #f0f0f0; padding: 15px; margin: 20px 0; border-radius: 5px; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th {{ background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; text-align: left; }}
                td {{ border: 1px solid #ddd; padding: 10px; }}
                .amount {{ text-align: right; }}
                .summary-section {{ margin-top: 30px; background-color: #f9f9f9; padding: 20px; border-radius: 5px; }}
                .summary-row {{ display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #ddd; }}
                .summary-row.total {{ font-size: 16px; font-weight: bold; border-top: 2px solid #003366; padding-top: 10px; }}
                .warning {{ background-color: #f8d7da; padding: 15px; margin: 20px 0; border-radius: 5px; color: #721c24; }}
                .success {{ background-color: #d4edda; padding: 15px; margin: 20px 0; border-radius: 5px; color: #155724; }}
                .footer {{ margin-top: 40px; font-size: 11px; color: #666; border-top: 1px solid #ddd; padding-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <div class="company-name">{company.name}</div>
                <div class="document-title">BID COSTING SCHEDULE</div>
            </div>

            <div class="tender-info">
                <strong>Tender:</strong> {self.bid_costing.tender_name}<br>
                <strong>Prepared:</strong> {self.bid_costing.date.strftime('%Y-%m-%d')}<br>
                {f'<strong>Tender Budget:</strong> R {self.bid_costing.tender_budget:,.2f}<br>' if self.bid_costing.tender_budget else ''}
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Service Line</th>
                        <th>Description</th>
                        <th class="amount">Base Cost</th>
                        <th class="amount">Contingency %</th>
                        <th class="amount">Contingency Amt</th>
                        <th class="amount">Margin %</th>
                        <th class="amount">Margin Amt</th>
                        <th class="amount">Bid Price</th>
                    </tr>
                </thead>
                <tbody>
        """

        for item in self.bid_costing.cost_items:
            html += f"""
                    <tr>
                        <td>{item.service_line.value}</td>
                        <td>{item.description}</td>
                        <td class="amount">R {item.cost:,.2f}</td>
                        <td class="amount">{item.contingency_percent:.1f}%</td>
                        <td class="amount">R {item.contingency_amount:,.2f}</td>
                        <td class="amount">{item.margin_percent:.1f}%</td>
                        <td class="amount">R {item.margin_amount:,.2f}</td>
                        <td class="amount"><strong>R {item.bid_price:,.2f}</strong></td>
                    </tr>
            """

        html += """
                </tbody>
            </table>

            <div class="summary-section">
                <div class="summary-row">
                    <span>Total Base Cost:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="summary-row">
                    <span>Total Contingency:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="summary-row">
                    <span>Cost + Contingency:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="summary-row">
                    <span>Total Margin:</span>
                    <span>R {:.2f}</span>
                </div>
                <div class="summary-row total">
                    <span>TOTAL BID PRICE:</span>
                    <span>R {:.2f}</span>
                </div>
        """.format(
            self.bid_costing.total_cost,
            self.bid_costing.total_contingency,
            self.bid_costing.total_cost_with_contingency,
            self.bid_costing.total_margin,
            self.bid_costing.total_bid_price
        )

        # Budget status
        if self.bid_costing.tender_budget:
            if self.bid_costing.within_budget:
                html += f"""
                <div class="success">
                    ✓ Within Budget: Bid price (R {self.bid_costing.total_bid_price:,.2f}) is R {abs(self.bid_costing.budget_variance):,.2f} below budget
                </div>
                """
            else:
                html += f"""
                <div class="warning">
                    ⚠️ OVER BUDGET: Bid price (R {self.bid_costing.total_bid_price:,.2f}) exceeds budget by R {self.bid_costing.budget_variance:,.2f}
                </div>
                """

        html += f"""
            </div>

            <div class="footer">
                <p>Prepared by: {company.name}</p>
                <p>This costing is confidential and prepared for tender submission only.</p>
            </div>
        </body>
        </html>
        """

        return html

    def generate_pdf(self, filename: str):
        """Generate PDF bid costing"""
        try:
            from reportlab.lib.pagesizes import landscape, letter
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.lib import colors

            doc = SimpleDocTemplate(filename, pagesize=landscape(letter))
            elements = []
            styles = getSampleStyleSheet()

            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=18,
                textColor=colors.HexColor('#003366'),
                spaceAfter=10
            )
            elements.append(Paragraph(f"{self.bid_costing.company.name}", title_style))
            elements.append(Paragraph(f"BID COSTING - {self.bid_costing.tender_name}", styles['Heading2']))
            elements.append(Spacer(1, 0.3*inch))

            # Build table
            headers = ['Service Line', 'Description', 'Base Cost', 'Cont %', 'Cont Amt', 'Margin %', 'Margin Amt', 'Bid Price']
            data = [headers]

            for item in self.bid_costing.cost_items:
                data.append([
                    item.service_line.value,
                    item.description,
                    f"R {item.cost:,.0f}",
                    f"{item.contingency_percent:.0f}%",
                    f"R {item.contingency_amount:,.0f}",
                    f"{item.margin_percent:.0f}%",
                    f"R {item.margin_amount:,.0f}",
                    f"R {item.bid_price:,.0f}",
                ])

            # Summary rows
            data.append(['', '', '', '', '', '', 'TOTAL:', f"R {self.bid_costing.total_bid_price:,.0f}"])

            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
                ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#003366')),
                ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            elements.append(table)
            doc.build(elements)
            print(f"Bid costing saved to {filename}")

        except ImportError:
            print("reportlab not installed. Saving HTML instead...")
            html_filename = filename.replace('.pdf', '.html')
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(self.generate_html())
            print(f"HTML bid costing saved to {html_filename}")

    def save_json(self, filename: str):
        """Save bid costing data as JSON"""
        super().save_json(filename, self.bid_costing.to_dict())


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("eTender Pro - Invoice & Quote Generator Module")
    print("=" * 50)

    # Example: Create a quote
    company = CompanyInfo()
    client = ClientInfo(
        name="Tech Corp SA",
        email="procurement@techcorp.co.za",
        address="Johannesburg, SA"
    )

    quote = Quote(quote_number=1001, client=client, company=company)
    quote.add_line_item(LineItem(
        description="Platform Engineering - Infrastructure as Code Implementation",
        quantity=1,
        unit_price=1500000,
        unit="project",
        service_line=ServiceLine.PLATFORM_ENGINEERING
    ))
    quote.add_line_item(LineItem(
        description="Training & Documentation",
        quantity=1,
        unit_price=50000,
        unit="project"
    ))

    generator = QuoteGenerator(quote)
    generator.generate_html()
    generator.save_json("quote_1001.json")
    print(f"\nQuote #1001 - Total: R {quote.total:,.2f} (incl. VAT)")
