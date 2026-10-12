# Ryno-Tec Modules

This directory contains reusable modules for Ryno-Tec Consulting business operations.

## Available Modules

### Invoice & Quote Generator (`invoice-quote-generator/`)

Professional invoice, quote, and bid costing module for generating SA-compliant financial documents.

**Features:**
- 📄 Professional quote generation with Ryno-Tec service templates
- 💰 Invoice management with automatic VAT calculation (15%)
- 📊 Bid costing analysis with contingency and margin calculations
- ✅ SA compliance (VAT, B-BBEE, POPIA, CIPC registration)
- 📥 PDF export with Ryno-Tec branded letterhead
- 📑 Template management and reuse

**Quick Start:**

```python
from modules.invoice_quote_generator import QuoteGenerator

# Create a professional quote
quote = QuoteGenerator(
    client_name="Enterprise Client",
    client_email="client@company.co.za",
    quote_date="2027-01-15"
)

# Add Ryno-Tec service offerings
quote.add_service_line_item(
    service="Platform Engineering",
    description="Infrastructure as Code implementation",
    quantity=1,
    unit_price=1500000
)

# Generate PDF
quote.generate_pdf("Quote_Client_20270115.pdf")
```

**Service Lines:**
- **Platform Engineering** (40% revenue target): Infrastructure as Code, DevOps, Cloud-native design
- **Azure Modern Workplace** (35% revenue target): AVD, Entra ID, Intune, M365
- **AI Infrastructure & MLOps** (25% revenue target): ML pipelines, model deployment, AI governance

**Documentation:**
- Full module documentation: [`docs/modules/INVOICE-QUOTE-GENERATOR.md`](../docs/modules/INVOICE-QUOTE-GENERATOR.md)
- Implementation guide and examples included
- eTender Pro integration guidance

**SA Compliance:**
- Automatic VAT (15%) calculation and display
- B-BBEE level and scorecard tracking
- POPIA compliance notation
- CIPC registration details
- Professional indemnity insurance references

---

## Integration with eTender Pro

The Invoice & Quote Generator is designed to integrate with eTender Pro's bid preparation workflow:

1. **Tender Discovery** → eTender Pro identifies tender opportunity
2. **Quote Generation** → Use this module to generate professional quotes
3. **Bid Costing** → Analyze costs, margins, and budget compliance
4. **Tender Submission** → Export quote and costing to PDF for submission
5. **Post-Award** → Convert approved quote to invoice for project delivery

### API Integration Example:

```python
# From eTender Pro system
from modules.invoice_quote_generator import QuoteGenerator

# Access tender details from eTender Pro
tender_details = etender_api.get_tender(tender_id)

# Create quote from tender scope
quote = QuoteGenerator.from_tender(tender_details)
quote.set_client_from_tender(tender_details['buyer'])
quote.add_services_from_tender_requirements(tender_details['scope'])

# Export for submission
quote.generate_pdf(f"Quote_{tender_id}.pdf")
tender_api.attach_quote_to_submission(quote)
```

---

## Configuration

### Company Details

Configure Ryno-Tec company information in module initialization:

```python
company_info = CompanyInfo(
    name="Ryno-Tec Consulting (Pty) Ltd",
    registration_number="CIPC_NUMBER",
    tax_reference="SARS_TRN",
    vat_registration="VAT_REG_NUMBER",
    address="Johannesburg, South Africa",
    email="kagiso@ryno-tec.co.za",
    phone="+27 (XXX) XXX XXXX",
    website="ryno-tec.co.za",
    vat_rate=0.15,
    bbbee_level=1,
    bbbee_scorecard="Generic"
)
```

### Service Offerings

Pre-configured Ryno-Tec service templates are available:

```python
quote.add_service_line_item(
    service="Platform Engineering",
    description="Custom infrastructure solution",
    quantity=1,
    unit_price=1500000,
    unit="project"
)
```

Available services: `Platform Engineering`, `Azure Modern Workplace`, `AI Infrastructure`

---

## Module Structure

```
invoice-quote-generator/
├── __init__.py              # Module exports and version
├── generator.py             # Core implementation
│   ├── Data Models (dataclasses)
│   ├── DocumentGenerator (abstract base class)
│   ├── QuoteGenerator
│   ├── InvoiceGenerator
│   └── BidCostingGenerator
└── README.md               # This file
```

---

## Dependencies

```
reportlab>=3.6.0          # PDF generation
jinja2>=3.0.0             # HTML templating
pydantic>=1.8.0           # Data validation
python-dateutil>=2.8.0    # Date handling
```

Install with:

```bash
pip install reportlab jinja2 pydantic python-dateutil
```

---

## Usage Examples

### 1. Generate Quote for Tender Bid

```python
from modules.invoice_quote_generator import QuoteGenerator

quote = QuoteGenerator(
    client_name="Large Enterprise SA",
    client_email="procurement@enterprise.co.za",
    quote_date="2027-01-15"
)

quote.add_service_line_item(
    service="Platform Engineering",
    description="IaC Implementation - Terraform & Bicep",
    quantity=1,
    unit_price=1500000
)

quote.add_service_line_item(
    service="Azure Modern Workplace",
    description="AVD design and Entra ID governance",
    quantity=1,
    unit_price=400000
)

quote.set_bbbee_info(
    level=1,
    scorecard="Generic",
    certificate_number="BE-2026-001"
)

quote.generate_pdf("Quote_Enterprise_20270115.pdf")
```

### 2. Generate Invoice for Delivered Project

```python
from modules.invoice_quote_generator import InvoiceGenerator

invoice = InvoiceGenerator(
    client_name="Tech Startup XYZ",
    client_address="123 Main St, Johannesburg",
    invoice_number=1001,
    invoice_date="2027-03-15",
    due_date="2027-04-15"
)

invoice.add_line_item(
    description="Platform Engineering - Phase 1 Delivery",
    quantity=1,
    unit_price=750000,
    vat_applicable=True
)

invoice.set_payment_details(
    bank="Standard Bank",
    account_holder="Ryno-Tec Consulting (Pty) Ltd",
    account_number="1234567890",
    branch_code="051001",
    reference="TechStartupXYZ-Invoice1001"
)

invoice.generate_pdf("Invoice_TechStartup_1001.pdf")
```

### 3. Generate Bid Costing Analysis

```python
from modules.invoice_quote_generator import BidCostingGenerator

bid_cost = BidCostingGenerator(
    tender_name="Department of Digital Transformation - RFP-2027-001",
    tender_budget=5000000
)

bid_cost.add_cost_item(
    service_line="Platform Engineering",
    description="DevOps & CI/CD setup",
    cost=2000000,
    contingency=10,
    margin=25
)

bid_cost.calculate_totals()
bid_cost.check_budget_compliance(tender_budget=5000000)
bid_cost.generate_pdf("BidCosting_DeptDigital_RFP2027001.pdf")
```

---

## Testing

Run module tests:

```bash
python -m pytest tests/test_invoice_quote.py -v
```

---

## Support & Maintenance

For issues or enhancements:
1. Create an issue in GitHub with label `module`
2. Reference the specific module and use case
3. Include example code if applicable

---

**Last Updated:** 2026-10-12  
**Module Version:** 1.0.0  
**Maintained by:** Kagiso Tshukudu
